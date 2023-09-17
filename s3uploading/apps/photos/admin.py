from django.contrib import admin

from s3uploading.apps.photos.models import (
    PrivateImage, PublicImage, CustomImageBackendExample, ImageByDefaultStorage
)


admin.site.register(ImageByDefaultStorage)
admin.site.register(PrivateImage)
admin.site.register(PublicImage)
admin.site.register(CustomImageBackendExample)
