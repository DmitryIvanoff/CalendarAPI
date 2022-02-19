DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PART_APPS = [
    'rest_framework',
    'corsheaders',
    'django_filters',
    'django_extensions',
    # 'django_celery_beat',
]

LOCAL_APPS = [
    'apps.users',
]

DEV_APPS = [
    'drf_spectacular',
    # 'drf_spectacular_sidecar',
    'silk',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PART_APPS + LOCAL_APPS + DEV_APPS
