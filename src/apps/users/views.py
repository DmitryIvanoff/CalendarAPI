from django.db import transaction

from rest_framework import viewsets, status, mixins
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework.throttling import AnonRateThrottle
from rest_framework.decorators import action
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from apps.users.models import User
from apps.users.serializers import RegistrationSerializer


class RegisterView(mixins.CreateModelMixin,
                   viewsets.GenericViewSet):
    serializer_class = RegistrationSerializer
    queryset = RegistrationSerializer.Meta.queryset
    permission_classes = [AllowAny, ]

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        new_user = User.objects.create_user(**serializer.validated_data)
        serializer = self.get_serializer(instance=new_user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)