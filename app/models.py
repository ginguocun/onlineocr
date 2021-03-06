import os
from pathlib import Path

from django.conf import settings
from django.db import models

from django.utils.translation import gettext_lazy as _

from app.ocr import get_letters_from_image


class ImageUpload(models.Model):
    image = models.ImageField(_('Image'), help_text=_('An image file.'), null=True, upload_to='image/%Y/%m/%d/')
    file_name = models.CharField(
        _('File Name'),
        help_text=_('The original file name of the image file, which is automatically extracted from the file.'),
        max_length=255, null=True, blank=True)
    letters = models.TextField(
        _('Letters'),
        help_text=_('Which are automatically extracted from the image after the image file is saved.'),
        max_length=10000, null=True, blank=True)
    count = models.PositiveIntegerField(
        _('Count'),
        help_text=_('The total number of letters.'),
        default=0)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        verbose_name=_('Created By')
    )
    created_at = models.DateTimeField(_('Created At'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated At'), auto_now=True)

    objects = models.Manager()

    class Meta:
        ordering = ['-id']
        verbose_name = _('Image Upload')
        verbose_name_plural = _('Image Uploads')

    def __str__(self):
        return "{0} {1}".format(
            self.pk,
            self.file_name,
        )

    def get_file_name(self):
        """
        Get the file_name from the image
        """
        if self.image and not self.file_name:
            self.file_name = Path(getattr(self, 'image').name).name

    def save(self, *args, **kwargs):
        # save the file_name of the image
        self.get_file_name()
        super(ImageUpload, self).save(*args, **kwargs)
        if self.image:
            path = os.path.join(settings.MEDIA_ROOT, self.image.name)
            # get the letters from the image
            letters = get_letters_from_image(path)
            if isinstance(letters, list):
                self.letters = letters
                self.count = len(letters)
            super(ImageUpload, self).save(update_fields=['letters', 'count'])
