from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect


def login(request):
    template = 'usuario/login.html'

    form = AuthenticationForm()

    return render(request, template, {'form': form})


def logout(request):
    template = 'usuario/logout'

    return render(request, template)


def index(request):
    return redirect('/login/')