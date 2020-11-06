from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
from main.models import RatingAssociation, Continent, Association, Country

from slugify import slugify

import requests


class Command(BaseCommand):
    help = "collect jobs"
    # define logic of command

    def handle(self, *args, **options):
        url = 'https://sport.ua/uk/ranking/uefa'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        continent = soup.find("h1").text
        continent = continent.split(' ')
        continent = continent[2]
        table = soup.find_all('td')
        print(len(table))
        i = 0
        is_new = not RatingAssociation.objects.filter(
            title=continent
        ).exists()
        if is_new:
            rating = RatingAssociation.objects.create(
                title=continent,
                continent=Continent.objects.get(
                    title_uk=continent,
                )
            )
            while i < 495:

                title = table[i + 1].text.split(
                    '\n\n\n                        \t                    '
                )
                title = (''.join(title))
                title = title.split('                    \n')
                title = (''.join(title))
                is_new_country = not Country.objects.filter(
                    title_uk__icontains=title
                ).exists()
                if is_new_country:
                    Country.objects.create(
                        title_uk=title,
                        slug=slugify(title.lower()),
                        continent=Continent.objects.get(
                            title_uk=continent,
                        )
                    )
                is_no_team = False
                count_team = table[i + 8].text.split('/')
                count_team_1 = int(count_team[0])
                count_team_2 = int(count_team[1])
                if count_team_1 == 7:
                    is_no_team = False
                    team = str(count_team_1) + '/' + str(count_team_2)
                elif count_team_1 == count_team_2:
                    is_no_team = True
                    team = '0' + '/' + str(count_team_2)
                elif count_team_1 == 0:
                    is_no_team = True
                    team = '0' + '/' + str(count_team_2)
                else:
                    is_no_team = False
                    team = str(count_team_1) + '/' + str(count_team_2)
                Association.objects.create(
                    place=table[i].text,
                    country=Country.objects.get(
                        title_uk=title,
                    ),
                    rating=RatingAssociation.objects.get(
                        title=rating.title,
                    ),
                    point_year1=table[i + 2].text,
                    point_year2=table[i + 3].text,
                    point_year3=table[i + 4].text,
                    point_year4=table[i + 5].text,
                    point_year5=table[i + 6].text,
                    points=table[i + 7].text,
                    teams=team,
                    no_teams=is_no_team,
                )
                i = i + 9

            print('ДОДАНО')
        else:
            rating = RatingAssociation.objects.filter(title=continent).delete()
            print('ВИДАЛЕНО')

            rating = RatingAssociation.objects.create(
                title=continent,
                continent=Continent.objects.get(
                    title_uk=continent,
                )
            )
            while i < 495:

                title = table[i + 1].text.split(
                    '\n\n\n                        \t                    '
                )
                title = (''.join(title))
                title = title.split('                    \n')
                title = (''.join(title))
                is_new_country = not Country.objects.filter(
                    title_uk__icontains=title
                ).exists()
                if is_new_country:
                    Country.objects.create(
                        title_uk=title,
                        slug=slugify(title.lower()),
                        continent=Continent.objects.get(
                            title_uk=continent,
                        )
                    )
                is_no_team = False
                count_team = table[i + 8].text.split('/')
                count_team_1 = int(count_team[0])
                count_team_2 = int(count_team[1])
                if count_team_1 == 7:
                    is_no_team = False
                    team = str(count_team_1) + '/' + str(count_team_2)
                elif count_team_1 == count_team_2:
                    is_no_team = True
                    team = '0' + '/' + str(count_team_2)
                elif count_team_1 == 0:
                    is_no_team = True
                    team = '0' + '/' + str(count_team_2)
                else:
                    is_no_team = False
                    team = str(count_team_1) + '/' + str(count_team_2)
                Association.objects.create(
                    place=table[i].text,
                    country=Country.objects.get(
                        title_uk=title,
                    ),
                    rating=RatingAssociation.objects.get(
                        title=rating.title,
                    ),
                    point_year1=table[i + 2].text,
                    point_year2=table[i + 3].text,
                    point_year3=table[i + 4].text,
                    point_year4=table[i + 5].text,
                    point_year5=table[i + 6].text,
                    points=table[i + 7].text,
                    teams=team,
                    no_teams=is_no_team,
                )
                i = i + 9

            print('ДОДАНО')
