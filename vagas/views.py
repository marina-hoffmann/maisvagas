from django.shortcuts import render
from vagas.models import Vaga

def index(request):
    vagas = Vaga.objects.all()
    return render(request, 'vagas.html', context={'vagas':vagas})

def criar_vaga(request):
    # if request.method == 'POST':
    #     nome_receita = request.POST['nome_receita']
    #     ingredientes = request.POST['ingredientes']
    #     modo_preparo = request.POST['modo_preparo']
    #     tempo_preparo = request.POST['tempo_preparo']
    #     rendimento = request.POST['rendimento']
    #     categoria = request.POST['categoria']
    #     foto_receita = request.FILES['foto_receita']
    #     user = get_object_or_404(User, pk=request.user.id)
    #     receita = Receita.objects.create(pessoa=user,nome_receita=nome_receita, ingredientes=ingredientes, modo_preparo=modo_preparo,tempo_preparo=tempo_preparo, rendimento=rendimento,categoria=categoria, foto_receita=foto_receita)
    #     receita.save()
    #     return redirect('dashboard')
    # else:
    return render(request, 'criar-vaga.html')