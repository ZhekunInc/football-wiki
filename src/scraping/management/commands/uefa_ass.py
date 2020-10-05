from django.core.management.base import BaseCommand
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
from main.models import RatingAssociation, Continent, Association, Country

from slugify import slugify


class Command(BaseCommand):
    help = "collect jobs"
    # define logic of command
    def handle(self, *args, **options):
        headers = {
            'User-Agent': "Mozilla/5.0 (X11; CrOS i686 0.12.433) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.77 Safari/534.30"
        }

        # collect html
        html = urlopen(Request('https://terrikon.com/football/uefa_coefs', headers=headers))
        # convert to soup
        soup = BeautifulSoup(html, 'html.parser')
        continent = soup.find("div", class_="ash1").text
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
                    title_ru=continent,
                )
            )
            rating.continent = Continent.objects.get(
                title_ru=continent,
            )
            while i < 550:

                is_new_country = not Country.objects.filter(
                    title_ru=table[i + 2].text
                ).exists()
                if is_new_country:
                    Country.objects.create(
                        title_ru=table[i + 2].text,
                        slug=slugify(table[i + 2].text.lower()),
                        continent=Continent.objects.get(
                            title_ru=continent,
                        )
                    )
                is_no_team = False
                count_team = table[i + 9].text.split('/')
                count_team = int(count_team[0])
                if count_team == 0:
                    is_no_team = True
                Association.objects.create(
                    place=table[i].text,
                    country=Country.objects.get(
                        title_ru=table[i + 2].text,
                    ),
                    rating=RatingAssociation.objects.get(
                        title=rating.title,
                    ),
                    point_year1=table[i + 3].text,
                    point_year2=table[i + 4].text,
                    point_year3=table[i + 5].text,
                    point_year4=table[i + 6].text,
                    point_year5=table[i + 7].text,
                    points=table[i + 8].text,
                    teams=table[i + 9].text,
                    no_teams=is_no_team,
                )
                i = i + 10
            '''
            for td in table:
                row = td.find_all('td')
                for item in row:
                    place = item.text
                    div = item.find('div')
                    count_str = str(count)
                    if place == count_str:
                        number = int(place)
                        print(number)
                    if div is not None:
                        if count <= 3:
                            print(place)
                            print(place)
                            title = div.text
                            title = title.split(
                                '\n\n                        \t                    '
                            )
                            title = (''.join(title))
                            title = title.split('                    ')
                            title = (''.join(title))
                            print(title)
                            
                            Association.objects.create(
                                place=number,
                                country=Country.objects.get(
                                    title_uk=title,
                                ),
                                rating=RatingAssociation.objects.get(
                                    title=rating.title,
                                )
                            )
                        count = count + 1'''
                
            print('ДОДАНО')
        else:
            print('ЄЄЄЄЄЄЄЄ')
        # grab all postings
        '''for p in postings:
            url = p.find('a', class_='posting-btn-submit')['href']
            title = p.find('h5').text
            location = p.find('span', class_='sort-by-location').text
            # check if url in db
            try:
                # save in db
                Job.objects.create(
                    url=url,
                    title=title,
                    location=location
                )
                print('%s added' % (title,))
            except:
                print('%s already exists' % (title,))
        self.stdout.write( 'job complete' )'''