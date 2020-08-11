from django import forms

from main.models import League

class LeagueCreateModelForm(forms.ModelForm):
    class Meta:
        model = League
        fields = [
            'title',
            'slug',
            'country',
            'main_text',
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
            'title',
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
            'main_text',
        ]
