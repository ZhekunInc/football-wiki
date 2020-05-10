from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.views.generic.base import View
from django.shortcuts import get_object_or_404
from datetime import datetime
from django.core.paginator import Paginator
from main.form.club import ClubCreateModelForm, ClubTitleUpdateModelForm, ClubInfoUpdateModelForm, ClubTrophyUpdateModelForm, ClubPlayerUpdateModelForm, ClubMainUpdateModelForm
from main.models import Country, Continent, League, Club, Player, Cup
from django.db.models import Q

class ClubCreateView(CreateView):
    template_name = 'main/change-club/club_create.html'
    form_class = ClubCreateModelForm
    queryset = Club.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class ClubTitleUpdateView(UpdateView):
    template_name = 'main/change-club/club_title_update.html'
    form_class = ClubTitleUpdateModelForm
    queryset = Club.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class ClubInfoUpdateView(UpdateView):
    template_name = 'main/change-club/club_info_update.html'
    form_class = ClubInfoUpdateModelForm
    queryset = Club.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class ClubTrophyUpdateView(UpdateView):
    template_name = 'main/change-club/club_trophy_update.html'
    form_class = ClubTrophyUpdateModelForm
    queryset = Club.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class ClubPlayerUpdateView(UpdateView):
    template_name = 'main/change-club/club_player_update.html'
    form_class = ClubPlayerUpdateModelForm
    queryset = Club.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class ClubMainUpdateView(UpdateView):
    template_name = 'main/change-club/club_main_update.html'
    form_class = ClubMainUpdateModelForm
    queryset = Club.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)