from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('place', 'content', 'image', 'url', 'address')  # Поля, которрые я хочу включить в форму
