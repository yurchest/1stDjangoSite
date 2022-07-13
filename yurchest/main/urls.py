from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.decorators import login_required

from .views import *

urlpatterns = [
    path('', Index.as_view(), name='home'),
    path('messages/', Messages.as_view(), name='messages'),
    path('news', News_view.as_view(), name='news'),
    path('str3', Str3.as_view(), name='str3'),
    path('about/', about, name='about'),
    path('curriculum', Curriculum.as_view(), name='cv'),
    path('register/', register, name='register'),
]

urlpatterns += staticfiles_urlpatterns()
