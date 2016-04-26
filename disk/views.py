# -*- coding:utf -*-

from django.shortcuts import render_to_response
from django.http import HttpResponse
from .forms import LoginForm


from .forms import  UserForm
from .models import  User

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            headimg = form.cleaned_data['headimg']
            user = User(username=username, headimg=headimg)
            user.save()

            return HttpResponse('OK')
    else:
        form = UserForm()
    return render_to_response('register.html', {'form': form})


def cook(requests):
    rep = HttpResponse('123')
    rep.set_cookie('isfirefox', True,domain='127.0.0.1', max_age=100)
    return rep



def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email, pwd = form.cleaned_data()
            print email, pwd
    else:
        form = LoginForm()

    return render_to_response('login.html', {'form': form})