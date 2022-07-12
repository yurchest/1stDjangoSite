from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User, Group

from .telegram import send_message
from .models import Article,Comment,Contact
from .forms import ContactFormCv, UserRegistrationForm

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

#@login_required
@permission_required('main.can_see_messages')
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
            messages.success(request, 'Сообщение успешно отправлено. Надеюсь оно до меня дойдет (^_^)')
    else:
        form = ContactFormCv()

    num_visits=request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    context = {
        'menu': menu,
        'title': 'Резюме',
        'form' : form,
        'num_visits':num_visits,
    }

    

    return render(request, 'main/curriculum.html', context=context)


def about(request):
    context = {
        'menu': menu,
        'title': 'О сайте',
    }
    return render(request, 'main/about.html', context=context)


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])

            # Save the User object
            new_user.save()
            new_user.groups.add(Group.objects.get(name='SiteUsers'))
            return render(request, 'registration/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'user_form': user_form})

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1> OOOPS...  Страница не найдена  :( </h1>')
