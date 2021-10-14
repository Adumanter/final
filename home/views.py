from django.shortcuts import render, redirect
from django.views.generic import DetailView

from publications.models import Article
from turnir.models import Turnir
from crafts.models import Craft
from fish_news.models import New
from .forms import ArticleForm
from telebot.send_message import send_telegram
from .models import Contact


def index(request):
    news = New.objects.all()
    data = {'news': news}
    return render(request, 'home/index1.html', context=data)


def get_article(request, aid):
    article = Article.objects.filter(pk=aid)
    return render(request, 'publications/article.html', {'articles': article})


def get_turnir(request, pk):
    turnir = Turnir.objects.filter(pk=pk)
    return render(request, 'turnir/turnir_single.html', {'turnirs': turnir})


def get_craft(request, cid):
    craft = Craft.objects.filter(pk=cid)
    return render(request, 'crafts/single_craft.html', {'crafts': craft})


def get_news(request, nid):
    new = New.objects.filter(id=nid)
    return render(request, 'fish_news/single_fish_news.html', {'news': new})


def contact(request):
    data = dict()
    if request.method == 'GET':
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        # Блокировка доступа через адресную строку!!!!!!!!!
        if request.user.username is not None:
            # Создаем экземпляр формы и передаеи его в шаблон:
            data['form'] = ArticleForm()
            return render(request, 'home/contact.html', context=data)
        else:
            return render(request, 'layouts/page403.html')
        # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    elif request.method == 'POST':
        # Обработка данных форм добавления новости
        filled_form = ArticleForm(request.POST, request.FILES)
        filled_form.save()
        send_telegram()
        return redirect('/home')


def about(request):
    return render(request, 'home/about.html')
