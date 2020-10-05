from django.contrib import admin
from scraping.models import Job

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )
