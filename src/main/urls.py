from django.urls import path, include
from .views import HomePageView
from django.views.generic import ListView, DetailView
from main.models import Continent, Country
from .views import ContinentDetail, CountryDetail, LeagueDetail, ClubDetail, SearchResultsView

urlpatterns = [
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('', HomePageView.as_view(), name='home_page'),
    path('<continent>/', ContinentDetail.as_view(), name='country_list'),
    path('<continent>/<country>/', CountryDetail.as_view(), name='league_list'),
    path('<continent>/<country>/<league>/', LeagueDetail.as_view(), name='club_list'),
    path('<continent>/<country>/<league>/<club>-<pk>/', ClubDetail.as_view(), name='club_detail'),
]
