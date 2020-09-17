from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Carteira
from django.views.generic import TemplateView
import requests
import finnhub
from .key_api import *




def home(request):
    context ={
        'title':'Seja Bem vindo',
        'form':'meu grande amigo',
    }
    return render(request, 'home.html',context)


def lista_acao(request):
    queryset = Carteira.objects.all()
    total_carteira = soma_da_carteira(queryset)
    queryset, lucro_da_carteira = tratamento(queryset)
    context = {
        'queryset':queryset,
        'total_carteira':total_carteira,
        'dolar':get_dolar_price(),
        'lucro_da_carteira':f'{lucro_da_carteira:.2f}',
    }
    return render(request, 'list_items.html', context)

def tratamento(lista_de_acao):
    lista = []
    lucro_da_carteira = float(0)
    for acao in lista_de_acao:
        preco_acao = 0
        if acao.dolarizado == False:
            if acao.papel == 'caixa':
                preco_acao = 1
            else:
                preco_acao = scraping(acao)
        if acao.dolarizado == True:
            if acao.papel == 'caixa':
                preco_acao = 1
            else:
                preco_acao = scraping_exterior(acao)
        lucro = (float(acao.quantidade)*float(preco_acao) - (float(acao.quantidade) * float(acao.preco_medio)))
        dicionario_retorno = {
            'mes_carteira':acao.mes_carteira,
            'papel':acao.papel,
            'quantidade':acao.quantidade,
            'cotacao_atual':f'{float(preco_acao):.2f}',
            'preco_medio':f'{acao.preco_medio:.2f}',
            'dolarizado': acao.dolarizado,
            'lucro':f'{lucro:.2f}'
        }
        if dicionario_retorno['dolarizado'] == True:
            dolar = get_dolar_price()
            lucro_da_carteira += float(dicionario_retorno['lucro'])*dolar
        else:
            lucro_da_carteira += float(dicionario_retorno['lucro'])
        lista.append(dicionario_retorno)
    return lista, lucro_da_carteira

def scraping(acao):
    endpoint  = f'https://secure-wildwood-34847.herokuapp.com/{acao}'
    resposta = requests.request('GET', endpoint)
    resposta_da_acao = resposta.json()
    return float(resposta_da_acao[f'{acao}']['fundamentalist_analysis']['adj_close'])

def scraping_exterior(acao):
    try:
        r = requests.get(f'https://finnhub.io/api/v1/quote?symbol={acao}&token={KEY_API}')
        return float(r.json()['c'])
    except:
        return 22.72


def soma_da_carteira(queryset):
    total_carteira = float(0)
    dolar = get_dolar_price()
    for acao in queryset:
        if acao.papel == 'caixa':
            if acao.dolarizado == False:
                total_carteira += float(acao.quantidade)*float(acao.preco_medio)
            else:
                total_carteira += (float(acao.quantidade)*float(acao.preco_medio))* dolar
        else:
            if acao.dolarizado == True:
                total_carteira += float(acao.quantidade)*float(scraping_exterior(acao))* dolar
            else:
                total_carteira += float(acao.quantidade)*float(scraping(acao))
    return total_carteira

def get_dolar_price():
    endpoint  = 'https://economia.awesomeapi.com.br/json/all/USD-BRL'
    resposta = requests.request('GET', endpoint)
    return float(resposta.json()['USD']['ask'])
