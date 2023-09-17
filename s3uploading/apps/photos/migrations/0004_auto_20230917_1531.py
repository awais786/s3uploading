# Generated by Django 3.2.19 on 2023-09-17 15:31

from django.db import migrations, models
import storages.backends.s3boto3


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_auto_20230917_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagebydefaultstorage',
            name='image',
            field=models.FileField(upload_to='public_images_1/images'),
        ),
        migrations.AlterField(
            model_name='publicimage',
            name='image',
            field=models.FileField(storage=storages.backends.s3boto3.S3Boto3Storage, upload_to='public_images_2/images'),
        ),
    ]
