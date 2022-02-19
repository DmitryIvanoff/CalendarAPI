"""
reactor API URL Configuration.
"""
from rest_framework.routers import SimpleRouter
from django.urls import (
    include,
    path,
)

app_name = 'api-v1'
router = SimpleRouter()


urlpatterns = [
    path('', include(router.urls)),
    path('', include('apps.users.urls')),
    path('', include('apps.events.urls'))
]
