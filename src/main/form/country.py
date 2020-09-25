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
        ]

class CountryMainUpdateModelForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = [
            'main_text',
        ]
