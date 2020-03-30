import pandas as pd
import quandl
import math
import numpy as np
from sklearn import preprocessing, model_selection, svm
from sklearn.linear_model import LinearRegression

quandl.ApiConfig.api_key = 'xEgXfFpmyJ9usGFxzJNw'

df = quandl.get('WIKI/GOOGL')

print(df.head())

df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]

df['HL_PCT'] = (df['Adj. High'] - df['Adj. Low']) / df['Adj. Close'] * 100
df['PCT_CHANGE'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100

df = df[['Adj. Close', 'HL_PCT', 'PCT_CHANGE', 'Adj. Volume']]

forecast_col = 'Adj. Close'

df.fillna(-99999, inplace=True)

forecast_out = int(math.ceil(0.01*len(df)))
print(forecast_out, 365*0.01)

df['label'] = df[forecast_col].shift(-forecast_out)

x = np.array(df.drop(['label'],1))
y = np.array(df['label'])

x = preprocessing.scale(x)

x = x[:-forecast_out]
df.dropna(inplace=True)
y = np.array(df['label'])

x_train, x_test, y_train, y_test = model_selection.train_test_split(x, y, test_size=0.2)

clf = LinearRegression()
clf.fit(x_train, y_train)
accuracy = clf.score(x_test, y_test)

print(accuracy)