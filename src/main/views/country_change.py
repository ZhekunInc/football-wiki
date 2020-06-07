from django.views.generic import CreateView, UpdateView
from main.form.country import CountryCreateModelForm
from main.form.country import CountryTitleUpdateModelForm
from main.form.country import CountryInfoUpdateModelForm
from main.form.country import CountryMainUpdateModelForm
from main.models import Country

class CountryCreateView(CreateView):
    template_name = 'main/change-country/country_create.html'
    form_class = CountryCreateModelForm
    queryset = Country.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class CountryTitleUpdateView(UpdateView):
    template_name = 'main/change-country/country_title_update.html'
    form_class = CountryTitleUpdateModelForm
    queryset = Country.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class CountryInfoUpdateView(UpdateView):
    template_name = 'main/change-country/country_info_update.html'
    form_class = CountryInfoUpdateModelForm
    queryset = Country.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class CountryMainUpdateView(UpdateView):
    template_name = 'main/change-country/country_main_update.html'
    form_class = CountryMainUpdateModelForm
    queryset = Country.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
