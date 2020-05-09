from django import forms

from main.models import Club

class ClubCreateModelForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = [
            'title_uk',
            'title_en',
            'title_ru',
            'slug',
            'league',
            'main_text_uk',
            'main_text_en',
            'main_text_ru',
            'picture',
            'nickname_uk',
            'nickname_en',
            'nickname_ru',
            'short_name_uk',
            'short_name_en',
            'short_name_ru',
            'founded',
            'stadium_uk',
            'stadium_en',
            'stadium_ru',
            'manager_uk',
            'manager_en',
            'manager_ru',
            'website',
            'cups',
            'famous_players',
            'cl',
            'gb'
        ]

class ClubTitleUpdateModelForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = [
            'title_uk',
            'title_en',
            'title_ru',
            'slug',
        ]

class ClubInfoUpdateModelForm(forms.ModelForm):
    class Meta:
        model = Club
        fields = [
            'league',
            'picture',
            'nickname_uk',
            'nickname_en',
            'nickname_ru',
            'short_name_uk',
            'short_name_en',
            'short_name_ru',
            'founded',
            'stadium_uk',
            'stadium_en',
            'stadium_ru',
            'manager_uk',
            'manager_en',
            'manager_ru',
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
