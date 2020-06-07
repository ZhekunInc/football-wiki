from django import forms

from main.models import Country

class CountryCreateModelForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = [
            'title_uk',
            'title_en',
            'title_ru',
            'slug',
            'continent',
            'main_text_uk',
            'main_text_en',
            'main_text_ru',
            'picture',
            'founded',
            'fifa',
            'uefa',
            'president',
            'website',
            'wc',
            'cl',
            'gb',
        ]

class CountryTitleUpdateModelForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = [
            'title_uk',
            'title_en',
            'title_ru',
            'slug',
        ]

class CountryInfoUpdateModelForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = [
            'continent',
            'picture',
            'founded',
            'fifa',
            'uefa',
            'president',
            'website',
            'wc',
            'cl',
            'gb',
        ]

class CountryMainUpdateModelForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = [
            'main_text_uk',
            'main_text_en',
            'main_text_ru',
        ]
