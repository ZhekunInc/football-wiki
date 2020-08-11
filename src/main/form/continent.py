from django import forms

from main.models import Continent

class ContinentTitleUpdateModelForm(forms.ModelForm):
    class Meta:
        model = Continent
        fields = [
            'title',
            'slug',
        ]

class ContinentInfoUpdateModelForm(forms.ModelForm):
    class Meta:
        model = Continent
        fields = [
            'image',
            'founded',
            'located',
            'region',
            'associations',
            'president',
            'website',
        ]

class ContinentMainUpdateModelForm(forms.ModelForm):
    class Meta:
        model = Continent
        fields = [
            'main_text',
        ]
