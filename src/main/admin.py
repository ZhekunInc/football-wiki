from django.contrib import admin
from main.models import Continent, Country, League, Club, Cup, Player

try:
    from modeltranslation.admin import TranslationAdmin
except:
    from django.contrib.admin.options import ModelAdmin as TranslationAdmin




@admin.register(Continent)
class ContinentAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'slug'
    )

    prepopulated_fields = {'slug': ('title',)}

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'slug', 'continent'
    )

    prepopulated_fields = {'slug': ('title',)}

@admin.register(League)
class LeagueAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'reputation', 'slug', 'country'
    )

    prepopulated_fields = {'slug': ('title',)}

@admin.register(Club)
class ClubAdmin(TranslationAdmin):
    list_display = (
        'id', 'title', 'slug', 'league'
    )

    filter_horizontal = ('cups', 'famous_players',)


@admin.register(Cup)
class CupAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'image'
    )

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'image'
    )

