# 문제1 : 머신러닝을 사용해서 300명이 방문했을 때 판매량을 예측해보세요
import sklearn
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

원본데이터 = pd.read_csv('kyobo.csv', encoding='cp949')

X = 원본데이터.iloc[:,:-1].values
y = 원본데이터.iloc[:,-1].values

book = LinearRegression()
book.fit(X,y)
y_pred = book.predict(X)
y_result = book.predict([[300]])
print(y_result,'명')

plt.scatter(X,y, color='green')
plt.plot(X,y_pred, color='red')
plt.title('corrsion rate per hours')
plt.xlabel('bang')
plt.ylabel('pan')
plt.show()