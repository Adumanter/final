from django.contrib import admin
from .views import New


class NewAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'published', 'content')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')


admin.site.register(New, NewAdmin)
# Register your models here.
