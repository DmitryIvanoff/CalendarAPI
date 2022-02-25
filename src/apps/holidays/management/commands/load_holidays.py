import logging
import ics
import re
import requests.exceptions
from urllib.parse import quote
from apps.holidays.tasks import download_file
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from apps.holidays.models import Country, Holiday
UserModel = get_user_model()


class Command(BaseCommand):
    help = 'cкачивает список праздников для каждой страны с https://www.officeholidays.com/'

    def handle(self, *args, **options):
        logger = logging.getLogger('django')
        for country in Country.objects.all():
            try:
                logger.info(f'{country.name} downloading...')
                data = download_file(f'https://www.officeholidays.com/ics/ics_country.php?tbl_country={ quote(country.name)}',
                                     country.name)
                calendar = ics.Calendar(data) if data else None
            except Exception as e:
                # logger.exception(e)
                continue
            if calendar is None:
                continue

            for event in calendar.events:
                print(event.begin, event.end)
                obj, created = Holiday.objects.update_or_create(
                    name=event.name.split(': ')[1],
                    begin=event.begin.date(),
                    end=event.end.date(),
                    description=event.description,
                    country=country
                )
                if created:
                    logger.info(f'{obj} created')
                else:
                    logger.info(f'{obj} updated')
