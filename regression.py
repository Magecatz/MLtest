import pandas as pd
import quandl
import math

quandl.ApiConfig.api_key = 'xEgXfFpmyJ9usGFxzJNw'

df = quandl.get('WIKI/GOOGL')

print(df.head())

df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]

df['HL_PCT'] = (df['Adj. High'] - df['Adj. Low']) / df['Adj. Close'] * 100
df['PCT_CHANGE'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100

df = df[['Adj. Close', 'HL_PCT', 'PCT_CHANGE', 'Adj. Volume']]

forecast_cal = 'Adj. Close'

df.fillna(-99999, inplace=True)

forecast_out = int(math.ceil(0.1*len(df)))7