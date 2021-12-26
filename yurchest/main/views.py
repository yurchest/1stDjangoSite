from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import Article,Comment

menu = [
    {'title': "Главная", 'url_name': 'home'},
    {'title': "Str1", 'url_name': 'str1'},
    {'title': "Str2", 'url_name': 'str2'},
    {'title': "Str3", 'url_name': 'str3'},
    {'title': "О сайте", 'url_name': 'about'},

]


def index(request):
    articles    = Article.objects.all()
    context = {
        'menu': menu,
        'articles': articles,
        'title': 'Главная страница',
    }
    return render(request, 'main/index.html', context=context)


def str1(request):
    context = {
        'menu': menu,
        'title': 'Str1',
    }
    return render(request, 'main/str1.html', context=context)

def str2(request):
    context = {
        'menu': menu,
        'title': 'Str2',
    }
    return render(request, 'main/str2.html', context=context)

def str3(request):
    context = {
        'menu': menu,
        'title': 'Str3',
    }
    return render(request, 'main/str3.html', context=context)



def about(request):
    context = {
        'menu': menu,
        'title': 'О сайте',
    }
    return render(request, 'main/about.html', context=context)

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1> OOOPS...  Страница не найдена  :( </h1>')
