import finnhub
import requests


endpoint  = 'https://economia.awesomeapi.com.br/json/all/USD-BRL'
resposta = requests.request('GET', endpoint)
dolar = resposta.json()['USD']['ask']

print(dolar)
