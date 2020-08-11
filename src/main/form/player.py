from django import forms

from main.models import Player

class PlayerCreateModelForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = [
            'title',
            'slug',
            'image',
            'main_text',
            'country',
            'clubs',
            'cups',
            'nickname',
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
            'title',
            'slug',
        ]

class PlayerInfoUpdateModelForm(forms.ModelForm):
    class Meta:
        model = Player
        fields = [
            'image',
            'nickname',
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
            'main_text',
        ]
