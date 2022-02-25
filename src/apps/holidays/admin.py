from django.contrib import admin
from apps.holidays.models import Country, Holiday


@admin.register(Holiday)
class HolidayAdmin(admin.ModelAdmin):
    list_filter = (
        'begin',
        'end'
    )


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    readonly_fields = (
        'name',
    )
