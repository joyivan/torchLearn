import numpy as np
from sklearn.linear_model import LogisticRegression
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn import datasets
from sklearn import preprocessing
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline


# 获取所需数据集
iris=datasets.load_iris()
#每行的数据，一共四列，每一列映射为feature_names中对应的值
X=iris.data
print(X)
#每行数据对应的分类结果值（也就是每行数据的label值）,取值为[0,1,2]
Y=iris.target
print(Y)

#归一化处理
X = StandardScaler().fit_transform(X)
print(X.shape)

X=X[:,:2]
lr = LogisticRegression()   # Logistic回归模型
lr.fit(X, Y)        # 根据数据[x,y]，计算回归参数

N, M = 500, 500     # 横纵各采样多少个值
x1_min, x1_max = X[:, 0].min(), X[:, 0].max()   # 第0列的范围
x2_min, x2_max = X[:, 1].min(), X[:, 1].max()   # 第1列的范围
t1 = np.linspace(x1_min, x1_max, N)
t2 = np.linspace(x2_min, x2_max, M)
x1, x2 = np.meshgrid(t1, t2)                    # 生成网格采样点
x_test = np.stack((x1.flat, x2.flat), axis=1)   # 测试点
print(x_test.shape)
cm_light = mpl.colors.ListedColormap(['#77E0A0', '#FF8080', '#A0A0FF'])
cm_dark = mpl.colors.ListedColormap(['g', 'r', 'b'])
y_hat = lr.predict(x_test)       # 预测值
y_hat = y_hat.reshape(x1.shape)                 # 使之与输入的形状相同
plt.pcolormesh(x1, x2, y_hat, cmap=cm_light)     # 预测值的显示
plt.scatter(X[:, 0], X[:, 1], c=Y.ravel(), edgecolors='k', s=50, cmap=cm_dark)
plt.xlabel('petal length')
plt.ylabel('petal width')
plt.xlim(x1_min, x1_max)
plt.ylim(x2_min, x2_max)
plt.grid()
plt.show()

y_hat = lr.predict(X)
Y = Y.reshape(-1)
result = y_hat == Y
print(y_hat)
print(result)
acc = np.mean(result)
print('准确度: %.2f%%' % (100 * acc))
