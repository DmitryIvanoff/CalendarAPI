from rest_framework import serializers, exceptions
from rest_framework_simplejwt.settings import api_settings as jwt_settings
from rest_framework_simplejwt.tokens import RefreshToken

from drf_spectacular.utils import extend_schema_field

from apps.events.models import CalendarEvent


class CalendarEventSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    def validate(self, attrs):
        notification_interval_type = attrs.get('notification_interval_type', None)
        if notification_interval_type is not None:
            attrs['notification_interval'] = CalendarEvent.INTERVAL_TIMEDELTA[notification_interval_type]
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
