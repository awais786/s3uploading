from django.db import models
from django.core.files.storage import get_storage_class
import io
from django.core.files.base import ContentFile

from django.conf import settings

from s3uploading.apps.storage import custom_storage


class ImageByDefaultStorage(models.Model):
    """ Here it will use django default storages."""
    image = models.FileField(upload_to='default_storages/images')


class PrivateImage(models.Model):
    """ Here using get_storage_class method to get s3boto3 object with specific keywords """
    custom_storage = get_storage_class(
        settings.PRIVATE_IMAGE_BACKEND['class']
    )(**settings.PRIVATE_IMAGE_BACKEND['STORAGE_KWARGS'])

    image = models.FileField(storage=custom_storage, upload_to='private/images')


class CustomImageBackendExample(models.Model):
    """ Here using get_storage_class method to get s3boto3 object with specific keywords """
    image = models.FileField(upload_to='custom_backend/images')

    def save(self, *args, **kwargs):
        buffer = ContentFile(self.image._file.file.read())

        # pass the images to customs storage.
        custom_storage.save(self.image._file.name, buffer)
        super(CustomImageBackendExample, self).save(*args, **kwargs)


class PublicImage(models.Model):
    """ Here using storages from settings."""
    image = models.FileField(upload_to='public/images')
