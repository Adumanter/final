from django.contrib import admin
from .models import Turnir


class TurnirAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'place', 'published')
    list_display_links = ('id', 'place')
    search_fields = ('place', 'title')


admin.site.register(Turnir, TurnirAdmin)
