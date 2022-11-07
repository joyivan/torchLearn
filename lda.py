import numpy as np
# define class of LDA
class LDA():
    def __init__(self):
        self.W=None
    def caculate_covariance_matrix(self,X):
        X=X-np.mean(X,axis=0)
        return np.matmul(X.T,X)
    def fit(self,X,y):
        # divide matrix X into 0/1 classes
        X0=X[y==0]
        X1=X[y==1]
        # sigma U
        sigma0=self.caculate_covariance_matrix(X0)
        sigma1=self.caculate_covariance_matrix(X1)
        print('sigma1 shape:',sigma1.shape)
        u0=np.mean(X0,axis=0)
        u1=np.mean(X1,axis=0)
        # within-class scatter matrix
        Sw=sigma0+sigma1
        # mean difference
        mean_diff=np.atleast_1d(u0-u1)
        #  take the SVD of Sw and invert it
        U,S,V=np.linalg.svd(Sw)
        inv_Sw=np.dot(np.dot(V.T,np.linalg.pinv(np.diag(S))),U.T)
        # solve the matrix W
        self.W=inv_Sw.dot(mean_diff)
    def pred(self,X):
        y_pred=[]
        u=np.mean(X.dot(self.W))
        for x_i in X:
            h=x_i.dot(self.W)
            if h>=u:
                y=0
            else:
                y=1
            y_pred.append(y)
        return y_pred
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
data=datasets.load_iris()
X=data.data
y=data.target
X=X[y!=2]
y=y[y!=2]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
print('X_train=',X_train)
print('X_train.shape',X_train.shape)
print('y_train=',y_train)
print('y_train.shape',y_train.shape)
print('X_test=',X_test)
print('X_test.shape',X_test.shape)
print('y_test=',y_test)
print('y_test.shape',y_test.shape)
lda=LDA()
lda.fit(X_train,y_train)
print('W=',lda.W)
y_pred=lda.pred(X_test)
print('y_pred=',y_pred)
Acc=accuracy_score(y_test,y_pred)
print('accuracy of LDA:',Acc)
