from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Carteira
from django.views.generic import TemplateView
import requests

class CarteiraView(ListView):
    model = Carteira
    template_name = 'home.html'



def preco_acao(request):
    acao = 'movi3'
    endpoint  = f'https://secure-wildwood-34847.herokuapp.com/{acao}'
    resposta = requests.request('GET', endpoint)
    resposta_da_acao = resposta.json()
    preco_acao = resposta_da_acao[acao]['fundamentalist_analysis']['adj_close']
    return render (request,'home.html', {'preco_acao':preco_acao})
