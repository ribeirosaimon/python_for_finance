from django.db import models

class Mes(models.Model):
    mes_do_ano = models.CharField(max_length=10)
    def __str__(self):
        return self.mes_do_ano


class Carteira(models.Model):
    mes_carteira = models.ForeignKey(Mes, on_delete=models.CASCADE)
    papel = models.CharField(max_length=10)
    quantidade = models.IntegerField()
    preco_medio = models.DecimalField(max_digits=20, decimal_places=2)
    dolarizado = models.BooleanField()
    def __str__(self):
        return self.papel
