from modeltranslation.translator import translator, TranslationOptions

from .models import Country, Continent, League, Club


class ClubTranslation(TranslationOptions):
    fields = ('title', 'main_text', 'manager')

translator.register(Club, ClubTranslation)
