from django.contrib.sitemaps import Sitemap
from main.models import Continent, Country, League, Club, Cup, Player

class ContinentSitemap(Sitemap):
    priority = 0.6
    changefreq = "monthly"
    i18n = True

    def items(self):
        return Continent.objects.all()

class CountrySitemap(Sitemap):
    priority = 0.6
    changefreq = "monthly"
    i18n = True

    def items(self):
        return Country.objects.all()

class LeagueSitemap(Sitemap):
    priority = 0.6
    changefreq = "monthly"
    i18n = True

    def items(self):
        return League.objects.all()

class ClubSitemap(Sitemap):
    priority = 0.6
    changefreq = "monthly"
    i18n = True

    def items(self):
        return Club.objects.all()

class CupSitemap(Sitemap):
    priority = 0.6
    changefreq = "monthly"
    i18n = True

    def items(self):
        return Cup.objects.all()

class PlayerSitemap(Sitemap):
    priority = 0.6
    changefreq = "monthly"
    i18n = True

    def items(self):
        return Player.objects.all()
