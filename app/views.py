from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib import messages

def login(request):
    template = 'usuario/login.html'
    if request.method == 'POST':
        username = request.POST['username']
        senha = request.POST['password']
        user = auth.authenticate(request, username=username, password=senha)

        if user:
            auth.login(request, user)
            if user.is_superuser:
                return redirect('/admin/')
            else:
                return redirect('app:gerenciador:tarefa:listar_tarefas')
        else:
            messages.error(request, 'Usuario ou senha incorretos')
            return redirect('/login/')
    form = AuthenticationForm()

    context = {
        'form': form
    }

    return render(request, template, context)


def logout(request):
    template = 'usuario/logout'

    return render(request, template)


def index(request):
    return redirect('/login/')