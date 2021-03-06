from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserForm


def index(request):
    return render(request, 'index.html')
    # header = "Персональные данные"
    # langs = ["Английский", "Испанский", "Русский",]
    # user = {"name": "Максим,", "age": 30}
    # addr = ("Виноградная", 23, 45)
    # data = {"header": header, "langs": langs, "user": user, "address": addr}
    # return render(request, "index.html", context=data)


def home(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        output = "<h2>Пользователь</h2><h3>Имя - {0}," \
                 " Возраст - {1}</h3>".format(name, age)
        return HttpResponse(output)
    else:
        userform = UserForm()
        return render(request, "firstapp/home.html", {"form": userform})
    # userform = UserForm()
    # return render(request, "firstapp/home.html",
    #               {"form": userform})
    # return render(request, 'firstapp/home.html')


def about(request):
    return render(request, 'firstapp/about.html')


def contact(request):
    return HttpResponse("<H2>Контакты</H2>")