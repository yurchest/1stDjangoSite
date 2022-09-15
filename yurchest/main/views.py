from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.models import User, Group
from django.views.generic import TemplateView, ListView, View
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.edit import FormView

from .serializers import NewsSerializer
from .telegram import send_message
from .models import Article, Comment, Contact, VisitNumber, News
from .forms import ContactFormCv, UserRegistrationForm
from .stats_visit import change_info
from .parse_news_yandex import parse

from rest_framework.views import APIView
from rest_framework import generics


class Index(TemplateView):
    template_name = "main/index.html"

    def get_context_data(self, *args, **kwargs):
        context = super(Index, self).get_context_data(*args, **kwargs)
        context['title'] = 'Главная страница'
        return context


class Messages(PermissionRequiredMixin, TemplateView):
    permission_required = 'main.can_see_messages'

    template_name = "main/messages.html"

    def get_context_data(self, *args, **kwargs):
        context = super(Messages, self).get_context_data(*args, **kwargs)
        context['title'] = 'Обратная связь'
        context['messages'] = Contact.objects.order_by('-published_date')
        return context


class News_view(TemplateView):
    template_name = "main/news.html"

    def get_context_data(self, *args, **kwargs):
        context = super(News_view, self).get_context_data(*args, **kwargs)
        # parse(url='https://ria.ru/lenta/')
        context['title'] = 'Новости'
        context['news'] = News.objects.order_by('-time_create')[:30]
        return context


class Str3(TemplateView):
    extra_context = {'title': 'Str3', }
    template_name = "main/str3.html"


class Curriculum(FormView):
    form_class = ContactFormCv
    template_name = 'main/curriculum.html'

    def get_context_data(self, **kwargs):
        change_info(self.request)
        context = super().get_context_data(**kwargs)
        context['number_visits'] = VisitNumber.objects.get(id=1)
        context['title'] = 'Резюме'
        return context

    def form_valid(self, form):
        message = form.save()
        formatedDate = message.published_date.strftime("%Y-%m-%d %H:%M:%S")
        telegram_message = \
            f"Name: {message.name} \nEmail: {message.email} \nText: {message.text}  \nDate/Time: {formatedDate}"
        send_message(telegram_message)
        messages.success(self.request, 'Сообщение успешно отправлено. Надеюсь оно до меня дойдет (^_^)')
        return super().form_valid(form)

    def get_success_url(self):
        return self.request.path


def about(request):
    context = {
        'title': 'О сайте',
    }
    return render(request, 'main/about.html', context=context)


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        context = {
            'title': 'О сайте',
            'user_form': user_form,
        }
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])

            # Save the User object
            new_user.save()
            new_user.groups.add(Group.objects.get(name='SiteUsers'))
            return render(request, 'registration/register_done.html', context)
    else:
        user_form = UserRegistrationForm()

    context = {
        'title': 'О сайте',
        'user_form': user_form,
    }
    return render(request, 'registration/register.html', context)


class NewsAPIView(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer



def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1> OOOPS...  Страница не найдена  :( </h1>')
