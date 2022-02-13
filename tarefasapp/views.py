from django.shortcuts import render
from .models import Autor, Info, Tarefa
# Create your views here.

def base(request):
    return render(request, 'tarefas/base.html', {})

def tarefas_list(request):
    tarefas = Tarefa.objects.all()
    return render(request, 'tarefas/tarefas_list.html', {'tarefas' : tarefas})

def registros_list(request):
    autores = Autor.objects.all()
    tarefas = Tarefa.objects.all()
    infos = Info.objects.all()
    return render(request, 'tarefas/registros_list.html', {'tarefas' : tarefas, 'autores' : autores, 'infos' : infos})
        