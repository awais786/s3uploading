from django.contrib import admin

from s3uploading.apps.photos.models import (
    PrivateImageExample, PublicImageExample, CustomImageBackendExample, DefaultStorageExample
)


admin.site.register(DefaultStorageExample)
admin.site.register(PrivateImageExample)
admin.site.register(PublicImageExample)
admin.site.register(CustomImageBackendExample)
