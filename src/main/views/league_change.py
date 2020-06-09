from django.views.generic import UpdateView, CreateView
from main.form.league import LeagueTitleUpdateModelForm
from main.form.league import LeagueCreateModelForm
from main.form.league import LeagueInfoUpdateModelForm
from main.form.league import LeagueMainUpdateModelForm
from main.models import League

class LeagueCreateView(CreateView):
    template_name = 'main/change-league/league_create.html'
    form_class = LeagueCreateModelForm
    queryset = League.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class LeagueTitleUpdateView(UpdateView):
    template_name = 'main/change-league/league_title_update.html'
    form_class = LeagueTitleUpdateModelForm
    queryset = League.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class LeagueInfoUpdateView(UpdateView):
    template_name = 'main/change-league/league_info_update.html'
    form_class = LeagueInfoUpdateModelForm
    queryset = League.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class LeagueMainUpdateView(UpdateView):
    template_name = 'main/change-league/league_main_update.html'
    form_class = LeagueMainUpdateModelForm
    queryset = League.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
