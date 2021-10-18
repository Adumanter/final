from django import forms
from django.contrib import admin
from .models import Article
from ckeditor_uploader.widgets import CKEditorUploadingWidget


class ArticleAdminForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Article
        fields = '__all__'


class ArticleAdmin(admin.ModelAdmin):
    form = ArticleAdminForm
    list_display = ('id', 'place', 'published', 'address')
    list_display_links = ('id', 'place')
    search_fields = ('place', 'address')


admin.site.register(Article, ArticleAdmin)