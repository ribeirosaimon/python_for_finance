from django.db import models

class Mes(models.Model):
    mes = models.CharField(max_length=10)

class Carteira(models.Model):
    mes = models.ForeignKey(Mes, on_delete=models.CASCADE)
    papel = models.CharField(max_length=10)
    quantidade = models.IntegerField()
    preco_medio = models.DecimalField(max_digits=20, decimal_places=2)
    tipo_mercado = models.BooleanField()
