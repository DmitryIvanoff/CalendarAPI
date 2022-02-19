from django.contrib import admin
from apps.events.models import CalendarEvent


@admin.register(CalendarEvent)
class CalendarEventAdmin(admin.ModelAdmin):
    list_filter = (
        'start_at',
        'end_at',
        'notification_sent'
    )
    list_display = (
        'name',
        'start_at',
        'end_at',
        'notification_interval_type',
        'notification_sent'
    )
    search_fields = (
        'name',
    )