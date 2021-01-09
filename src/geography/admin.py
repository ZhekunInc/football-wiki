from django.contrib import admin
from .models import Continent, Country


@admin.register(Continent)
class ContinentAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'slug'
    )
    search_fields = ['title', ]
    ordering = ('title',)
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'capital', 'continent', 'flag'
    )
    list_filter = ('continent',)
    search_fields = ['title', ]
    ordering = ('title',)
    prepopulated_fields = {'slug': ('title',)}
