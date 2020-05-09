from django.urls import path, include
from django.views.generic import TemplateView
from .views import HomePageView
from django.views.generic import ListView, DetailView
from main.models import Continent, Country
from .views import ContinentDetail, CountryDetail, LeagueDetail, ClubDetail, SearchResultsView, PlayerDetail, CupDetail
from .views import ClubCreateView, ClubTitleUpdateView, ClubInfoUpdateView, ClubTrophyUpdateView, ClubPlayerUpdateView


urlpatterns = [
    path(
        'create-center/',
        TemplateView.as_view(
            template_name='main/create_center.html',
            get_context_data=lambda: {'is_create_center': True}
        ),
        name='create_center'
    ),
    path('create-club/', ClubCreateView.as_view(), name='club_create'),
    path('trophies_and_awards/<cup>-<pk>/', CupDetail.as_view(), name='cup_detail'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('players/<player>-<pk>/', PlayerDetail.as_view(), name='player_detail'),
]

urlpatterns += [
    path('', HomePageView.as_view(), name='home_page'),
    path('<continent>/', ContinentDetail.as_view(), name='country_list'),
    path('<continent>/<country>/', CountryDetail.as_view(), name='league_list'),
    path('<continent>/<country>/<league>/', LeagueDetail.as_view(), name='club_list'),
    path('<continent>/<country>/<league>/<club>-<pk>/', ClubDetail.as_view(), name='club_detail'),
    path('<continent>/<country>/<league>/<club>-<pk>/club-title-update/', ClubTitleUpdateView.as_view(), name='club_title_update'),
    path('<continent>/<country>/<league>/<club>-<pk>/club-info-update/', ClubInfoUpdateView.as_view(), name='club_info_update'),
    path('<continent>/<country>/<league>/<club>-<pk>/club-trophy-update/', ClubTrophyUpdateView.as_view(), name='club_trophy_update'),
    path('<continent>/<country>/<league>/<club>-<pk>/club-player-update/', ClubPlayerUpdateView.as_view(), name='club_player_update'),
]