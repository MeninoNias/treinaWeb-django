from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def user_cadastro(request):
    template = 'usuario/form_user.html'

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:gerenciador:tarefa:listar_tarefas')
    else:
        form = UserCreationForm()

    return render(request, template, {'form':form})


