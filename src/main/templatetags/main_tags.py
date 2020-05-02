from django import template
from main.models import Continent, Country

register = template.Library()

@register.inclusion_tag('tag-pages/continent-list.html')
def continent_on_home():
    return {
        'continent': Continent.objects.all().filter(is_published=True).order_by("title")
    }
