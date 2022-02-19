from django.urls import (
    include,
    path,
)

from rest_framework.routers import SimpleRouter

from apps.events.views import *

router = SimpleRouter()
router.register('events', CalendarEventsView, basename='events')

urlpatterns = [
    path('', include(router.urls)),
]
