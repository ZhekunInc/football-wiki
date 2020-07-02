from django.urls import path
from django.views.generic import TemplateView
from main.views.main import HomePageView
from main.views.main import ContinentDetail, CountryDetail, LeagueDetail
from main.views.main import ClubDetail, SearchResultsView, PlayerDetail
from main.views.main import CupDetail, PlayerList, CupList
from main.views.club_change import ClubCreateView, ClubTitleUpdateView
from main.views.club_change import ClubInfoUpdateView, ClubTrophyUpdateView
from main.views.club_change import ClubPlayerUpdateView, ClubMainUpdateView
from main.views.player_change import PlayerCreateView, PlayerTitleUpdateView
from main.views.player_change import PlayerInfoUpdateView
from main.views.player_change import PlayerTrophyUpdateView
from main.views.player_change import PlayerClubUpdateView, PlayerMainUpdateView
from main.views.cup_change import CupCreateView, CupTitleUpdateView
from main.views.cup_change import CupInfoUpdateView, CupClubUpdateView
from main.views.cup_change import CupCountryUpdateView, CupMainUpdateView
from main.views.country_change import CountryCreateView, CountryTitleUpdateView
from main.views.country_change import CountryMainUpdateView
from main.views.country_change import CountryInfoUpdateView
from main.views.continent_change import ContinentTitleUpdateView
from main.views.continent_change import ContinentMainUpdateView
from main.views.continent_change import ContinentInfoUpdateView
from main.views.league_change import LeagueCreateView
from main.views.league_change import LeagueTitleUpdateView
from main.views.league_change import LeagueMainUpdateView
from main.views.league_change import LeagueInfoUpdateView
from main.views.detail import ContinentAbout, CountryAbout, LeagueAbout
from main.views.rating import RatingClubListView, RatingCountryListView, RatingAssociationListView


urlpatterns = [
    path(
        'create-center/',
        TemplateView.as_view(
            template_name='main/create_center.html',
            get_context_data=lambda: {'is_create_center': True}
        ),
        name='create_center'
    ),
    path(
        'all-ratings/',
        TemplateView.as_view(
            template_name='main/all-rating.html',
            get_context_data=lambda: {'is_all_rating': True}
        ),
        name='all_rating'
    ),
    path(
        'club-rating/',
        TemplateView.as_view(
            template_name='main/rating/main-club.html',
            get_context_data=lambda: {'is_club_rating': True}
        ),
        name='club_rating'
    ),
    path(
        'association-rating/',
        TemplateView.as_view(
            template_name='main/rating/main-association.html',
            get_context_data=lambda: {'is_association_rating': True}
        ),
        name='association_rating'
    ),
    path(
        'country-rating/',
        RatingCountryListView.as_view(),
        name='country_rating'
    ),
    path(
        'club-rating/rating-<continent>/',
        RatingClubListView.as_view(),
        name='club-rating_page'
    ),
    path(
        'association-rating/rating-<continent>/',
        RatingAssociationListView.as_view(),
        name='association-rating_page'
    ),
    path(
        'players/',
        PlayerList.as_view(),
        name='players_page'
    ),
    path(
        'trophies_and_awards/',
        CupList.as_view(),
        name='cups_page'
    ),
    path('create-club/', ClubCreateView.as_view(), name='club_create'),
    path(
        'create-country/',
        CountryCreateView.as_view(),
        name='country_create'
    ),
    path(
        'create-league/',
        LeagueCreateView.as_view(),
        name='league_create'
    ),
    path('create-player/', PlayerCreateView.as_view(), name='player_create'),
    path('create-cup/', CupCreateView.as_view(), name='cup_create'),
    path(
        'trophies_and_awards/<cup>-<pk>/',
        CupDetail.as_view(),
        name='cup_detail'
    ),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path(
        'players/<player>-<pk>/',
        PlayerDetail.as_view(),
        name='player_detail'
    ),
    path(
        'about-<continent>-<pk>/',
        ContinentAbout.as_view(),
        name='continent_about'
    ),

    path(
        '<continent>-<pk>/continent-title-update/',
        ContinentTitleUpdateView.as_view(),
        name='continent_title_update'
    ),
    path(
        '<continent>-<pk>/continent-info-update/',
        ContinentInfoUpdateView.as_view(),
        name='continent_info_update'
    ),
    path(
        '<continent>-<pk>/continent-main-update/',
        ContinentMainUpdateView.as_view(),
        name='continent_main_update'
    ),
    path(
        '<continent>/about-<country>-<pk>/',
        CountryAbout.as_view(),
        name='country_about'
    ),
    path(
        '<continent>/<country>/about-<league>-<pk>/',
        LeagueAbout.as_view(),
        name='league_about'
    ),

    path(
        'players/<player>-<pk>/player-title-update/',
        PlayerTitleUpdateView.as_view(),
        name='player_title_update'
    ),
    path(
        'players/<player>-<pk>/player-info-update/',
        PlayerInfoUpdateView.as_view(),
        name='player_info_update'
    ),
    path(
        'players/<player>-<pk>/player-main-update/',
        PlayerMainUpdateView.as_view(),
        name='player_main_update'
    ),
    path(
        'players/<player>-<pk>/player-club-update/',
        PlayerClubUpdateView.as_view(),
        name='player_club_update'
    ),
    path(
        'players/<player>-<pk>/player-trophy-update/',
        PlayerTrophyUpdateView.as_view(),
        name='player_trophy_update'
    ),

    path(
        'trophies_and_awards/<cup>-<pk>/cup-title-update/',
        CupTitleUpdateView.as_view(),
        name='cup_title_update'
    ),
    path(
        'trophies_and_awards/<cup>-<pk>/cup-info-update/',
        CupInfoUpdateView.as_view(),
        name='cup_info_update'
    ),
    path(
        'trophies_and_awards/<cup>-<pk>/cup-main-update/',
        CupMainUpdateView.as_view(),
        name='cup_main_update'
    ),
    path(
        'trophies_and_awards/<cup>-<pk>/cup-club-update/',
        CupClubUpdateView.as_view(),
        name='cup_club_update'
    ),
    path(
        'trophies_and_awards/<cup>-<pk>/cup-country-update/',
        CupCountryUpdateView.as_view(),
        name='cup_country_update'
    ),

    path(
        '<continent>/<country>-<pk>/country-title-update/',
        CountryTitleUpdateView.as_view(),
        name='country_title_update'
    ),
    path(
        '<continent>/<country>-<pk>/country-info-update/',
        CountryInfoUpdateView.as_view(),
        name='country_info_update'
    ),
    path(
        '<continent>/<country>-<pk>/country-main-update/',
        CountryMainUpdateView.as_view(),
        name='country_main_update'
    ),

    path(
        '<continent>/<country>/<league>-<pk>/league-title-update/',
        LeagueTitleUpdateView.as_view(),
        name='league_title_update'
    ),
    path(
        '<continent>/<country>/<league>-<pk>/league-info-update/',
        LeagueInfoUpdateView.as_view(),
        name='league_info_update'
    ),
    path(
        '<continent>/<country>/<league>-<pk>/league-main-update/',
        LeagueMainUpdateView.as_view(),
        name='league_main_update'
    ),
]

urlpatterns += [
    path('', HomePageView.as_view(), name='home_page'),
    path('<continent>/', ContinentDetail.as_view(), name='country_list'),
    path(
        '<continent>/<country>/',
        CountryDetail.as_view(),
        name='league_list'
    ),
    path(
        '<continent>/<country>/<league>/',
        LeagueDetail.as_view(),
        name='club_list'
    ),
    path(
        '<continent>/<country>/<league>/<club>-<pk>/',
        ClubDetail.as_view(),
        name='club_detail'
    ),

    path(
        '<continent>/<country>/<league>/<club>-<pk>/club-title-update/',
        ClubTitleUpdateView.as_view(),
        name='club_title_update'
    ),
    path(
        '<continent>/<country>/<league>/<club>-<pk>/club-info-update/',
        ClubInfoUpdateView.as_view(),
        name='club_info_update'
    ),
    path(
        '<continent>/<country>/<league>/<club>-<pk>/club-trophy-update/',
        ClubTrophyUpdateView.as_view(),
        name='club_trophy_update'
    ),
    path(
        '<continent>/<country>/<league>/<club>-<pk>/club-player-update/',
        ClubPlayerUpdateView.as_view(),
        name='club_player_update'
    ),
    path(
        '<continent>/<country>/<league>/<club>-<pk>/club-main-update/',
        ClubMainUpdateView.as_view(),
        name='club_main_update'
    ),

]
