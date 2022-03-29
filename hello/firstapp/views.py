from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("<H2>Главная</H2>")

def about(request):
    return HttpResponse("<H2>О сайте</H2>")

def contact(request):
    return HttpResponse("<H2>Контакты</H2>")