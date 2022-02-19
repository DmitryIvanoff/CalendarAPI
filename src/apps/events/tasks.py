import logging
import traceback
from django.db.models.functions import Now
from django.db.models import F, Value
from smtplib import SMTPException
from django.utils import timezone
from django.conf import settings
from django.core.mail import (
    EmailMessage,
)
from calendarapi.celery_app import app
from apps.events.models import CalendarEvent

MESSAGE_NOTIFICATION_TEMPLATE = """
Здравствуйте!
Напоминаем, что событие "{name}" начнется через {interval} в {start_at}.

by Calendar App

"""


@app.task
def process_events_notifications():
    logger = logging.getLogger('django')
    events = CalendarEvent.objects.filter(
        notification_sent=False,
        start_at__lte=Now() + F('notification_interval'),
        start_at__gte=Now() + F('notification_interval') - timezone.timedelta(seconds=120)
    ).all()
    for event in events:
        try:
            email = EmailMessage(
                subject=f'Оповещение о событии {event.name}',
                body=MESSAGE_NOTIFICATION_TEMPLATE.format(
                    name=event.name,
                    interval=event.get_notification_interval_type_display(),
                    start_at=event.start_at.strftime('%d.%m.%Y %H:%M')),
                from_email=settings.SERVER_EMAIL,
                to=[event.created_by.email],
            )
            email.send()

        except SMTPException as exc:
            logger.warning(
                f'Ошибка при отправке письма. Повтор:'
                f' method: send_book_request_far_session_reminders'
                f' traceback: {traceback.format_exc()}',
            )

        except Exception as e:
            logger.exception(e)
        else:
            event.notification_sent = True
    CalendarEvent.objects.bulk_update(events, ['notification_sent'])
