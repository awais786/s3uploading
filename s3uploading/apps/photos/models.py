from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files.storage import get_storage_class
from django.db import models
from storages.backends.s3boto3 import S3Boto3Storage

from s3uploading.apps.storage import custom_storage


class ImageByDefaultStorage(models.Model):  # example 1
    """ Here it will use django default storages which is right now s3boto3."""
    # it will use s3boto3 because default storage is defined as s3boto3.
    image = models.FileField(upload_to='public_images_1/images')


class PublicImage(models.Model):    # example 1
    """ Here using storages from settings."""
    image = models.FileField(storage=S3Boto3Storage, upload_to='public_images_2/images')


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
        custom_storage.save(self.image._file.name, buffer)
        super(CustomImageBackendExample, self).save(*args, **kwargs)

