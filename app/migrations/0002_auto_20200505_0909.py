# Generated by Django 3.0.5 on 2020-05-05 09:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='imageupload',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Created By'),
        ),
        migrations.AlterField(
            model_name='imageupload',
            name='count',
            field=models.PositiveIntegerField(default=0, help_text='The total number of letters.', verbose_name='Count'),
        ),
        migrations.AlterField(
            model_name='imageupload',
            name='file_name',
            field=models.CharField(blank=True, help_text='The original file name of the image file, which is automatically extracted from the file.', max_length=255, null=True, verbose_name='File Name'),
        ),
        migrations.AlterField(
            model_name='imageupload',
            name='image',
            field=models.ImageField(help_text='An image file.', null=True, upload_to='image/%Y/%m/%d/', verbose_name='Image'),
        ),
        migrations.AlterField(
            model_name='imageupload',
            name='letters',
            field=models.TextField(blank=True, help_text='Which are automatically extracted from the image after the image file is saved.', max_length=10000, null=True, verbose_name='Letters'),
        ),
    ]
