from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from apps.users.managers import CalendarAPIUserManager
# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('country')
        verbose_name_plural = _('countries')


class Holiday(models.Model):
    name = models.CharField(max_length=100)
    begin = models.DateField(_('holiday begin date'), db_index=True)
    end = models.DateField(_('holiday end date'), db_index=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='holidays')
    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.country.name}: {self.name} {self.begin.strftime("%Y.%m.%d")} {self.end.strftime("%Y.%m.%d")}'

    class Meta:
        verbose_name = _('holiday')
        verbose_name_plural = _('holidays')
