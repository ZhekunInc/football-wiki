from django import forms

from main.models import Cup

class CupCreateModelForm(forms.ModelForm):
    class Meta:
        model = Cup
        fields = [
            'title_uk',
            'title_en',
            'title_ru',
            'slug',
            'image',
            'main_text_uk',
            'main_text_en',
            'main_text_ru',
            'clubs',
            'countrys',
            'founded',
            'region',
            'website',
        ]

class CupTitleUpdateModelForm(forms.ModelForm):
    class Meta:
        model = Cup
        fields = [
            'title_uk',
            'title_en',
            'title_ru',
            'slug',
        ]

class CupInfoUpdateModelForm(forms.ModelForm):
    class Meta:
        model = Cup
        fields = [
            'image',
            'founded',
            'region',
            'website',
        ]

class CupClubUpdateModelForm(forms.ModelForm):
    class Meta:
        model = Cup
        fields = [
            'clubs',
        ]

class CupCountryUpdateModelForm(forms.ModelForm):
    class Meta:
        model = Cup
        fields = [
            'countrys',
        ]

class CupMainUpdateModelForm(forms.ModelForm):
    class Meta:
        model = Cup
        fields = [
            'main_text_uk',
            'main_text_en',
            'main_text_ru',
        ]