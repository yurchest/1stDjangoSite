from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('str1', str1, name='str1'),
    path('str2', str2, name='str2'),
    path('str3', str3, name='str3'),
    path('about/', about, name='about'),

]
