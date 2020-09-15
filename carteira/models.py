from django.db import models


class Carteira(models.Model):
    MES_CHOICES = (
    	('01','Janeiro'),
    	('02','Fevereiro'),
    	('03','Março'),
    	)
    mes_carteira = models.CharField(u'Mês', blank=True, max_length=200, choices = MES_CHOICES)
    papel = models.CharField(max_length=10)
    quantidade = models.DecimalField(max_digits=20, decimal_places=10)
    preco_medio = models.DecimalField(max_digits=20, decimal_places=2)
    dolarizado = models.BooleanField()
    lucro = models.DecimalField(max_digits=20, decimal_places=2, blank=True, default=0)

    def __str__(self):
        return self.papel
