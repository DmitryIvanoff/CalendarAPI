# Generated by Django 3.2.12 on 2022-02-19 18:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CalendarEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('start_at', models.DateTimeField(db_index=True, verbose_name='start time')),
                ('end_at', models.DateTimeField(db_index=True, verbose_name='end time')),
                ('notification_interval', models.DurationField(blank=True, null=True)),
                ('notification_interval_type', models.SmallIntegerField(blank=True, choices=[(0, 'day'), (1, 'hour'), (2, '2 hours'), (3, '4 hours'), (4, 'week')], null=True)),
                ('notification_sent', models.BooleanField(default=False)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to=settings.AUTH_USER_MODEL, verbose_name='creator')),
            ],
            options={
                'verbose_name': 'calendar event',
                'verbose_name_plural': 'calendar events',
            },
        ),
    ]
