# 머신러닝
# pip install scikit-learn

import sklearn
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

print('사이킷런 버전', sklearn.__version__)

운동시간 = [[1],[2],[3],[4],[5]]
근육량 = [[1.4],[2.3],[3.5],[4.5],[5.3]]

lin = LinearRegression()
# 인공지능 학습 fix(X,y)
lin.fit(운동시간,근육량)

# 학습 기반으로 예측
근육량예측 = lin.predict(운동시간)
print(근육량예측)
#2.5시간 운동하면 근육량이 얼마일까
print('2.5시간 운동하면 근육 증갸랑은',lin.predict([[2.5]])) 

plt.scatter(운동시간, 근육량, color='blue')         # 점 (실제 제공데이터)
plt.plot(운동시간, 근육량예측, color='green')       # 선 (예측값)
plt.show()