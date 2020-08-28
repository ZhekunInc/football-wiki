from django import forms

from main.models import Cup

class CupCreateModelForm(forms.ModelForm):
    class Meta:
        model = Cup
        fields = [
            'title',
            'slug',
            'image',
            'main_text',
            'founded',
            'region',
            'website',
        ]

class CupTitleUpdateModelForm(forms.ModelForm):
    class Meta:
        model = Cup
        fields = [
            'title',
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
        ]

class CupCountryUpdateModelForm(forms.ModelForm):
    class Meta:
        model = Cup
        fields = [
        ]

class CupMainUpdateModelForm(forms.ModelForm):
    class Meta:
        model = Cup
        fields = [
            'main_text',
        ]
