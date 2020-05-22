from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.views.generic.base import View
from django.shortcuts import get_object_or_404
from datetime import datetime
from django.core.paginator import Paginator
from main.form.player import PlayerCreateModelForm, PlayerTitleUpdateModelForm, PlayerInfoUpdateModelForm, PlayerTrophyUpdateModelForm, PlayerClubUpdateModelForm, PlayerMainUpdateModelForm
from main.models import Country, Continent, League, Club, Player, Cup
from django.db.models import Q

class PlayerCreateView(CreateView):
    template_name = 'main/change-player/player_create.html'
    form_class = PlayerCreateModelForm
    queryset = Player.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class PlayerTitleUpdateView(UpdateView):
    template_name = 'main/change-player/player_title_update.html'
    form_class = PlayerTitleUpdateModelForm
    queryset = Player.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class PlayerInfoUpdateView(UpdateView):
    template_name = 'main/change-player/player_info_update.html'
    form_class = PlayerInfoUpdateModelForm
    queryset = Player.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class PlayerTrophyUpdateView(UpdateView):
    template_name = 'main/change-player/player_trophy_update.html'
    form_class = PlayerTrophyUpdateModelForm
    queryset = Player.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class PlayerClubUpdateView(UpdateView):
    template_name = 'main/change-player/player_club_update.html'
    form_class = PlayerClubUpdateModelForm
    queryset = Player.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class PlayerMainUpdateView(UpdateView):
    template_name = 'main/change-player/player_main_update.html'
    form_class = PlayerMainUpdateModelForm
    queryset = Player.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)