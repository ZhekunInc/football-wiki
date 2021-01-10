from django.urls import path
from .views import CountryList

urlpatterns = [
    path(
        'geo/learn/country/',
        CountryList.as_view(),
        name='geo'
    ),
]