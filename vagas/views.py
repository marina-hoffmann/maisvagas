from django.shortcuts import render, get_object_or_404, redirect
from vagas.models import Vaga
from django.contrib.auth.models import User
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib import messages

def index(request):
    vagas = Vaga.objects.all()
    return render(request, 'vagas.html', context={'vagas':vagas})

def criar_vaga(request):
    if request.method == 'POST':
        titulo = request.POST['titulo']
        local = request.POST['local']
        descricao = request.POST['descricao']
        requisitos = request.POST['requisitos']
        beneficios = request.POST['beneficios']
        categoria = request.POST['categoria']
        senioridade = request.POST['senioridade']
        user = get_object_or_404(User, pk=request.user.id)
        try:    
            publicada = request.POST['publicada']
            publicada = True                    
        except MultiValueDictKeyError:
            publicada = False
        vaga = Vaga.objects.create(empresa=user,titulo=titulo,local=local,descricao=descricao, requisitos=requisitos,beneficios=beneficios, publicada=publicada, categoria=categoria, senioridade=senioridade)
        vaga.save()
        return redirect('minhas-vagas')
    else:
        return render(request, 'criar-vaga.html')

def buscar_vaga(request):
    lista_vagas = Vaga.objects.order_by('-data_criacao').filter(publicada=True)

    if 'buscar-vaga' in request.GET:
        nome_a_buscar = request.GET['buscar-vaga']
        lista_vagas = lista_vagas.filter(titulo__icontains=nome_a_buscar)

    dados = {
        'vagas' : lista_vagas
    }

    return render(request, 'buscar-vaga.html', dados)

def deletar_vaga(request, vaga_id):
    vaga = get_object_or_404(Vaga, pk=vaga_id)
    vaga.delete()
    return redirect('minhas-vagas')

def editar_vaga(request, vaga_id):    
    vaga = Vaga.objects.filter(id=vaga_id).first()
    dados = {'vaga' : vaga}
    if request.method == 'POST':
        vaga.titulo = request.POST['titulo']
        vaga.local = request.POST['local']
        vaga.descricao = request.POST['descricao']
        vaga.requisitos = request.POST['requisitos']
        vaga.beneficios = request.POST['beneficios']
        vaga.categoria = request.POST['categoria']
        vaga.senioridade = request.POST['senioridade']
        vaga.user = get_object_or_404(User, pk=request.user.id)
        try:    
            publicada = request.POST['publicada']
            vaga.publicada = True                    
        except MultiValueDictKeyError:
            vaga.publicada = False
        vaga.save()
        return redirect('minhas-vagas')
    return render(request, 'editar-vaga.html', dados)

def vaga(request, id_vaga):
    vaga = Vaga.objects.filter(id=id_vaga).first()
    if (not vaga == None):
        return render(request, 'vaga.html', context={"vaga":vaga})
    else:
        messages.error(request,'Vaga não encontrada.')
        return redirect('/')