from django import forms
from .models import Craft


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Craft
        fields = ('title', 'content', 'image')  # Поля, которрые я хочу включить в форму
