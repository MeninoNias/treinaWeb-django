from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tarefa(models.Model):

    PRIORIDADE_CHOICES = [
        ('1', 'Muito alta'),
        ('2', 'Alta'),
        ('3', 'Normal'),
        ('4', 'Baixa'),
        ('5', 'Muito baixa'),
    ]

    titulo= models.CharField(max_length=30, null=False, blank=False)
    descricao= models.CharField(max_length=160, null=False, blank=False)
    data_expiracao= models.DateField(null=False, blank=False)
    prioridade= models.CharField(max_length=1, choices=PRIORIDADE_CHOICES, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)

    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name='Tarefa'
        verbose_name_plural = 'Tarefas'
        ordering = ['-data_expiracao']
