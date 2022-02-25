from django.urls import (
    include,
    path,
)

from rest_framework.routers import SimpleRouter

from apps.holidays.views import *

router = SimpleRouter()
router.register('holidays', HolidayView, basename='holidays')
router.register('countries', CountryView, basename='countries')
urlpatterns = [
    path('', include(router.urls)),
]
