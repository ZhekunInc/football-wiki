from django.urls import path, include
from django.views.generic import TemplateView
from main.views.main import HomePageView
from django.views.generic import ListView, DetailView
from main.models import Continent, Country
from main.views.main import ContinentDetail, CountryDetail, LeagueDetail, ClubDetail, SearchResultsView, PlayerDetail, CupDetail
from main.views.club_change import ClubCreateView, ClubTitleUpdateView, ClubInfoUpdateView, ClubTrophyUpdateView, ClubPlayerUpdateView, ClubMainUpdateView
from main.views.player_change import PlayerCreateView, PlayerTitleUpdateView, PlayerInfoUpdateView, PlayerTrophyUpdateView, PlayerClubUpdateView, PlayerMainUpdateView
from main.views.detail import ContinentAbout


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
    path('create-player/', PlayerCreateView.as_view(), name='player_create'),
    path('trophies_and_awards/<cup>-<pk>/', CupDetail.as_view(), name='cup_detail'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('players/<player>-<pk>/', PlayerDetail.as_view(), name='player_detail'),
    path('about-<continent>-<pk>/', ContinentAbout.as_view(), name='continent_about'),
    path('players/<player>-<pk>/player-title-update/', PlayerTitleUpdateView.as_view(), name='player_title_update'),
    path('players/<player>-<pk>/player-info-update/', PlayerInfoUpdateView.as_view(), name='player_info_update'),
    path('players/<player>-<pk>/player-main-update/', PlayerMainUpdateView.as_view(), name='player_main_update'),
    path('players/<player>-<pk>/player-club-update/', PlayerClubUpdateView.as_view(), name='player_club_update'),
    path('players/<player>-<pk>/player-trophy-update/', PlayerTrophyUpdateView.as_view(), name='player_trophy_update'),
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
    path('<continent>/<country>/<league>/<club>-<pk>/club-main-update/', ClubMainUpdateView.as_view(), name='club_main_update'),

]