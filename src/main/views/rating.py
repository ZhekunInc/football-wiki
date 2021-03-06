from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404
from datetime import datetime
from main.models import Continent, Country, RatingAssociation, RatingTeam, RatingCountry

def get_continent_or_404(continent):
    """Retrieve a Category instance by a continent"""
    continent_bits = [p for p in continent.split('/') if p]
    return get_object_or_404(Continent, slug=continent_bits[-1])


class RatingClubListView(ListView):
    template_name = 'main/rating/club-rating.html'
    context_object_name = "ratings"

    def get_queryset(self):
        """
        Retrieve the category by his continent and
        build a queryset of her published entries.
        """
        self.continent = get_continent_or_404(self.kwargs['continent'])
        return self.continent.club.filter(
            is_published=True,
            published_at__lte=datetime.now()
        ).order_by("place")

    def get_context_data(self, **kwargs):
        """
        Add the current category in context.
        """
        context = super(RatingClubListView, self).get_context_data(**kwargs)
        context['continent'] = self.continent
        return context


class RatingAssociationListView(DetailView):
    template_name = 'main/rating/association-rating.html'
    model = RatingAssociation


class RatingTeamListView(DetailView):
    template_name = 'main/rating/club-rating.html'
    model = RatingTeam


class RatingCountryListView(DetailView):
    template_name = 'main/rating/country-rating.html'
    model = RatingCountry
