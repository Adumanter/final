from django import forms
from .models import Contact


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'telephone', 'message')  # Поля, которрые я хочу включить в форму
