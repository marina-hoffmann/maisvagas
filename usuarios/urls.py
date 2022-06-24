from django.urls import path

from . import views

urlpatterns = [
    path('cadastro', views.cadastro, name='cadastro'),
    path('login', views.login, name='login'),
    path('minhas-vagas', views.minhas_vagas, name='minhas-vagas'),
    path('logout', views.logout, name='logout')
]