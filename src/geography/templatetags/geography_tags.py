from django import template
from geography.models import Continent, Country

register = template.Library()


@register.inclusion_tag('geography-tag-pages/continent-list.html')
def geography_continents():
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
