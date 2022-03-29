from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # return render(request, 'firstapp/home.html')
    header = "Персональные данные"
    langs = ["Английский", "Испанский", "Русский",]
    user = {"name": "Максим,", "age": 30}
    addr = ("Виноградная", 23, 45)
    data = {"header": header, "langs": langs, "user": user, "address": addr}
    return render(request, "index.html", context=data)

def about(request):
    return HttpResponse("<H2>О сайте</H2>")


def contact(request):
    return HttpResponse("<H2>Контакты</H2>")