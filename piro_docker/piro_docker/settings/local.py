from piro_docker.settings.base import *
from piro_docker.settings.secrets import get_secrets

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': get_secrets('DATABASE_NAME'),
        'USER': get_secrets('DATABASE_USER'),
        'PASSWORD': get_secrets('DATABASE_PASSWORD'),
        'HOST': get_secrets('DATABASE_HOST'),
        'PORT': get_secrets('DATABASE_PORT'),
    }
}

# AWS MEDIA
AWS_REGION = get_secrets('AWS_REGION')
AWS_STORAGE_BUCKET_NAME = get_secrets('AWS_STORAGE_BUCKET_NAME')
AWS_ACCESS_KEY_ID = get_secrets('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = get_secrets('AWS_SECRET_ACCESS_KEY')

AWS_QUERYSTRING_AUTH = False
AWS_S3_HOST = 's3.%s.amazonaws.com' % AWS_REGION
AWS_S3_CUSTOM_DOMAIN = get_secrets('AWS_CLOUDFRONT_DOMAIN')

# Static Setting
AWS_STATIC_LOCATION = 'static'
STATIC_URL = "https://%s/%s/" % (AWS_S3_CUSTOM_DOMAIN, AWS_STATIC_LOCATION)
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# Media Setting
MEDIA_URL = "https://%s/" % AWS_S3_CUSTOM_DOMAIN
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

