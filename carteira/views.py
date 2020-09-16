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
    queryset = tratamento(queryset)
    context = {
        'queryset':queryset,
        'title':'Carteira',
    }
    return render(request, 'list_items.html', context)

def tratamento(lista_de_acao):
    lista = []
    for acao in lista_de_acao:
        endpoint  = f'https://secure-wildwood-34847.herokuapp.com/{acao}'
        resposta = requests.request('GET', endpoint)
        resposta_da_acao = resposta.json()
        cotacao_atual = resposta_da_acao[f'{acao}']['fundamentalist_analysis']['adj_close']
        dicionario_retorno = {
            'mes_carteira':acao.mes_carteira,
            'papel':acao.papel,
            'quantidade':acao.quantidade,
            'cotacao_atual':acao.cotacao_atual,
            'preco_medio':acao.preco_medio,
            'dolarizado': acao.dolarizado,
            'lucro':acao.quantidade * acao.preco_medio
        }
        lista.append(dicionario_retorno)
    return lista
