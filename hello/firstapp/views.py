from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'firstapp/home.html')


def about(request):
    return HttpResponse("<H2>О сайте</H2>")


def contact(request):
    return HttpResponse("<H2>Контакты</H2>")