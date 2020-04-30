from django.db import models

from django.utils.translation import gettext_lazy as _


class ImageUpload(models.Model):
    image = models.ImageField(_('Image'), null=True, upload_to='image/%Y/%m/%d/')
    file_name = models.CharField(_('File Name'), max_length=255, null=True, blank=True)
    letters = models.TextField(_('Letters'), max_length=10000, null=True, blank=True)
    count = models.PositiveIntegerField(_('Count'), default=0)
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
