import yfinance as yf
from requests import get
from bs4 import BeautifulSoup

def site(acao):
	start_url = f'https://finance.yahoo.com/quote/{acao}/key-statistics?p={acao}'
	start_browser = BeautifulSoup(get(start_url).content, "html.parser")
	browser = start_browser.find('div', {'id': 'quote-header-info'})
	preco = float(browser.find('span', {'data-reactid': '32'}).text)
	porcentagem = browser.find('span', {'data-reactid': '33'}).text.replace('(',',').replace(')','').split(',')
	preco_intradiario = float(porcentagem[0])
	porcentagem_diaria = float(porcentagem[1][:-1])
	tbody = start_browser.find('tbody', {'data-reactid': '76'})
	market_cap = tbody.find('td', {'data-reactid': '84'}).text
	print(market_cap)
	return preco, preco_intradiario, porcentagem_diaria

mu = site('mu')
print(mu)
