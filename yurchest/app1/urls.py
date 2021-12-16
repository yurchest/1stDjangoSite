from django.urls import path

from .views import *

urlpatterns = [
    path('', index),
    path('str1', Zagolovok)
]