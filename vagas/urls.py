from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('criar-vaga', views.criar_vaga, name='criar-vaga'),
    path('editar-vaga/<int:vaga_id>', views.editar_vaga, name='editar-vaga'),
    path('deletar-vaga/<int:vaga_id>', views.deletar_vaga, name='deletar-vaga'),
    path('vaga/<int:id_vaga>', views.vaga, name='vaga')
]