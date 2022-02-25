import re

from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import requests
from apps.holidays.models import Country
from bs4 import BeautifulSoup
UserModel = get_user_model()


class Command(BaseCommand):
    help = 'cкачивает список стран с https://www.officeholidays.com/countries'

    def handle(self, *args, **options):
        response = requests.get('https://www.officeholidays.com/countries')
        soup = BeautifulSoup(response.text, 'html.parser')
        divs = soup.findAll('div', class_='four omega columns')
        links = []
        for column in divs:
            links += column.findAll('a')
        for country in (re.search(r'(?<=/)[^/]+$', link['href']).group() for link in links):
            Country.objects.update_or_create(name=country)
        self.stdout.write(self.style.SUCCESS(f'Successfully downloaded'))