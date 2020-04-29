from modeltranslation.translator import translator, TranslationOptions

from .models import Country, Continent, League, Club, Cup, Player

class ContinentTranslation(TranslationOptions):
    fields = ('title',)

translator.register(Continent, ContinentTranslation)

class CountryTranslation(TranslationOptions):
    fields = ('title',)

translator.register(Country, CountryTranslation)

class LeagueTranslation(TranslationOptions):
    fields = ('title',)

translator.register(League, LeagueTranslation)

class ClubTranslation(TranslationOptions):
    fields = ('title', 'main_text', 'nickname', 'short_name', 'stadium', 'manager')

translator.register(Club, ClubTranslation)

class CupTranslation(TranslationOptions):
    fields = ('title',)

translator.register(Cup, CupTranslation)

class PlayerTranslation(TranslationOptions):
    fields = ('title',)

translator.register(Player, PlayerTranslation)
