from django import forms
from .models import Craft


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Craft
        fields = ('title', 'content', 'image', 'ref')  # Поля, которрые я хочу включить в форму

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'ref': forms.URLInput(attrs={'class': 'form-control'})
        }
