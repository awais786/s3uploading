# s3uploading
#### How do I run this project?

## Create Environment
```
python -m venv env_s3uploading
```

## Activate the environment
```
source env_s3uploading/bin/activate
```

## run following command to install requirements, create user and runserver
```
make install_requirements
make runserver
```

## Add AWS credentials in ur private.py
```
AWS_ACCESS_KEY_ID = ""
AWS_SECRET_ACCESS_KEY = ""
AWS_STORAGE_BUCKET_NAME = ""
```

## CustomImageBackend 
`It is using private acl. It also shows override method to change any specific obect also.`

## Image by default storages 
`It is using default storage as s3boto3 and its acl is public-read`

## Private images
`private acl`

## Public images
`using public-read via settings.yml`

## s3boto3 settings orders
1: First it picks settings `AWS_DEFAULT_ACL` or `AWS_BUCKET_ACL`
2: If bucket level settings exists then it overrides first one ```
PUBCLIC_IMAGE_BACKEND:
  class: storages.backends.s3boto3.S3Boto3Storage
  STORAGE_KWARGS:
    bucket_name: awaisqureshi
    default_acl: public-read
```
3: If following `object_parameters` exists then it overrides both above2.
```
PUBCLIC_IMAGE_BACKEND:
  class: storages.backends.s3boto3.S3Boto3Storage
  STORAGE_KWARGS:
    bucket_name: awaisqureshi
    default_acl: private
  object_parameters:
    CacheControl: max-age-3600
    default_acl: public-read
```

