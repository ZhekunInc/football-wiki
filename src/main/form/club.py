from django import forms

from main.models import Club

class ClubCreateModelForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = [
            'title',
            'slug',
            'league',
            'main_text',
            'picture',
            'color1',
            'color2',
            'nickname',
            'short_name',
            'founded',
            'stadium',
            'manager',
            'website',
            'place',
            'points',
            'cups',
            'famous_players',
            'cl',
            'gb'
        ]

class ClubTitleUpdateModelForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = [
            'title',
            'slug',
        ]

class ClubInfoUpdateModelForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = [
            'league',
            'picture',
            'color1',
            'color2',
            'nickname',
            'short_name',
            'founded',
            'stadium',
            'manager',
            'place',
            'points',
            'website',
        ]

class ClubTrophyUpdateModelForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = [
            'cups',
            'cl',
            'gb'
        ]

class ClubPlayerUpdateModelForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = [
            'famous_players',
        ]

class ClubMainUpdateModelForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = [
            'main_text',
        ]
