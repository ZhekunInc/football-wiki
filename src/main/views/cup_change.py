from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.views.generic.base import View
from django.shortcuts import get_object_or_404
from datetime import datetime
from django.core.paginator import Paginator
from main.form.cup import CupCreateModelForm, CupTitleUpdateModelForm, CupInfoUpdateModelForm, CupClubUpdateModelForm, CupCountryUpdateModelForm, CupMainUpdateModelForm
from main.models import Country, Continent, League, Club, Player, Cup
from django.db.models import Q

class CupCreateView(CreateView):
    template_name = 'main/change-cup/cup_create.html'
    form_class = CupCreateModelForm
    queryset = Cup.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class CupTitleUpdateView(UpdateView):
    template_name = 'main/change-cup/cup_title_update.html'
    form_class = CupTitleUpdateModelForm
    queryset = Cup.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class CupInfoUpdateView(UpdateView):
    template_name = 'main/change-cup/cup_info_update.html'
    form_class = CupInfoUpdateModelForm
    queryset = Cup.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class CupClubUpdateView(UpdateView):
    template_name = 'main/change-cup/cup_club_update.html'
    form_class = CupClubUpdateModelForm
    queryset = Cup.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class CupCountryUpdateView(UpdateView):
    template_name = 'main/change-cup/cup_country_update.html'
    form_class = CupCountryUpdateModelForm
    queryset = Cup.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class CupMainUpdateView(UpdateView):
    template_name = 'main/change-cup/cup_main_update.html'
    form_class = CupMainUpdateModelForm
    queryset = Cup.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
