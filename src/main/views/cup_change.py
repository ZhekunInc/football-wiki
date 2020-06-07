from django.views.generic import CreateView, UpdateView
from main.form.cup import CupCreateModelForm, CupTitleUpdateModelForm
from main.form.cup import CupInfoUpdateModelForm, CupClubUpdateModelForm
from main.form.cup import CupCountryUpdateModelForm, CupMainUpdateModelForm
from main.models import Cup

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
