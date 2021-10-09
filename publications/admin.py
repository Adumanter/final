from django.contrib import admin
from .models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'place', 'published', 'address')
    list_display_links = ('id', 'place')
    search_fields = ('place', 'address')


admin.site.register(Article, ArticleAdmin)
