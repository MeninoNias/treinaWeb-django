from django import forms
from .util import ChangeDateInput, adiciona_form_control

from .models import Tarefa



class TarefaForm(forms.ModelForm):

    class Meta:
        model = Tarefa
        fields = ['titulo', 'descricao', 'data_expiracao', 'prioridade']

        widgets = {
            'data_expiracao':ChangeDateInput()
        }

    def __init__(self, *args, **kwargs):
        super(TarefaForm, self).__init__(*args, **kwargs)
        adiciona_form_control(self)



