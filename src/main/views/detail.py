from django.views.generic import DetailView
from main.models import Country, Continent, League


class ContinentAbout(DetailView):
    model = Continent
    template_name = 'main/detail/continent-detail.html'

class CountryAbout(DetailView):
    model = Country
    template_name = 'main/detail/country-detail.html'

class LeagueAbout(DetailView):
    model = League
    template_name = 'main/detail/league-detail.html'
