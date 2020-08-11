from django import forms

from main.models import Country

class CountryCreateModelForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = [
            'title',
            'slug',
            'continent',
            'main_text',
            'picture',
            'flag',
            'founded',
            'fifa',
            'uefa',
            'president',
            'website',
            'place',
            'points',
            'place_ass',
            'points_ass',
            'cl_teams',
            'el_teams',
            'wc',
            'cl',
            'gb',
        ]

class CountryTitleUpdateModelForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = [
            'title',
            'slug',
        ]

class CountryInfoUpdateModelForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = [
            'continent',
            'picture',
            'flag',
            'founded',
            'fifa',
            'uefa',
            'president',
            'website',
            'place',
            'points',
            'place_ass',
            'points_ass',
            'cl_teams',
            'el_teams',
            'wc',
            'cl',
            'gb',
        ]

class CountryMainUpdateModelForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = [
            'main_text',
        ]
