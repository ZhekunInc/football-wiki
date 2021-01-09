from django.shortcuts import render
from django.views.generic import ListView
from .models import Country, Continent


class CountryList(ListView):

    template_name = "geo/geo.html"
    context_object_name = "countries"

    def get_queryset(self):
        return Country.objects.all().order_by("title")
