from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
from main.models import RatingTeam, Continent, Team, Club, League, Country

from slugify import slugify

import requests


class Command(BaseCommand):
    help = "collect jobs"
    # define logic of command

    def handle(self, *args, **options):
        print("URL:")
        url = input()
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find_all('td')
        print(table[1].text)

        url = url.split('/')
        continent = 'УЄФА'
        if url[6] == 'ukraine' and url[7] == '1':
            country = 'УКРАЇНА'
            reputation = 1
            league = 'Українська Прем\'єр-ліга'
            print(league)
        elif url[6] == 'ukraine' and url[7] == '2':
            country = 'УКРАЇНА'
            reputation = 2
            league = 'Чемпіонат України Перша ліга'
            print(league)
        elif url[6] == 'ukraine' and url[7] == '6':
            country = 'УКРАЇНА'
            reputation = 3
            league = 'Чемпіонат України Друга ліга. Гр. А'
            print(league)
        elif url[6] == 'ukraine' and url[7] == '7':
            country = 'УКРАЇНА'
            reputation = 4
            league = 'Чемпіонат України Друга ліга. Гр. Б'
            print(league)
        elif url[6] == 'england':
            country = 'Англія'
            league = 'Прем\'єр-ліга'
        elif url[6] == 'germany':
            country = 'Німеччина'
            league = 'Бундесліга'
        elif url[6] == 'spain':
            country = 'Іспанія'
            league = 'Ла Ліга'
        elif url[6] == 'italy':
            country = 'Італія'
            league = 'Серія А'
        elif url[6] == 'france':
            country = 'Франція'
            league = 'Ліга 1'
        elif url[6] == 'poland':
            country = 'Польща'
            league = 'Екстракласа'
        elif url[6] == 'belgium':
            country = 'Бельгія'
            league = 'Ліга Жюпілер'
        elif url[6] == 'greece':
            country = 'Греція'
            league = 'Чемпіонат Греції Суперліга'
        elif url[6] == 'holland':
            country = 'Нідерланди'
            league = 'Ередивізі'
        elif url[6] == 'portugal':
            country = 'Португалія'
            league = 'Ліга НОС'
        elif url[6] == 'romania':
            country = 'Румунія'
            league = 'Ліга I'
        elif url[6] == 'turkey':
            country = 'Туреччина'
            league = 'Чемпіонат Туреччини Суперліга'
        elif url[6] == 'russia':
            country = 'Росія'
            league = 'Чемпіонат Росії Прем\'єр-ліга'
        elif url[6] == 'brazil':
            country = 'Бразилія'
            league = 'Серія A (Бразилія)'
        elif url[6] == 'argentina':
            country = 'Аргентина'
            league = 'Чемпіонат Аргентини Прімера'
        is_new_league = not League.objects.filter(
            title_uk=league
        ).exists()
        if is_new_league:
            count_team = len(table) / 9
            League.objects.create(
                title_uk=league,
                slug=slugify(league.lower()),
                country=Country.objects.get(
                    title_uk=country
                ),
                count_team=count_team,
                reputation=reputation,
            )
        i = 0
        print(len(table))
        while i < len(table):
            is_new_club = not Club.objects.filter(
                title_uk=table[i + 1].text
            )
            if is_new_club:
                Club.objects.create(
                    title_uk=table[i + 1].text,
                    slug=slugify(table[i + 1].text.lower()),
                    continent=Continent.objects.get(
                        title_uk=continent
                    ),
                    country=Country.objects.get(
                        title_uk=country
                    ),
                    league=League.objects.get(
                        title_uk=league
                    )
                )
            i = i + 9

        '''print(continent)
        continent = continent.split(' ')
        continent = continent[2]
        table = soup.find_all('td')
        i = 0
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

            while i < 1800:
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
                        print(table[i + j])
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
            print('ЄЄЄЄЄЄЄЄ')'''
