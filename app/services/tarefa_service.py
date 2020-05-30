from ..models import Tarefa


def cadastrar_tarefa(tarefa):
    Tarefa.objects.create(titulo=tarefa.titulo,
                          descricao=tarefa.descricao,
                          data_expiracao=tarefa.data_expiracao,
                          prioridade=tarefa.prioridade,
                          user=tarefa.usuario)

def listar_tarefas_user(usuario):
    return Tarefa.objects.filter(user=usuario).all()

def listar_tarefas():
    return Tarefa.objects.all()

def listar_tarefas_id(id):
    return Tarefa.objects.get(id=id)


def atualizar_tarefa(tarefa, tarefa_nova):
    tarefa.titulo = tarefa_nova.titulo
    tarefa.descricao = tarefa_nova.descricao
    tarefa.data_expiracao = tarefa_nova.data_expiracao
    tarefa.prioridade = tarefa_nova.prioridade
    tarefa.save(force_update=True)


def remover_tarefa(tarefa):
    tarefa.delete()