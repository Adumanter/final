from django.contrib import admin
from .models import Craft


class CraftAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'published', 'content')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')


admin.site.register(Craft, CraftAdmin)
