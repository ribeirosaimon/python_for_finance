from django.contrib import admin
from .models import Carteira

class CarteiraAdmin(admin.ModelAdmin):
    list_display = ('mes_carteira','papel','quantidade','preco_medio','dolarizado')
admin.site.register(Carteira, CarteiraAdmin)
