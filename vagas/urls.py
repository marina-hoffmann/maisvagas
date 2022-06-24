from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('criar-vaga', views.criar_vaga, name='criar-vaga')
]