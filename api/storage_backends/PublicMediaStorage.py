# myapp/storage_backends/PublicMediaStorage.py
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage

class PublicMediaStorage(S3Boto3Storage):
    location = getattr(settings, 'AWS_PUBLIC_MEDIA_LOCATION', 'media/uploaded_documents')
    file_overwrite = True 
    # custom_domain = f'{settings.AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    # Other settings specific to your use case
    # ...
