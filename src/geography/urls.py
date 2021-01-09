from django.urls import path
from .views import CountryList

urlpatterns = [
    path(
        'geography/learn/country/',
        CountryList.as_view(),
        name='geography'
    ),
]