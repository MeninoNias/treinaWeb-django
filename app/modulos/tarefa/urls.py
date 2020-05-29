from django.urls import path

from .views import *

app_name = 'tarefa'
urlpatterns = [
    path('', listar_tarefas, name='listar_tarefas'),
    path('cadastrar_tarefa/', cadastrar_tarefa, name='cadastrar_tarefa'),
    path('atualizar_tarefa/<int:id>', autualizar_tarefa, name='atualizar_tarefa'),
    path('remover_tarefa/<int:id>', remover_tarefa, name='remover_tarefa'),
]