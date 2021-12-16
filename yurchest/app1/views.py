from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("STRANICA 1")

def Zagolovok(request):
    return HttpResponse("<h1> Заголовок 1</h1>")