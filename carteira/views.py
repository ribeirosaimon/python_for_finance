from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Carteira
from django.views.generic import TemplateView
import requests

def home(request):
    context ={
        'title':'Seja Bem vindo',
        'form':'meu grande amigo',
    }
    return render(request, 'home.html',context)


def lista_acao(request):
    queryset = Carteira.objects.all()
    total_carteira = soma_da_carteira(queryset)
    queryset = tratamento(queryset)
    context = {
        'queryset':queryset,
        'total_carteira':total_carteira,
    }
    return render(request, 'list_items.html', context)

def tratamento(lista_de_acao):
    lista = []
    for acao in lista_de_acao:
        dicionario_retorno = {
            'mes_carteira':acao.mes_carteira,
            'papel':acao.papel,
            'quantidade':acao.quantidade,
            'cotacao_atual':f'{float(scraping(acao)):.2f}',
            'preco_medio':f'{acao.preco_medio:.2f}',
            'dolarizado': acao.dolarizado,
            'lucro':f'{(float(acao.quantidade)*float(scraping(acao)) - (float(acao.quantidade) * float(acao.preco_medio))):.2f}'
        }
        lista.append(dicionario_retorno)
    return lista

def scraping(acao):
    endpoint  = f'https://secure-wildwood-34847.herokuapp.com/{acao}'
    resposta = requests.request('GET', endpoint)
    resposta_da_acao = resposta.json()
    return float(resposta_da_acao[f'{acao}']['fundamentalist_analysis']['adj_close'])

def soma_da_carteira(queryset):
    total_carteira = float(0)
    for acao in queryset:
        total_carteira += float(acao.quantidade)*float(scraping(acao))
    return total_carteira
