from django.contrib import admin

from s3uploading.apps.photos.models import PrivateImage, PublicImage


admin.site.register(PrivateImage)
admin.site.register(PublicImage)
