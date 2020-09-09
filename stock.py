import pandas as pd
import numpy as np
import yfinance as yf
from datetime import datetime
from pandas_datareader import data as pdr

yf.pdr_override()

stock = input('Enter a stock tiker symbol: ')
print(stock)

start_year = 2019
start_month = 1
start_day = 1

start = datetime(start_year,start_month,start_day)
now = datetime.now()
df = pdr.get_data_yahoo(stock, start,now)
'''
ma=50
smaString=f'Sma_{ma}'

df[smaString] = df.iloc[:,4].rolling(window=ma).mean()
numH, numC = 0,0
for i in df.index:
    if(df['Adj Close'][i] > df[smaString][i]):
        print('The Close is higher')
        numH += 1
    else:
        print('The Close is lower')
        numC += 1

print('Num Higher: ',numH)
print('Num Lower: ', numC)
'''

emasUsed[3,5,8,10,12,15,30,35,40,45,50,60]

for x in emasUsed:
    ema = x
    df[f'Ema_{ema}']=round(df.iloc[:,4].ewm(span=ema, adjust=False).mean(),2)

print(df.tail())
