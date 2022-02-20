from django.db import transaction

from rest_framework import viewsets, status, mixins
from rest_framework.settings import api_settings
from rest_framework.filters import SearchFilter
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.throttling import AnonRateThrottle
from rest_framework.decorators import action
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from apps.events.serializers import CalendarEventSerializer
from apps.events.filters import *


class CalendarEventsView(mixins.CreateModelMixin,
                         mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin,
                         mixins.ListModelMixin,
                         viewsets.GenericViewSet):
    serializer_class = CalendarEventSerializer
    queryset = CalendarEventSerializer.Meta.queryset

    filter_backends = api_settings.DEFAULT_FILTER_BACKENDS + [SearchFilter]
    filterset_class = CalendarEventFilter
    search_fields = [
        'name',
    ]

    def get_queryset(self):
        return super().get_queryset().filter(created_by=self.request.user)

