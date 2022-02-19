from pathlib import Path

from calendarapi.settings import BASE_DIR

# Application definition
ROOT_URLCONF = 'calendarapi.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'calendarapi.wsgi.application'


# Static files
MEDIA_URL = '/media/'
MEDIA_ROOT = '/var/calendarapi/media/'

STATIC_URL = '/static/'
STATIC_ROOT = '/var/calendarapi/static/'

# 100mb
DATA_UPLOAD_MAX_MEMORY_SIZE = 1024 * 1024 * 100

FILE_UPLOAD_PERMISSIONS = 0o644

BROKER_URL = 'amqp://rabbit'

AUTH_USER_MODEL = 'users.User'
