"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns

from main.sitemaps import ContinentSitemap, LeagueSitemap, CountrySitemap, ClubSitemap, CupSitemap, PlayerSitemap

continents = {
    'continents': ContinentSitemap,
}

countrys = {
    'countrys': CountrySitemap,
}

leagues = {
    'leagues': LeagueSitemap,
}

clubs = {
    'clubs': ClubSitemap,
}

cups = {
    'cups': CupSitemap,
}

players = {
    'players': PlayerSitemap,
}

urlpatterns = [
    path('i18/', include('django.conf.urls.i18n')),
    
]

urlpatterns += i18n_patterns (
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('continent-sitemaps.xml', sitemap, {'sitemaps': continents}),
    path('country-sitemaps.xml', sitemap, {'sitemaps': countrys}),
    path('league-sitemaps.xml', sitemap, {'sitemaps': leagues}),
    path('club-sitemaps.xml', sitemap, {'sitemaps': clubs}),
    path('cup-sitemaps.xml', sitemap, {'sitemaps': cups}),
    path('player-sitemaps.xml', sitemap, {'sitemaps': players}),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
