import datetime
import pytz
from rest_framework import serializers, exceptions
from rest_framework_simplejwt.settings import api_settings as jwt_settings
from rest_framework_simplejwt.tokens import RefreshToken
from django.utils import timezone
from drf_spectacular.utils import extend_schema_field

from apps.events.models import CalendarEvent


class CalendarEventSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.fields['end_at'].required = False
        self.fields['end_at'].allow_null = True

    def validate(self, attrs):
        notification_interval_type = attrs.get('notification_interval_type', None)
        if notification_interval_type is not None:
            attrs['notification_interval'] = CalendarEvent.INTERVAL_TIMEDELTA[notification_interval_type]

        if not attrs.get('end_at'):
            attrs['end_at'] = timezone.datetime.combine(
                timezone.localdate(attrs['start_at'], pytz.UTC),
                datetime.time(0, 0, 0)
            ) + timezone.timedelta(days=1) - timezone.timedelta(milliseconds=1)
        return attrs

    class Meta:
        model = CalendarEvent
        model_fields = (
            'id',
            'name',
            'notification_interval_type',
            'start_at',
            'end_at',
            'created_by',
        )

        fields = model_fields
        queryset = CalendarEvent.objects.select_related(
            'created_by',
        ).only(*model_fields)
