from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Turnir


def index(request):
    turnirs = Turnir.objects.all()
    paginator = Paginator(turnirs, 1)
    page_number = request.GET.get('page')  # Извлекает страницы
    page_object = paginator.get_page(page_number)

    return render(request, 'turnir/index.html', context={
        'turnirs': turnirs,
        'page_object': page_object
    })