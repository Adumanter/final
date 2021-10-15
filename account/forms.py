from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class UserAuthForm(AuthenticationForm):
    username = forms.CharField(max_length=100, label='Имя пользователя', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(max_length=100, label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=100, label='Имя пользователя', help_text='Не более 100 символов', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(max_length=100, label='Пароль', help_text='Не более 100 символов', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(max_length=100, label='Подтверждение пароля', help_text='Не более 100 символов', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Почта пользователя', widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
