from django.shortcuts import render
from django.contrib.auth.models import User, UserManager
from django.contrib.auth import *
from django.contrib.auth.decorators import login_required


def create_user(request, username, password):
    user: UserManager = User.objects.create_user(username=username, password=password)
    user.save()
    return render(request, "singUp.html", {})


def login(request, log, psw):
    user = authenticate(request, username=log, password=psw)
    d = {
        "username": log,
        "password": psw,
    }
    if user is not None:
        login(request, user, psw)
        return render(request, "authFun.html", d)
    else:
        return render(request, "notFound.html", d)


def page(request):
    username = 'danile'
    password = 'qwerty'

    user = authenticate(request, username=username, password=password)
    print(request.POST, user)

    user = authenticate(request, username=username, password=password)


@login_required
def fun_with_login(request):

    username = request.POST['username']
    password = request.POST['password']
    d = {
        "username": username,
        "password": password,
    }
    return render(request, "authFun.html", d)
