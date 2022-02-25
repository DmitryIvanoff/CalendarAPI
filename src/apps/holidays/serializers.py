from rest_framework import serializers, exceptions
from rest_framework_simplejwt.settings import api_settings as jwt_settings
from rest_framework_simplejwt.tokens import RefreshToken

from drf_spectacular.utils import extend_schema_field

from apps.holidays.models import Holiday, Country


class CountryField(serializers.PrimaryKeyRelatedField):
    def to_representation(self, value):
        return str(value.name)

    def use_pk_only_optimization(self):
        return False


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        model_fields = (
            'id',
            'name',
        )

        fields = model_fields
        queryset = Country.objects.only(*model_fields)


class HolidaySerializer(serializers.ModelSerializer):
    country = CountryField(queryset=Country.objects.all())

    class Meta:
        model = Holiday
        model_fields = (
            'name',
            'begin',
            'end',
            'description',
            'country',
        )

        fields = model_fields
        queryset = Holiday.objects.only(*model_fields)

