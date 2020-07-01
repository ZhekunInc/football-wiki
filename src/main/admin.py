from django.contrib import admin
from main.models import Continent, Country, League, Club, Cup, Player, Kits, Fifa

try:
    from modeltranslation.admin import TranslationAdmin
except:
    from django.contrib.admin.options import ModelAdmin as TranslationAdmin


@admin.register(Continent)
class ContinentAdmin(TranslationAdmin):
    list_display = (
        'title', 'slug'
    )
    list_filter = ('is_published',)
    search_fields = ['title',]
    ordering = ('title',)
    prepopulated_fields = {'slug': ('title_en',)}

@admin.register(Country)
class CountryAdmin(TranslationAdmin):
    list_display = (
        'title', 'slug', 'continent'
    )
    list_filter = ('continent',)
    search_fields = ['title',]
    ordering = ('title',)
    prepopulated_fields = {'slug': ('title_en',)}

@admin.register(League)
class LeagueAdmin(TranslationAdmin):
    list_display = (
        'title', 'reputation', 'slug', 'country'
    )
    list_filter = ('country',)
    search_fields = ['title']
    ordering = ('title',)
    prepopulated_fields = {'slug': ('title_en',)}

class KitsInlinePost(admin.TabularInline):
    model = Kits
    extra = 0

@admin.register(Kits)
class KitsAdmin(TranslationAdmin):
    list_display = (
        'title',
    )

class FifaInlinePost(admin.TabularInline):
    model = Fifa
    extra = 0

@admin.register(Club)
class ClubAdmin(TranslationAdmin):
    list_display = (
        'title', 'slug', 'league'
    )
    list_filter = ('league',)
    search_fields = ('title',)
    ordering = ('title',)
    filter_horizontal = ('cups', 'famous_players',)
    inlines = [KitsInlinePost]
    prepopulated_fields = {'slug': ('title_en',)}

@admin.register(Cup)
class CupAdmin(TranslationAdmin):
    list_display = (
        'title', 'image', 'region'
    )
    list_filter = ('region',)
    search_fields = ['title',]
    ordering = ('title',)
    filter_horizontal = ('players', 'clubs', 'countrys')
    prepopulated_fields = {'slug': ('title_en',)}

@admin.register(Player)
class PlayerAdmin(TranslationAdmin):
    list_display = (
        'title', 'image', 'country'
    )
    list_filter = ('country',)
    search_fields = ['title',]
    ordering = ('title',)
    filter_horizontal = ('clubs', 'cups')
    inlines = [FifaInlinePost]
    prepopulated_fields = {'slug': ('title_en',)}
