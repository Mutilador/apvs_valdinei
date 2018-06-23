from django.db import models
from django.utils import timezone

# Create your models here.
class Cliente(models.Model):
    date_register = models.DateTimeField(auto_now=timezone.now())
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    cidade = models.CharField(max_length=200)
    bairro = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)


    def __str__(self):
        return self.nome

# Create your models here.
class FipeDetail(models.Model):
    user = models.OneToOneField(Cliente,
        on_delete=models.CASCADE,
        primary_key=True,)
    marca = models.CharField(max_length=200)
    modelo = models.CharField(max_length=200)
    ano = models.IntegerField()
    valor = models.CharField(max_length=200)


    def __str__(self):
        return self.nome

