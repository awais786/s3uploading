from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files.storage import get_storage_class
from django.db import models
from storages.backends.s3boto3 import S3Boto3Storage
import requests
import random

from s3uploading.apps.storage import custom_storage_backend


class ImageByDefaultStorage(models.Model):  # example 1
    """ Here it will use django default storages which is right now s3boto3."""
    # it will use s3boto3 because default storage is defined as s3boto3.
    image = models.FileField(upload_to='public_images_1/images')


class PublicImage(models.Model):    # example 1
    """ Here using storages from settings."""
    image = models.FileField(storage=S3Boto3Storage, upload_to='public_images_2/images')


class PrivateImage(models.Model):
    """ Here using get_storage_class method to get s3boto3 object with specific keywords """
    private_storage = get_storage_class(
        settings.PRIVATE_IMAGE_BACKEND['class']
    )(**settings.PRIVATE_IMAGE_BACKEND['STORAGE_KWARGS'])

    image = models.FileField(storage=private_storage, upload_to='private_storages/images')


def saving_steam(image):
    list1 = [1, 2, 3, 4, 5, 11, 12, 13, 14, 15, 16]
    name = random.choice(list1)
    response = requests.get(image)
    buff = ContentFile(response.content)
    custom = custom_storage_backend
    custom_storage_backend.save(f'{name}.jpg', buff)
    return custom.url(f'{name}.jpg')


class CustomImageBackendExample(models.Model):
    """ Here using get_storage_class method to get s3boto3 object with specific keywords """
    image = models.URLField(max_length=250)

    def save(self, *args, **kwargs):
        url = saving_steam(self.image)
        self.image = url
        return super(CustomImageBackendExample, self).save(*args, **kwargs)




