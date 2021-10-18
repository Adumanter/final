from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm
from django.core.paginator import Paginator


def index(request):

    articles = Article.objects.all()
    paginator = Paginator(articles, 1)  # группировка стaтей по три
    page_number = request.GET.get('page')  # Извлекает страницы
    page_object = paginator.get_page(page_number)
    return render(request, 'publications/index.html', context={
        'articles': articles,
        'page_object': page_object
    })


def create(request):

    data = dict()
    if request.method == 'GET':
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # Блокировка доступа через адресную строку!!!!!!!!!
        if request.user.username == 'Adumanter007':
            # Создаем экземпляр формы и передаеи его в шаблон:
            data['form'] = ArticleForm()
            return render(request, 'publications/create_craft.html', context=data)
        else:
            return render(request, 'layouts/page403.html')
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    elif request.method == 'POST':
        # Обработка данных форм добавления новости
        filled_form = ArticleForm(request.POST, request.FILES)
        filled_form.save()
        return redirect('/publications')
