from django.views.generic import CreateView, UpdateView
from main.form.club import ClubCreateModelForm, ClubTitleUpdateModelForm
from main.form.club import ClubInfoUpdateModelForm, ClubTrophyUpdateModelForm
from main.form.club import ClubPlayerUpdateModelForm, ClubMainUpdateModelForm
from main.models import Club

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
