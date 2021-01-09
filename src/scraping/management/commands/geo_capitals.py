from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
from geography.models import Country, Continent

from slugify import slugify

import requests


class Command(BaseCommand):
    help = "collect jobs"
    # define logic of command

    def handle(self, *args, **options):
        url = 'http://merkator.org.ua/dovidnyk/stolyci-krajin-svitu/'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        table = soup.find_all('td')

        i = 0
        count = 0
        while i < 1112:
            char = table[i + 2].text.find("(")
            if table[i].text == '' or table[i + 1].text == '' or char != -1:
                print(table[i + 2].text)
                i += 4
                count += 1
            else:
                is_new = not Country.objects.filter(
                    title=table[i + 2].text
                ).exists()
                is_new_continent = not Continent.objects.filter(
                    title=table[i + 3].text
                ).exists()
                if is_new_continent:
                    Continent.objects.create(
                        title=table[i + 3].text,
                        slug=slugify(table[i + 3].text.lower()),
                        is_published=False,
                    )
                if is_new:
                    Country.objects.create(
                        title=table[i + 2].text,
                        slug=slugify(table[i + 2].text.lower()),
                        capital=table[i + 1].text,
                        continent=Continent.objects.get(
                            title=table[i + 3].text,
                        ),
                    )
                i += 4
        print(count)
