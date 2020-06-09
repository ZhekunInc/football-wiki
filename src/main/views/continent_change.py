from django.views.generic import UpdateView
from main.form.continent import ContinentTitleUpdateModelForm
from main.form.continent import ContinentInfoUpdateModelForm
from main.form.continent import ContinentMainUpdateModelForm
from main.models import Continent

class ContinentTitleUpdateView(UpdateView):
    template_name = 'main/change-continent/continent_title_update.html'
    form_class = ContinentTitleUpdateModelForm
    queryset = Continent.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class ContinentInfoUpdateView(UpdateView):
    template_name = 'main/change-continent/continent_info_update.html'
    form_class = ContinentInfoUpdateModelForm
    queryset = Continent.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class ContinentMainUpdateView(UpdateView):
    template_name = 'main/change-continent/continent_main_update.html'
    form_class = ContinentMainUpdateModelForm
    queryset = Continent.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
