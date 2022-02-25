from django.db import transaction

from rest_framework import viewsets, status, mixins
from rest_framework.permissions import AllowAny
from apps.holidays.serializers import HolidaySerializer, CountrySerializer


class HolidayView(mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = HolidaySerializer
    queryset = HolidaySerializer.Meta.queryset
    ordering = 'begin'

    def get_queryset(self):
        return super().get_queryset().filter(country=self.request.user.country)


class CountryView(mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = CountrySerializer
    queryset = CountrySerializer.Meta.queryset
    permission_classes = (AllowAny, )
    pagination_class = None
