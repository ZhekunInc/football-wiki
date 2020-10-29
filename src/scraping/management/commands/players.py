from django.core.management.base import BaseCommand
from bs4 import BeautifulSoup
from main.models import RatingTeam, Continent, Team, Club, League, Country

from slugify import slugify

import requests

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located


class Command(BaseCommand):
    help = "collect jobs"
    # define logic of command

    def handle(self, *args, **options):
        url = 'http://www.ranker.com/crowdranked-list/the-best-soccer-players-of-all-time?page=20'
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        }
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        link = soup.find('a', class_='pagination_link__3Dsfn')
        links = soup.find_all('a', class_='gridItem_name__3zasT gridItem_nameLink__3jE6V')
        print(link.text)
        print(link['href'])
        for a in links:
            print(a.text)



        #This example requires Selenium WebDriver 3.13 or newer
        with webdriver.Chrome('/home/zhekun/Desktop/chromedriver') as driver:
            wait = WebDriverWait(driver, 10)
            driver.get("http://www.ranker.com/crowdranked-list/the-best-soccer-players-of-all-time")
            cheese = driver.find_elements_by_css_selector(".gridView_main__2R52j li")
            for foo in cheese:
                print(foo.text)
