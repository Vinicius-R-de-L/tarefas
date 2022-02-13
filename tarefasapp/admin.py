from django.contrib import admin

# Register your models here.

from tarefasapp.models import Autor, Info, Tarefa

admin.site.register(Tarefa)
admin.site.register(Autor)
admin.site.register(Info)
