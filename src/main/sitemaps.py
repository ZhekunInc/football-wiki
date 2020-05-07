from django.contrib.sitemaps import Sitemap
from main.models import Continent, Country, League, Club, Cup, Player

class ContinentSitemap(Sitemap):

    def items(self):
        return Continent.objects.all()

class CountrySitemap(Sitemap):

    def items(self):
        return Country.objects.all()

class LeagueSitemap(Sitemap):

    def items(self):
        return League.objects.all()

class ClubSitemap(Sitemap):

    def items(self):
        return Club.objects.all()

class CupSitemap(Sitemap):

    def items(self):
        return Cup.objects.all()

class PlayerSitemap(Sitemap):

    def items(self):
        return Player.objects.all()
