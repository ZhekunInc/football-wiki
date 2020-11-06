from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
from main.models import RatingCountry, Continent, FifaCountry, Country

from slugify import slugify

import requests

class Command(BaseCommand):
    help = "collect jobs"
    # define logic of command

    def handle(self, *args, **options):
        url = 'https://www.championat.com/football/fifa/'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        continent = soup.find("div", class_='entity-header__title-name').text
        continent = continent.split(
            '\n                                            '
        )
        continent = (''.join(continent))
        continent = continent.split(' ')
        continent = continent[1]
        table = soup.find_all('td')
        print(len(table))
        i = 0
        is_new = not RatingCountry.objects.filter(
            title=continent
        ).exists()
        if is_new:
            rating = RatingCountry.objects.create(
                title=continent,
                continent=Continent.objects.get(
                    title_ru=continent,
                )
            )
            while i < 1470:
                title = table[i + 2].text
                title = title.split(
                    '\n\n\n \n'
                )
                title = (''.join(title))
                title = title.split(
                    '\n\n'
                )
                title = (''.join(title))
                point = ((table[i + 3]).text).split(' ')
                point = int((''.join(point)))
                print(point)
                is_new_country = not Country.objects.filter(
                    title_ru=title
                ).exists()
                if is_new_country:
                    Country.objects.create(
                        title_ru=title,
                        slug=slugify(title.lower()),
                        continent=Continent.objects.get(
                            title_ru=table[i + 5].text,
                        )
                    )
                FifaCountry.objects.create(
                    place=table[i].text,
                    country=Country.objects.get(
                        title_ru=title,
                    ),
                    rating=RatingCountry.objects.get(
                        title=rating.title,
                    ),
                    points=point,
                    place_continent=table[i + 6].text
                )
                i = i + 7

            print('ДОДАНО')
        else:
            rating = RatingCountry.objects.filter(title=continent).delete()
            print('ВИДАЛЕНО')

            rating = RatingCountry.objects.create(
                title=continent,
                continent=Continent.objects.get(
                    title_ru=continent,
                )
            )
            while i < 1470:
                title = table[i + 2].text
                title = title.split(
                    '\n\n\n \n'
                )
                title = (''.join(title))
                title = title.split(
                    '\n\n'
                )
                title = (''.join(title))
                point = ((table[i + 3]).text).split(' ')
                point = int((''.join(point)))
                is_new_country = not Country.objects.filter(
                    title_ru=title
                ).exists()
                if is_new_country:
                    Country.objects.create(
                        title_ru=title,
                        slug=slugify(title.lower()),
                        continent=Continent.objects.get(
                            title_ru=table[i + 5].text,
                        )
                    )
                FifaCountry.objects.create(
                    place=table[i].text,
                    country=Country.objects.get(
                        title_ru=title,
                    ),
                    rating=RatingCountry.objects.get(
                        title=rating.title,
                    ),
                    points=point,
                    place_continent=table[i + 6].text
                )
                i = i + 7

            print('ДОДАНО')
