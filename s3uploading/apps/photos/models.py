from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files.storage import get_storage_class
from django.db import models
from storages.backends.s3boto3 import S3Boto3Storage
import requests
import random

from s3uploading.apps.storage import custom_storage_backend


class DefaultStorageExample(models.Model):  # example 1
    """ Here it will use django default storages which is right now s3boto3."""
    # it will use s3boto3 because default storage is defined as s3boto3.
    image = models.FileField(upload_to='public_images_1/images')


class PublicImageExample(models.Model):    # example 1
    """ Here using storages from settings."""
    image = models.FileField(storage=S3Boto3Storage, upload_to='public_images_2/images')


class PrivateImageExample(models.Model):
    """ Here using get_storage_class method to get s3boto3 object with specific keywords """
    private_storage = get_storage_class(
        settings.PRIVATE_IMAGE_BACKEND['class']
    )(**settings.PRIVATE_IMAGE_BACKEND['STORAGE_KWARGS'])

    image = models.FileField(storage=private_storage, upload_to='private_storages/images')


def saving_steam(image, acl):
    list1 = [1, 2, 3, 4, 5, 11, 12, 13, 14, 15, 16]
    name = random.choice(list1)
    response = requests.get(image)
    buff = ContentFile(response.content)

    custom = custom_storage_backend

    if acl == 'public':
        custom.object_parameters = {"ACL": "public-read"}

    custom_storage_backend.save(f'{name}.jpg', buff)
    return custom.url(f'{name}.jpg')


class CustomImageBackendExample(models.Model):
    """ its an example to download any image and save it with custom backend. """
    ACL_SELECT = (
        ('private', 'private'),
        ('public', 'public'),
    )

    ACL_TYPE = models.CharField(max_length=11, choices=ACL_SELECT, default='pvt')
    image = models.URLField(
        max_length=250,
        default='https://www.edx.org/contentful/ii9ehdcj88bc/2SkUwC7Kf9G5I5b49hjVgu/1fa2453e92e46d980f9f99cf08a51e73/image_processing.jpg'
    )

    def save(self, *args, **kwargs):
        url = saving_steam(self.image, self.ACL_TYPE)
        self.image = url
        return super(CustomImageBackendExample, self).save(*args, **kwargs)


