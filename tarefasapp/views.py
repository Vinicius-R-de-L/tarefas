from django.shortcuts import render
from .models import Autor, Info, Tarefa
from .forms import TarefaForm
from django.shortcuts import redirect
from django.shortcuts import get_object_or_404
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

def crud(request):
    autores = Autor.objects.all()
    tarefas = Tarefa.objects.all()
    infos = Info.objects.all()
    return render(request, 'tarefas/crud.html', {'tarefas' : tarefas, 'autores' : autores, 'infos' : infos})

def new(request):
    if request.method == "POST":
        form = TarefaForm(request.POST)
        if form.is_valid():
            tarefa = form.save(commit=False)
            tarefa.titulo = tarefa.titulo
            tarefa.autor = tarefa.autor
            tarefa.info = tarefa.info
            tarefa.save()
            return redirect('crud',)
    else:
        form = TarefaForm()
    return render(request, 'tarefas/new.html', {'form': form})