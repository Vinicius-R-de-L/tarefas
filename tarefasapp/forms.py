from django import forms

from .models import Autor, Info, Tarefa

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ('nome', 'sobrenome',)

class InfoForm(forms.ModelForm):
    class Meta:
        model = Info
        fields = ('conteudo',)

class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ('titulo', 'autor', 'info',)