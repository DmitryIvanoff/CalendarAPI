import os

from django.conf import settings

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'calendarapi.settings')

app = Celery('calendarapi', broker=settings.BROKER_URL)

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.update(
    # beat_scheduler='django_celery_beat.schedulers:DatabaseScheduler',
    beat_schedule={
        'process_events_notifications': {
            'task': 'apps.events.tasks.process_events_notifications',
            'schedule': 30.0  # run task every 10 secs
        },
        'process_sync_holidays_for_countries': {
            'task': 'apps.holidays.tasks.process_sync_holidays_for_countries',
            'schedule': 24*60*60  # run task every 24 hrs
        },
    },
    # result_backend='redis://localhost:6379/2'
)
