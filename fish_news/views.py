from django.core.paginator import Paginator
from django.shortcuts import render
from .models import New


def index(request):

    crafts = New.objects.all()
    paginator = Paginator(crafts, 1)  # группировка ститей по три
    page_number = request.GET.get('page')  # Извлекает страницы
    page_object = paginator.get_page(page_number)

    return render(request, 'crafts/index.html', context={
        'crafts': crafts,
        'page_object': page_object
    })

