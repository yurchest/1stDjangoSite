from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import Article,Comment,Contact
from .forms import ContactFormCv
from django.contrib import messages
from .telegram import send_message


menu = [
    {'title': "Главная", 'url_name': 'home'},
    {'title': "Str1", 'url_name': 'str1'},
    {'title': "Str2", 'url_name': 'str2'},
    {'title': "Str3", 'url_name': 'str3'},
    {'title': "О сайте", 'url_name': 'about'},
    {'title': "Резюме", 'url_name': 'cv'},

]


def index(request):
    articles = Article.objects.all()
    context = {
        'menu': menu,
        'articles': articles,
        'title': 'Главная страница',
    }
    return render(request, 'main/index.html', context=context)


def str1(request):
    messages = Contact.objects.all()
    context = {
        'menu': menu,
        'messages': messages,
        'title': 'Обратная связь',
    }
    return render(request, 'main/messages.html', context=context)

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

def curriculum(request):
    if request.method == "POST":
        form = ContactFormCv(request.POST)
        if form.is_valid():
            message = form.save()
            formatedDate = message.published_date.strftime("%Y-%m-%d %H:%M:%S")
            telegram_message = \
            f"Name: {message.name} \nEmail: {message.email} \nText: {message.text}  \nDate/Time: {formatedDate}"
            send_message(telegram_message)
            messages.success(request, 'Сообщение успешно отправлено')
    else:
        form = ContactFormCv()

    context = {
        'menu': menu,
        'title': 'Резюме',
        'form' : form,
    }
    return render(request, 'main/curriculum.html', context=context)



def about(request):
    context = {
        'menu': menu,
        'title': 'О сайте',
    }
    return render(request, 'main/about.html', context=context)

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1> OOOPS...  Страница не найдена  :( </h1>')
