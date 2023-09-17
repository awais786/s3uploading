from django.db import models


class ImageByDefaultStorage(models.Model):
    """ Here it will use django default storages."""
    image = models.FileField(upload_to='default_storages/images')


class PrivateImage(models.Model):
    image = models.FileField(upload_to='private/images')


class PublicImage(models.Model):
    image = models.FileField()

    def save(self, *args, **kwargs):
        import pdb;
        pdb.set_trace()
        super(PublicImage, self).save(*args, **kwargs)
