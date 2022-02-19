from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.core.exceptions import ValidationError


class CalendarEvent(models.Model):
    INTERVAL_DAY = 0
    INTERVAL_1HOUR = 1
    INTERVAL_2HOUR = 2
    INTERVAL_4HOUR = 3
    INTERVAL_WEEK = 4
    INTERVAL_CHOICES = (
        (INTERVAL_DAY, _('day')),
        (INTERVAL_1HOUR, _('hour')),
        (INTERVAL_2HOUR, _('2 hours')),
        (INTERVAL_4HOUR, _('4 hours')),
        (INTERVAL_WEEK, _('week'))
    )

    INTERVAL_TIMEDELTA = {
        INTERVAL_DAY: timezone.timedelta(days=1),
        INTERVAL_1HOUR: timezone.timedelta(hours=1),
        INTERVAL_2HOUR: timezone.timedelta(hours=2),
        INTERVAL_4HOUR: timezone.timedelta(hours=4),
        INTERVAL_WEEK: timezone.timedelta(weeks=1)
    }
    # -----

    name = models.CharField(max_length=150)

    start_at = models.DateTimeField(_('start time'), db_index=True)
    end_at = models.DateTimeField(_('end time'), db_index=True)

    notification_interval = models.DurationField(null=True, blank=True)
    notification_interval_type = models.SmallIntegerField(choices=INTERVAL_CHOICES, null=True, blank=True)
    notification_sent = models.BooleanField(default=False)

    created_by = models.ForeignKey(
        'users.User',
        on_delete=models.CASCADE,
        verbose_name=_('creator'),
        related_name=_('events')
    )
    # -----

    @property
    def notification_time(self):
        if self.notification_interval_type is None:
            return None
        return self.start_at - self.notification_interval

    def __str__(self):
        return f'({self.pk}) {self.name}'

    def clean(self):
        if self.notification_interval is not None and self.notification_interval_type is None:
            raise ValidationError(_('notification interval type is not set'))
        elif self.notification_interval is None and self.notification_interval_type is not None:
            ValidationError(_('notification interval is not set'))

    class Meta:
        verbose_name = _('calendar event')
        verbose_name_plural = _('calendar events')

