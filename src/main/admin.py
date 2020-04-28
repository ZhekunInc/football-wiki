from django.contrib import admin
from main.models import Continent, Country, League, Club, Cup, Player

try:
    from modeltranslation.admin import TranslationAdmin
except:
    from django.contrib.admin.options import ModelAdmin as TranslationAdmin

from tof.admin import TofAdmin


@admin.register(Continent)
class ContinentAdmin(TofAdmin):
    list_display = (
        'title', 'slug'
    )

    prepopulated_fields = {'slug': ('title',)}

@admin.register(Country)
class CountryAdmin(TofAdmin):
    list_display = (
        'title', 'slug', 'continent'
    )

    prepopulated_fields = {'slug': ('title',)}

@admin.register(League)
class LeagueAdmin(TofAdmin):
    list_display = (
        'title', 'reputation', 'slug', 'country'
    )

    prepopulated_fields = {'slug': ('title',)}

@admin.register(Club)
class ClubAdmin(TofAdmin):
    list_display = (
        'id', 'title', 'slug', 'league'
    )

    filter_horizontal = ('cups', 'famous_players',)


@admin.register(Cup)
class CupAdmin(TofAdmin):
    list_display = (
        'title', 'image'
    )

@admin.register(Player)
class PlayerAdmin(TofAdmin):
    list_display = (
        'title', 'image'
    )

