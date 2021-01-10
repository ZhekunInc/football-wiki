from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
from geo.models import Country

from slugify import slugify

import requests


class Command(BaseCommand):
    help = "collect jobs"
    # define logic of command

    def handle(self, *args, **options):
        url = 'http://merkator.org.ua/dovidnyk/prapory-krajin-svitu-za-rehionamy/'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        flags = soup.find_all('figure', class_='wp-block-image')
        for flag in flags:
            url = flag.find('a')['href']
            title = flag.find('span').text
            print(title)

            is_new = Country.objects.filter(
                title=title
            ).exists()

            if is_new:
                product = Country.objects.get(
                    title=title
                )

                product.flag = url

                product.save()
        '''
        is_new = not RatingTeam.objects.filter(
            title=continent
        ).exists()
        if is_new:
            rating = RatingTeam.objects.create(
                title=continent,
                continent=Continent.objects.get(
                    title_uk=continent,
                )
            )

            while i < 180:
                title = table[i + 1].text
                title = title.split(
                    '\n\n\n                        \t                    '
                )
                title = (''.join(title))
                title = title.split('                    \n')
                title = (''.join(title))
                is_new_club = not Club.objects.filter(
                    title_uk=title
                ).exists()
                if is_new_club:
                    Club.objects.create(
                        title_uk=title,
                        slug=slugify(title.lower()),
                        continent=Continent.objects.get(
                            title_uk=continent,
                        )
                    )
                for j in range(2, 7):
                    if table[i + j].text == '–':
                        table[i + j] = None
                    else:
                        table[i + j] = table[i + j].text
                Team.objects.create(
                    place=table[i].text,
                    club=Club.objects.get(
                        title_uk=title,
                    ),
                    rating=RatingTeam.objects.get(
                        title=rating.title,
                    ),
                    point_year1=table[i + 2],
                    point_year2=table[i + 3],
                    point_year3=table[i + 4],
                    point_year4=table[i + 5],
                    point_year5=table[i + 6],
                    points=table[i + 7].text,
                )
                i = i + 9
            print('ДОДАНО')
        else:
            rating = RatingTeam.objects.filter(title=continent).delete()
            print('ВИДАЛЕНО')
            rating = RatingTeam.objects.create(
                title=continent,
                continent=Continent.objects.get(
                    title_uk=continent,
                )
            )

            while i < 180:
                title = table[i + 1].text
                title = title.split(
                    '\n\n\n                        \t                    '
                )
                title = (''.join(title))
                title = title.split('                    \n')
                title = (''.join(title))
                is_new_club = not Club.objects.filter(
                    title_uk=title
                ).exists()

                if is_new_club:
                    Club.objects.create(
                        title_uk=title,
                        slug=slugify(title.lower()),
                        continent=Continent.objects.get(
                            title_uk=continent,
                        )
                    )
                for j in range(2, 7):
                    if table[i + j].text == '–':
                        table[i + j] = None
                    else:
                        table[i + j] = table[i + j].text
                Team.objects.create(
                    place=table[i].text,
                    club=Club.objects.get(
                        title_uk=title,
                    ),
                    rating=RatingTeam.objects.get(
                        title=rating.title,
                    ),
                    point_year1=table[i + 2],
                    point_year2=table[i + 3],
                    point_year3=table[i + 4],
                    point_year4=table[i + 5],
                    point_year5=table[i + 6],
                    points=table[i + 7].text,
                )
                i = i + 9
            print('ДОДАНО')
        '''