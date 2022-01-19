from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

import random


def password(request):
    characters = list('abcedefghijklmnopqrstuvwxyz')

    length = eval(request.GET.get('length'))

    print(request.GET)

    if request.GET.get('uppercase'):
        characters += list('abcedefghijklmnopqrstuvwxyz'.upper())

    if request.GET.get('numbers'):
        characters += list('0123456789')

    if request.GET.get('special'):
        characters += list('@#$%^&*')

    if request.GET.get('input-length'):
        length = eval(request.GET.get('input-length'))

    password = ''.join([random.choice(characters) for i in range(length)])

    print(password)

    return render(request, "password.html", {'password': password})


def index(requset):
    return render(requset, "index.html")
