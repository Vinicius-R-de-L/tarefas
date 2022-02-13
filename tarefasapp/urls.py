from django.urls import path
from tarefasapp import views


urlpatterns = [
    path('', views.registros_list, name='registros_list'),
]