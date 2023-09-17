"""
Storage backend example
"""

from django.conf import settings
from django.core.files.storage import get_storage_class
from storages.backends.s3boto3 import S3Boto3Storage


class CustomStorageBackend(S3Boto3Storage):
    """
    S3 backend for course metadata export
    """
    def __init__(self):
        bucket_name = settings.PRIVATE_IMAGE_BACKEND['STORAGE_KWARGS']['bucket_name']
        acl = settings.PRIVATE_IMAGE_BACKEND['STORAGE_KWARGS']['default_acl']
        super().__init__(
            bucket_name=bucket_name, default_acl=acl, querystring_auth=True
        )

custom_storage = get_storage_class(settings.CUSTOM_STORAGE)()
