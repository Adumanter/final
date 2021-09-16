from django.shortcuts import render


def index(request):
    return render(request, 'talking/index.html')
