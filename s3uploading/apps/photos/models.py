from django.core.files.storage import get_storage_class
from django.db import models

import logging
log = logging.getLogger(__name__)


class ImageByDefaultStorage(models.Model):
    """ Here it will use django default storages."""
    image = models.FileField(upload_to='default_storages/images')


class PrivateImage(models.Model):
    image = models.FileField(upload_to='private/images')


class PublicImage(models.Model):
    image = models.FileField()
