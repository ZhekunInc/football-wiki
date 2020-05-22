from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.views.generic.base import View
from django.shortcuts import get_object_or_404
from datetime import datetime
from django.core.paginator import Paginator
from main.models import Country, Continent, League, Club, Player, Cup
from django.db.models import Q


class ContinentAbout(DetailView):
    model = Continent
    template_name = 'main/detail/continent-detail.html'

class CountryAbout(DetailView):
    model = Country
    template_name = 'main/detail/country-detail.html'

class LeagueAbout(DetailView):
    model = League
    template_name = 'main/detail/league-detail.html'