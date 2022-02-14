from django.urls import path
from tarefasapp import views


urlpatterns = [
    path('', views.registros_list, name='registros_list'),
    path('tarefas_list', views.tarefas_list, name='tarefas_list'),
    path('crud', views.crud, name='crud'),
    path('new', views.new, name='new'),
]