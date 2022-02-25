import logging
import requests
import io
import ics
from urllib.parse import quote
from django.db import transaction

from calendarapi.celery_app import app
from apps.holidays.models import Holiday, Country


def download_file(url, filename=None):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with io.BytesIO() as f:
            for chunk in r.iter_content(chunk_size=8192):
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk:
                f.write(chunk)
            buffer = f.getvalue()
    buffer = buffer.decode()
    return buffer


@app.task
def process_sync_holidays_for_countries():
    logger = logging.getLogger('django')
    with transaction.atomic():
        for country in Country.objects.all():
            try:
                logger.info(f'{country.name} downloading...')
                data = download_file(
                    f'https://www.officeholidays.com/ics/ics_country.php?tbl_country={quote(country.name)}',
                    country.name)
                calendar = ics.Calendar(data) if data else None
            except Exception as e:
                # logger.exception(e)
                continue
            if calendar is None:
                continue
            for event in calendar.events:
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


