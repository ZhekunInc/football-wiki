from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
import requests


class Command(BaseCommand):
    help = "collect jobs"
    # define logic of command
    def handle(self, *args, **options):
        url = 'https://uk.wikipedia.org/wiki/%D0%A4%D0%86%D0%A4%D0%90_100'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        player_item = soup.find_all("ul")
        players = player_item[1].find_all('li')
        for player in players:
            info = player.find_all('a')
            name = info[0].text
            country = player.find('span')
            if country is None:
                country = info[2].text
            else:
                country = country.text
            if country == 'СРСР':
                country = 'Росія'
            '''link = player.find('a')['href']
            url = 'https://uk.wikipedia.org/%s' % link
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
            }
            response = requests.get(url, headers=headers)
            detail = BeautifulSoup(response.text, 'html.parser')
            text = detail.find_all('p')
            info = ""
            i = 2
            if name == 'Йоган Нескенс':
                info += text[i].text
            else:
                while i < 7:
                    info += text[i].text
                    i += 1'''
            print(name)
            print(country)
