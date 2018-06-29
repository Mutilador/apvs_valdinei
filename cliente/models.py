from django.db import models
from django.utils import timezone

CARRO_RESERVA = (
    ('7','7 dias'),
    ('10', '14 dias')
)

REBOQUE_DISTANCIA = (
    ('300','300Km'),
    ('500','500Km')
)

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
    id = models.AutoField(primary_key=True)
    user = models.OneToOneField(Cliente,
        on_delete=models.CASCADE,)
    marca = models.CharField(max_length=200)
    modelo = models.CharField(max_length=200)
    ano = models.IntegerField()
    valor = models.CharField(max_length=200)
    dd_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

# Create your models here.
class SeguroDetail(models.Model):
    id = models.AutoField(primary_key=True)
    fipe_detail = models.OneToOneField(FipeDetail,
        on_delete=models.CASCADE,)
    choice_dano = models.BooleanField()
    choice_reboque_distancia = models.CharField(choices=CARRO_RESERVA,max_length=2,verbose_name="reboque_distancia")
    choice_reembolso = models.BooleanField()
    choice_reserva = models.CharField(choices=REBOQUE_DISTANCIA,max_length=2,verbose_name="carro_reserva")

    def __str__(self):
        return str(self.id)

