from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.views.generic.base import View
from django.shortcuts import get_object_or_404
from datetime import datetime
from django.core.paginator import Paginator
from main.models import Country, Continent, League, Club, Player, Cup
from django.db.models import Q

def get_continent_or_404(continent):
    """Retrieve a Category instance by a continent"""
    continent_bits = [p for p in continent.split('/') if p]
    return get_object_or_404(Continent, slug=continent_bits[-1])

def get_country_or_404(country):
    """Retrieve a Category instance by a continent"""
    country_bits = [p for p in country.split('/') if p]
    return get_object_or_404(Country, slug=country_bits[-1])

def get_league_or_404(league):
    """Retrieve a Category instance by a continent"""
    league_bits = [p for p in league.split('/') if p]
    return get_object_or_404(League, slug=league_bits[-1])

class HomePageView(ListView):

    def home(request):
        from django.utils import translation
        #user_language = 'fi'
        #translation.activate(user_language)
        #request.session[translation.LANGUAGE_SESSION_KEY] =user_language
        if translation.LANGUAGE_SESSION_KEY in request.session:
            del request.session[translation.LANGUAGE_SESSION_KEY]

    def get(self, request):
        clubs = Club.objects.all().order_by("-published_at")
        paginator = Paginator(clubs, 20)
        page = request.GET.get('page')
        clubs = paginator.get_page(page)
        return render(request, "main/homepage.html", {'clubs': clubs})

class ContinentDetail(ListView):
    template_name = 'main/country_list.html'
    context_object_name = "countries"

    def get_queryset(self):
        """
        Retrieve the category by his continent and
        build a queryset of her published entries.
        """
        self.continent = get_continent_or_404(self.kwargs['continent'])
        return self.continent.country.filter(
            is_published=True,
            published_at__lte=datetime.now()
        ).order_by("title")

    def get_context_data(self, **kwargs):
        """
        Add the current category in context.
        """
        context = super(ContinentDetail, self).get_context_data(**kwargs)
        context['continent'] = self.continent
        return context

class CountryDetail(ListView):
    template_name = 'main/league_list.html'
    context_object_name = "leagues"

    def get_queryset(self):
        """
        Retrieve the category by his continent and
        build a queryset of her published entries.
        """
        self.country = get_country_or_404(self.kwargs['country'])
        return self.country.league.filter(
            is_published=True,
            published_at__lte=datetime.now()
        ).order_by("reputation")

    def get_context_data(self, **kwargs):
        """
        Add the current category in context.
        """
        context = super(CountryDetail, self).get_context_data(**kwargs)
        context['country'] = self.country
        return context

class LeagueDetail(ListView):

    template_name = 'main/club_list.html'
    context_object_name = "clubs"

    def get_queryset(self):
        """
        Retrieve the category by his continent and
        build a queryset of her published entries.
        """
        self.league = get_league_or_404(self.kwargs['league'])
        return self.league.club.filter(
            is_published=True,
            published_at__lte=datetime.now()
        ).order_by("title")

    def get_context_data(self, **kwargs):
        """
        Add the current category in context.
        """
        context = super(LeagueDetail, self).get_context_data(**kwargs)
        context['league'] = self.league
        return context

class ClubDetail(DetailView):
    model = Club
    template_name = 'main/club_detail.html'

class PlayerDetail(DetailView):
    model = Player
    template_name = 'main/player_detail.html'

class CupDetail(DetailView):
    model = Cup
    template_name = 'main/cup_detail.html'

class SearchResultsView(ListView):
    template_name = "main/search_results.html"

    def get(self, request, *args, **kwargs):
        query = request.GET.get('q')

        country = Country.objects.none()
        league = League.objects.none()
        club = Club.objects.none()
        player = Player.objects.none()
        cup = Cup.objects.none()
        if query:
            country = Country.objects.all().filter(
                Q(title__icontains=query)
            )
            league = League.objects.all().filter(
                Q(title__icontains=query)
            )
            club = Club.objects.all().filter(
                Q(title__icontains=query) | Q(stadium__icontains=query)
            )
            player = Player.objects.all().filter(
                Q(title__icontains=query) | Q(nickname__icontains=query)
            )
            cup = Cup.objects.all().filter(
                Q(title__icontains=query)
            )
        return render(
            self.request,
            self.template_name,
            context={
                'query': query,
                'search_country': country,
                'search_league': league,
                'search_club': club,
                'search_player': player,
                'search_cup': cup,
            }
        )