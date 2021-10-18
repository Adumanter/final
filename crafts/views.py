from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from .forms import ArticleForm
from .models import Craft


def index(request):

    crafts = Craft.objects.all()
    paginator = Paginator(crafts, 1)  # группировка ститей по три
    page_number = request.GET.get('page')  # Извлекает страницы
    page_object = paginator.get_page(page_number)

    return render(request, 'crafts/index.html', context={
        'crafts': crafts,
        'page_object': page_object
    })


def create(request):
    data = dict()
    if request.method == 'GET':
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # Блокировка доступа через адресную строку!!!!!!!!!
        if request.user.username:
            # Создаем экземпляр формы и передаеи его в шаблон:
            data['form'] = ArticleForm()
            return render(request, 'crafts/create_craft.html', context=data)
        else:
            return render(request, 'layouts/page403.html')
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    elif request.method == 'POST':
        # Обработка данных форм добавления новости
        filled_form = ArticleForm(request.POST, request.FILES)
        filled_form.save()
        return redirect('/crafts')