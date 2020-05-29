from django.shortcuts import render, redirect

# Create your views here.
from ...entidades.Tarefa import Tarefa
from ...forms import TarefaForm
from ...services import tarefa_service


def listar_tarefas(request):
    template = 'tarefa/listar_tarefas.html'
    tarefas = tarefa_service.listar_tarefas()

    context = {
        'tarefas': tarefas
    }

    return render(request, template, context)

def cadastrar_tarefa(request):
    template = 'tarefa/form_tarefa.html'

    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():

            titulo = form.cleaned_data['titulo']
            descricao = form.cleaned_data['descricao']
            data_expiracao = form.cleaned_data['data_expiracao']
            prioridade = form.cleaned_data['prioridade']

            tarefa = Tarefa(titulo=titulo, descricao=descricao, data_expiracao=data_expiracao, prioridade=prioridade)

            tarefa_service.cadastrar_tarefa(tarefa)

            return redirect('app:listar_tarefas')
    else:
        form = TarefaForm()

    context = {
        'form':form,
    }
    return render(request, template, context)

def autualizar_tarefa(request, id):
    template = 'tarefa/form_editar_tarefa.html'
    tarefa = tarefa_service.listar_tarefas_id(id)

    form = TarefaForm(request.POST or None, instance=tarefa)
    if form.is_valid():
        titulo = form.cleaned_data['titulo']
        descricao = form.cleaned_data['descricao']
        data_expiracao = form.cleaned_data['data_expiracao']
        prioridade = form.cleaned_data['prioridade']

        tarefa_nova = Tarefa(titulo=titulo, descricao=descricao, data_expiracao=data_expiracao, prioridade=prioridade)

        tarefa_service.atualizar_tarefa(tarefa_nova=tarefa_nova, tarefa=tarefa)

        return redirect('app:gerenciador:tarefa:listar_tarefas')

    context = {
        'form':form,
        'tarefa':tarefa
    }

    return render(request, template, context)

def remover_tarefa(request, id):
    template = 'tarefa/remover_tarefa.html'
    tarefa = tarefa_service.listar_tarefas_id(id)

    if request.method == 'POST':
        tarefa_service.remover_tarefa(tarefa)
        return redirect('app:gerenciador:tarefa:listar_tarefas')

    context = {
        'tarefa':tarefa
    }

    return render(request, template, context)