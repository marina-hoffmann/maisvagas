from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Vaga(models.Model):
    titulo = models.CharField(
        max_length=100,
    )

    data_criacao = models.DateField(
        default= datetime.now,
        blank= True
    )

    empresa = models.ForeignKey(
        User,
        on_delete= models.CASCADE
    )

    local = models.CharField(
        max_length=100
    )

    descricao = models.TextField()

    requisitos = models.TextField()

    beneficios = models.TextField()

    publicada = models.BooleanField(
        default= False
    )

    categoria = models.CharField(
        max_length= 50
    )

    senioridade = models.CharField(
        max_length= 10
    )