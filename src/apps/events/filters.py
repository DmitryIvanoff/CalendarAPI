import datetime

import pytz
from django_filters import rest_framework as filters
from django.utils import timezone
from datetime import timedelta
from dateutil.rrule import rrule, MONTHLY, DAILY
from apps.events.models import CalendarEvent


class CalendarEventFilter(filters.FilterSet):
    month = filters.DateTimeFilter(field_name='start_at', method='filter_month')
    day = filters.DateTimeFilter(field_name='start_at', method='filter_day')

    def filter_day(self, queryset, name, value):
        qs = queryset
        if value:
            curr_day = timezone.localdate(value, pytz.UTC)
            curr_day, next_day = rrule(DAILY, count=2, dtstart=curr_day)
            qs = queryset.filter(**{f'{name}__date__gte': curr_day, f'{name}__date__lt': next_day}).order_by(f'{name}')
        return qs

    def filter_month(self, queryset, name, value):
        qs = queryset
        if value:
            first_month_day = timezone.localdate(value, pytz.UTC).replace(day=1)
            curr_month, next_month = rrule(MONTHLY, count=2, dtstart=first_month_day)
            qs = queryset.filter(**{f'{name}__date__gte': curr_month, f'{name}__date__lt': next_month}).order_by(f'{name}')
        return qs

    class Meta:
        model = CalendarEvent
        fields = (
            'month',
            'day'
        )