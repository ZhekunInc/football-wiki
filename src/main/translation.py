from modeltranslation.translator import translator, TranslationOptions

from .models import Country, Continent, League, Club, Cup, Player, Kits, Fifa

class ContinentTranslation(TranslationOptions):
    fields = ('title', 'main_text', 'located', 'region', 'president',)

translator.register(Continent, ContinentTranslation)

class CountryTranslation(TranslationOptions):
    fields = ('title', 'main_text', 'president',)

translator.register(Country, CountryTranslation)

class LeagueTranslation(TranslationOptions):
    fields = ('title', 'main_text', 'last')

translator.register(League, LeagueTranslation)

class ClubTranslation(TranslationOptions):
    fields = ('title', 'main_text', 'nickname', 'short_name', 'stadium', 'manager')

translator.register(Club, ClubTranslation)

class CupTranslation(TranslationOptions):
    fields = ('title', 'main_text')

translator.register(Cup, CupTranslation)

class PlayerTranslation(TranslationOptions):
    fields = ('title', 'main_text', 'nickname', 'positions')

translator.register(Player, PlayerTranslation)

class KitsTranslation(TranslationOptions):
    fields = ('title',)

translator.register(Kits, KitsTranslation)
