from django import template
from main.models import Continent, RatingAssociation

register = template.Library()

@register.inclusion_tag('tag-pages/continent-list.html')
def continent_on_home():
    return {
        'continent': Continent.objects.all().filter(is_published=True).order_by("title")
    }

@register.inclusion_tag('tag-pages/rating-list.html')
def rating_list_club():
    return {
        'rating_continent': Continent.objects.all().filter(is_published=True).order_by("title")
    }

@register.inclusion_tag('tag-pages/rating-list-association.html')
def rating_list_association():
    return {
        'rating_continent': RatingAssociation.objects.all().order_by("continent__title")
    }
