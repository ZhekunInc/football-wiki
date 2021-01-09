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
from django.contrib.sitemaps import views
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns

from main.sitemaps import ContinentSitemap, LeagueSitemap, CountrySitemap, ClubSitemap, CupSitemap, PlayerSitemap

urlpatterns = [
    path('i18/', include('django.conf.urls.i18n')),
]

sm_info = {
    'continents': ContinentSitemap(),
    'countrys': CountrySitemap(),
    'leagues': LeagueSitemap(),
    'clubs': ClubSitemap(),
    'cups': CupSitemap(),
    'players': PlayerSitemap(),
}

urlpatterns += i18n_patterns(
    path('rosetta/', include('rosetta.urls')),
    path('accounts/', include('allauth.urls')),
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('geography/', include('geo.urls')),
    path('sitemaps.xml', views.sitemap, {'sitemaps': sm_info}),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
