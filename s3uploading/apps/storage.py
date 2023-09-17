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

    def get_object_parameters(self, name):
        """
        it gives us way to control things at object level.
        for special kind of object it can be controlled.
        Here if name of file is abc.png it will should be public otherwise private.
        """
        s3_object_params = {
            'CacheControl': 'max-age=1000',
        }

        if name == 'abc.png':
            s3_object_params['ACL'] = 'public-read'
            return {**s3_object_params}

        return {**s3_object_params}

custom_storage = get_storage_class(settings.CUSTOM_STORAGE)()
