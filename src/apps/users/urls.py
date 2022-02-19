from django.urls import (
    include,
    path,
)

from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from rest_framework.routers import SimpleRouter

from apps.users.views import *

router = SimpleRouter()
router.register('register', RegisterView, basename='register')

urlpatterns = [
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('login/', TokenObtainPairView.as_view(), name='login'),

    path('', include(router.urls)),
]
