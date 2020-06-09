from django import forms

from main.models import League

class LeagueCreateModelForm(forms.ModelForm):
    class Meta:
        model = League
        fields = [
            'title_uk',
            'title_en',
            'title_ru',
            'slug',
            'country',
            'main_text_uk',
            'main_text_en',
            'main_text_ru',
            'picture',
            'founded',
            'count_team',
            'reputation',
            'last',
            'website',
        ]

class LeagueTitleUpdateModelForm(forms.ModelForm):
    class Meta:
        model = League
        fields = [
            'title_uk',
            'title_en',
            'title_ru',
            'slug',
        ]

class LeagueInfoUpdateModelForm(forms.ModelForm):
    class Meta:
        model = League
        fields = [
            'country',
            'picture',
            'founded',
            'count_team',
            'reputation',
            'last',
            'website',
        ]

class LeagueMainUpdateModelForm(forms.ModelForm):
    class Meta:
        model = League
        fields = [
            'main_text_uk',
            'main_text_en',
            'main_text_ru',
        ]
