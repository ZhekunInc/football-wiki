from django.contrib import admin
from main.models import Continent, Country, League, Club, Cup, Player, Kits

try:
    from modeltranslation.admin import TranslationAdmin
except:
    from django.contrib.admin.options import ModelAdmin as TranslationAdmin


@admin.register(Continent)
class ContinentAdmin(TranslationAdmin):
    list_display = (
        'title', 'slug'
    )

    prepopulated_fields = {'slug': ('title_en',)}

@admin.register(Country)
class CountryAdmin(TranslationAdmin):
    list_display = (
        'title', 'slug', 'continent'
    )

    prepopulated_fields = {'slug': ('title_en',)}

@admin.register(League)
class LeagueAdmin(TranslationAdmin):
    list_display = (
        'title', 'reputation', 'slug', 'country'
    )

    prepopulated_fields = {'slug': ('title_en',)}

class KitsInlinePost(admin.TabularInline):
    model=Kits
    extra=0 

@admin.register(Kits)
class KitsAdmin(TranslationAdmin):
    list_display = (
        'title',
    )

@admin.register(Club)
class ClubAdmin(TranslationAdmin):
    list_display = (
        'title', 'slug', 'league'
    )

    filter_horizontal = ('cups', 'famous_players',)
    inlines=[KitsInlinePost]
    prepopulated_fields = {'slug': ('title_en',)}

@admin.register(Cup)
class CupAdmin(TranslationAdmin):
    list_display = (
        'title', 'image'
    )

@admin.register(Player)
class PlayerAdmin(TranslationAdmin):
    list_display = (
        'title', 'image'
    )
