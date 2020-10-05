from django.contrib import admin
from main.models import Continent, Country, League, Club, Cup, Player, Kits, Fifa, PlayerClub, PlayerCup, CupClub, CupCountry, CountryPlayer, RatingAssociation, Association

try:
    from modeltranslation.admin import TabbedDjangoJqueryTranslationAdmin as TranslationAdmin, TranslationStackedInline
except:
    from django.contrib.admin.options import ModelAdmin as TranslationAdmin


class CupCountryInlinePost(admin.TabularInline):
    model = CupCountry
    extra = 0


class CountryPlayerInlinePost(admin.TabularInline):
    model = CountryPlayer
    extra = 0


@admin.register(Continent)
class ContinentAdmin(TranslationAdmin):
    list_display = (
        'title', 'slug'
    )
    list_filter = ('is_published',)
    search_fields = ['title',]
    ordering = ('title',)
    prepopulated_fields = {'slug': ('title_en',)}

    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

@admin.register(Country)
class CountryAdmin(TranslationAdmin):
    list_display = (
        'title', 'slug', 'continent'
    )
    list_filter = ('continent',)
    search_fields = ['title',]
    ordering = ('title',)
    prepopulated_fields = {'slug': ('title_en',)}
    inlines = [CupCountryInlinePost, CountryPlayerInlinePost]

    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

@admin.register(League)
class LeagueAdmin(TranslationAdmin):
    list_display = (
        'title', 'reputation', 'slug', 'country'
    )
    list_filter = ('country',)
    search_fields = ['title']
    ordering = ('title',)
    prepopulated_fields = {'slug': ('title_en',)}

    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

class KitsInlinePost(admin.TabularInline, TranslationStackedInline):
    model = Kits
    extra = 0

    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

class FifaInlinePost(admin.TabularInline):
    model = Fifa
    extra = 0


class PlayerClubInlinePost(admin.TabularInline):
    model = PlayerClub
    extra = 0

class PlayerCupInlinePost(admin.TabularInline):
    model = PlayerCup
    extra = 0

class CupClubInlinePost(admin.TabularInline):
    model = CupClub
    extra = 0

class AssociationInlinePost(admin.TabularInline):
    model = Association
    extra = 0

@admin.register(Club)
class ClubAdmin(TranslationAdmin):
    list_display = (
        'title', 'slug', 'league'
    )
    list_filter = ('league',)
    search_fields = ('title',)
    ordering = ('title',)
    inlines = [KitsInlinePost, PlayerClubInlinePost, CupClubInlinePost]
    prepopulated_fields = {'slug': ('title_en',)}

    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

@admin.register(Cup)
class CupAdmin(TranslationAdmin):
    list_display = (
        'title', 'image', 'region'
    )
    list_filter = ('region',)
    search_fields = ['title']
    ordering = ('title',)
    prepopulated_fields = {'slug': ('title_en',)}
    inlines = [PlayerCupInlinePost, CupClubInlinePost, CupCountryInlinePost]

    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

@admin.register(Player)
class PlayerAdmin(TranslationAdmin):
    list_display = (
        'title', 'image', 'country'
    )
    list_filter = ('country',)
    search_fields = ['title', ]
    ordering = ('title',)
    inlines = [FifaInlinePost, PlayerClubInlinePost, PlayerCupInlinePost]
    prepopulated_fields = {'slug': ('title_en',)}

    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

@admin.register(RatingAssociation)
class RatingAssociationAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'continent'
    )
    inlines = [AssociationInlinePost]

@admin.register(Association)
class AssociationAdmin(admin.ModelAdmin):
    list_display = (
        'id',
    )