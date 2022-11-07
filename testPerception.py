import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

class Perception():
    def __init__(self):
        self.weight = None
    def sign(self,value):
        return 1 if value >= 0 else -1

    def fit(self, data_set, labels):
        lr = 0.01
        data_set = np.array(data_set)
        n = data_set.shape[0]
        m = data_set.shape[1]
        weights = np.zeros(m)
        i = 0
        while i < n:
            if (labels[i] * self.sign(np.dot(weights, data_set[i])) == -1):
                #weights = weights + lr * labels[i] * data_set[i]
                weights = weights + lr  * data_set[i]
                i = 0
            else:
                i += 1
        self.weight = weights

    def predict(self, data):
        if (self.weight is not None):
            if len(self.weight.shape)==1:
                self.weight=self.weight.reshape(self.weight.shape[0],-1)
                print(self.weight.shape)
            result=np.dot(data, self.weight)
            return np.sign(result)
        else:
            return 0


if __name__ == "__main__":
    iris=datasets.load_iris()
    x=iris.data
    y=iris.target
    dot_num =iris.data.shape[0]

    data_set=np.concatenate([x,y.reshape(-1,1)],axis=1)
    '随机扰乱数据集'
    np.random.shuffle(data_set)
    split_num=140
    perception = Perception()
    #perception = LogisticRegression()
    feature_num=3
    perception.fit(data_set[:split_num, 0:feature_num], data_set[:split_num,-1])
   # print("weights is: ", perception.weight)
   # print("bias is: ", perception.bias)
    y_predict=perception.predict(data_set[split_num:,0:feature_num])
    print(y_predict.reshape(-1),data_set[split_num:,-1])
    y_predict=y_predict.reshape(-1)
    result=[]
    for i in range(dot_num-split_num):
        #print("in for:",y_predict[i])
        #print("in for:",result)

        if y_predict[i]==data_set[split_num:,-1][i]:
            result.append(1)

        else:
            result.append(0)
    print("result:",result)
    print('准确度: %.2f%%' % (100 * np.mean(result)))
    #plt.show()
