from django.contrib import admin
from .models import Carteira, Vendas

class CarteiraAdmin(admin.ModelAdmin):
    list_display = ('mes_carteira','papel','quantidade','preco_medio','dolarizado', 'lucro')
admin.site.register(Carteira, CarteiraAdmin)


class VendaAdmin(admin.ModelAdmin):
    list_display = ('mes_carteira_venda','papel_venda','quantidade_venda','preco_medio_venda','dolarizado_venda', 'lucro_venda')
admin.site.register(Vendas, VendaAdmin)
