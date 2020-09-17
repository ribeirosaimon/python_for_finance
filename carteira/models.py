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
    cotacao_atual = models.DecimalField(max_digits=20, decimal_places=2, blank=True, default=0)
    preco_medio = models.DecimalField(max_digits=20, decimal_places=2)
    dolarizado = models.BooleanField()
    lucro = models.DecimalField(max_digits=20, decimal_places=2, blank=True, default=0)

    def __str__(self):
        return self.papel


class Vendas(models.Model):
    MES_CHOICES = (
    	('01','Janeiro'),
    	('02','Fevereiro'),
    	('03','Março'),
    	('04','Abril'),
    	('05','Maio'),
    	('06','Junho'),
        )
    papel_venda = models.CharField(max_length=10)
    mes_carteira_venda = models.CharField(u'Mês', blank=True, max_length=200, choices = MES_CHOICES)
    quantidade_venda = models.DecimalField(max_digits=20, decimal_places=10)
    cotacao_atual_venda = models.DecimalField(max_digits=20, decimal_places=2)
    preco_medio_venda = models.DecimalField(max_digits=20, decimal_places=2, blank=True, default=0)
    dolarizado_venda = models.BooleanField()
    lucro_venda = models.DecimalField(max_digits=20, decimal_places=2, blank=True, default=0)

    def __str__(self):
        return self.papel_venda
