from django.core.paginator import Paginator
from django.shortcuts import render
from .models import New


def index(request):

    news = New.objects.all()
    paginator = Paginator(news, 1)  # группировка ститей по три
    page_number = request.GET.get('page')  # Извлекает страницы
    page_object = paginator.get_page(page_number)

    return render(request, 'fish_news/index.html', context={
        'news': news,
        'page_object': page_object
    })

