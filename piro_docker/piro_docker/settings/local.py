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

