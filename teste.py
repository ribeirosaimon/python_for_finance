import requests

def preco_acao(acao):
    endpoint  = f'https://secure-wildwood-34847.herokuapp.com/{acao}'
    resposta = requests.request('GET', endpoint)
    resposta_da_acao = resposta.json()
    resposta_da_acao = resposta_da_acao[acao]['fundamentalist_analysis']['adj_close']
    return resposta_da_acao
