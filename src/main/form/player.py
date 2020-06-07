from django import forms

from main.models import Player

class PlayerCreateModelForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = [
            'title_uk',
            'title_en',
            'title_ru',
            'slug',
            'image',
            'main_text_uk',
            'main_text_en',
            'main_text_ru',
            'country',
            'clubs',
            'cups',
            'nickname_uk',
            'nickname_en',
            'nickname_ru',
            'date_of_birth',
            'height',
            'positions',
            'wc',
            'cl',
            'gb',
        ]

class PlayerTitleUpdateModelForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = [
            'title_uk',
            'title_en',
            'title_ru',
            'slug',
        ]

class PlayerInfoUpdateModelForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = [
            'image',
            'nickname_uk',
            'nickname_en',
            'nickname_ru',
            'country',
            'date_of_birth',
            'height',
            'positions',
        ]

class PlayerTrophyUpdateModelForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = [
            'cups',
            'wc',
            'cl',
            'gb',
        ]

class PlayerClubUpdateModelForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = [
            'clubs',
        ]

class PlayerMainUpdateModelForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = [
            'main_text_uk',
            'main_text_en',
            'main_text_ru',
        ]
