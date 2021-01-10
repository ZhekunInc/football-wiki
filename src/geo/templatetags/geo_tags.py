from django import template
from geo.models import Continent, Country

register = template.Library()


@register.inclusion_tag('geo-tag-pages/continent-list.html')
def geo_continents():
    return {
        'continents': Continent.objects.all().filter(
            is_published=True
        ).order_by("title")
    }


@register.simple_tag
def get_europe_country():
    continent_country = Country.objects.all(
    ).filter(
        continent__title='Європа'
    ).order_by('title')
    return continent_country
