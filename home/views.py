from django.shortcuts import render, redirect
from publications.models import Article
from turnir.models import Turnir
from crafts.models import Craft
from fish_news.models import New
from .forms import ArticleForm
from telebot.send_message import send_telegram
from .models import Contact


def index(request):
    articles = Article.objects.all()
    turnirs = Turnir.objects.all()
    crafts = Craft.objects.all()
    news = New.objects.all()
    data = {
        'articles': articles,
        'turnirs': turnirs,
        'crafts': crafts,
        'news': news

    }
    print(type(articles))
    return render(request, 'home/index.html', context=data)

def get_article(request, aid):
    article = Article.objects.filter(pk=aid)
    return render(request, 'publications/article.html', {'articles': article})
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

