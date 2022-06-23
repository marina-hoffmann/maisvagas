from django.shortcuts import render
from vagas.models import Vaga

# Create your views here.
def index(request):
    vagas = Vaga.objects.all()
    return render(request, 'vagas.html', context={'vagas':vagas})