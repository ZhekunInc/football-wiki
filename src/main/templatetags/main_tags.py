from django import template
from main.models import Continent, RatingAssociation, RatingTeam, RatingCountry, FifaCountry

register = template.Library()

@register.inclusion_tag('tag-pages/continent-list.html')
def continent_on_home():
    return {
        'continent': Continent.objects.all().filter(is_published=True).order_by("title")
    }

@register.inclusion_tag('tag-pages/rating-list-club.html')
def rating_list_club():
    return {
        'rating_club': RatingTeam.objects.all().order_by("continent__title")
    }

@register.inclusion_tag('tag-pages/rating-list-association.html')
def rating_list_association():
    return {
        'rating_ass': RatingAssociation.objects.all().order_by("continent__title")
    }

@register.inclusion_tag('tag-pages/rating-list-country.html')
def rating_list_country():
    return {
        'rating_country': RatingCountry.objects.all().order_by("continent__title")
    }

@register.simple_tag
def get_uefa_country():
    continent_country = FifaCountry.objects.all(
    ).filter(
        country__continent__slug='uefa'
    ).order_by('-points')
    return continent_country

@register.simple_tag
def get_conmebol_country():
    continent_country = FifaCountry.objects.all(
    ).filter(
        country__continent__slug='conmebol'
    ).order_by('-points')
    return continent_country

@register.simple_tag
def get_concacaf_country():
    continent_country = FifaCountry.objects.all(
    ).filter(
        country__continent__slug='concacaf'
    ).order_by('-points')
    return continent_country

@register.simple_tag
def get_caf_country():
    continent_country = FifaCountry.objects.all(
    ).filter(
        country__continent__slug='caf'
    ).order_by('-points')
    return continent_country

@register.simple_tag
def get_afc_country():
    continent_country = FifaCountry.objects.all(
    ).filter(
        country__continent__slug='afc'
    ).order_by('-points')
    return continent_country

@register.simple_tag
def get_ofc_country():
    continent_country = FifaCountry.objects.all(
    ).filter(
        country__continent__slug='ofc'
    ).order_by('-points')
    return continent_country
