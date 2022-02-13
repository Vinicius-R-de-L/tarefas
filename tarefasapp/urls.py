from django.urls import path
from tarefasapp import views


urlpatterns = [
    path('', views.tarefas_list, name='tarefas_list'),
]