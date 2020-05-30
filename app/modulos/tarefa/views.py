from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
from ...entidades.Tarefa import Tarefa
from ...forms import TarefaForm
from ...services import tarefa_service

@login_required()
def listar_tarefas(request):
    template = 'tarefa/listar_tarefas.html'

    if request.user.is_superuser:
        tarefas = tarefa_service.listar_tarefas()
    else:
        tarefas = tarefa_service.listar_tarefas_user(request.user)

    context = {
        'tarefas': tarefas
    }

    return render(request, template, context)

@login_required()
def cadastrar_tarefa(request):
    template = 'tarefa/form_tarefa.html'

    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():

            titulo = form.cleaned_data['titulo']
            descricao = form.cleaned_data['descricao']
            data_expiracao = form.cleaned_data['data_expiracao']
            prioridade = form.cleaned_data['prioridade']
            usuario = request.user
            tarefa = Tarefa(titulo=titulo, descricao=descricao, data_expiracao=data_expiracao, prioridade=prioridade, usuario=usuario)

            tarefa_service.cadastrar_tarefa(tarefa)

            messages.success(request, 'Tarefa alterada com sucesso')
            return redirect('app:gerenciador:tarefa:listar_tarefas')
    else:
        form = TarefaForm()

    context = {
        'form':form,
    }
    return render(request, template, context)

@login_required()
def autualizar_tarefa(request, id):
    template = 'tarefa/form_editar_tarefa.html'
    tarefa = tarefa_service.listar_tarefas_id(id)
    if not request.user.is_superuser:
        if request.user != tarefa.user:
            messages.error(request, 'Você não tem permissão para alterar essa tarefa')
            return redirect('app:gerenciador:tarefa:listar_tarefas')

    form = TarefaForm(request.POST or None, instance=tarefa)
    if form.is_valid():
        titulo = form.cleaned_data['titulo']
        descricao = form.cleaned_data['descricao']
        data_expiracao = form.cleaned_data['data_expiracao']
        prioridade = form.cleaned_data['prioridade']

        tarefa_nova = Tarefa(titulo=titulo, descricao=descricao, data_expiracao=data_expiracao, prioridade=prioridade, usuario=tarefa.user)

        tarefa_service.atualizar_tarefa(tarefa_nova=tarefa_nova, tarefa=tarefa)

        messages.success(request, 'Tarefa alterada com sucesso')
        return redirect('app:gerenciador:tarefa:listar_tarefas')

    context = {
        'form':form,
        'tarefa':tarefa
    }

    return render(request, template, context)

@login_required()
def remover_tarefa(request, id):
    template = 'tarefa/remover_tarefa.html'
    tarefa = tarefa_service.listar_tarefas_id(id)

    if not request.user.is_superuser:
        if request.user != tarefa.user:
            messages.error(request, 'Você não tem permissão para remover essa tarefa')
            return redirect('app:gerenciador:tarefa:listar_tarefas')

    if request.method == 'POST':
        tarefa_service.remover_tarefa(tarefa)

        messages.error(request, 'Tarefa alterada com sucesso')
        return redirect('app:gerenciador:tarefa:listar_tarefas')

    context = {
        'tarefa':tarefa
    }

    return render(request, template, context)