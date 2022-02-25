from rest_framework import serializers, exceptions
from rest_framework_simplejwt.settings import api_settings as jwt_settings
from rest_framework_simplejwt.tokens import RefreshToken

from drf_spectacular.utils import extend_schema_field

from apps.users.models import User
from apps.users.fields import PasswordField


class JwtSerializer(serializers.Serializer):
    refresh = serializers.CharField(read_only=True)
    access = serializers.CharField(read_only=True)

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class RegistrationSerializer(serializers.ModelSerializer):
    password = PasswordField()
    token = serializers.SerializerMethodField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].write_only = True

    @extend_schema_field(JwtSerializer)
    def get_token(self, user: User):
        refresh = RefreshToken.for_user(user)
        return {'access': str(refresh.access_token), 'refresh': str(refresh)}

    class Meta:
        model = User
        model_fields = (
            'password',
            'email',
            'country'
        )
        extra_fields = (
            'token',
        )
        fields = model_fields + extra_fields
        queryset = User.objects.only(*model_fields)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'email',
        )
