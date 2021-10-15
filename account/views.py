from django.contrib.auth import login, logout
from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import UserRegisterForm, UserAuthForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid:
            user = form.save()
            login(request, user)
            messages.success(request, 'Вы успешно зарегестрировались!')
            return redirect('home')
        else:
            messages.error(request, 'Произошла ошибка!')
    else:
        form = UserRegisterForm()
        return render(request, 'account/sign_up.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserAuthForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserAuthForm()
        return render(request, 'account/sign_in.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('login')

