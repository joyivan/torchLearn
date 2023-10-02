import torch
from torch.utils.data import Dataset
from torchvision import datasets
from torchvision.transforms import ToTensor
import matplotlib.pyplot as plt
'''
train_data=datasets.FashionMNIST(root='data',train=True,download=True,\
                                 transform=ToTensor())
test_data=datasets.FashionMNIST(root='data',train=False,download=True,\
                                 transform=ToTensor())
labels_map = {
    0: "T-Shirt",
    1: "Trouser",
    2: "Pullover",
    3: "Dress",
    4: "Coat",
    5: "Sandal",
    6: "Shirt",
    7: "Sneaker",
    8: "Bag",
    9: "Ankle Boot",}
#print(type(train_data))

figure = plt.figure(figsize=(8,8))
cols,rows = 3,3
for i in range(1,cols * rows + 1):
    sample_index = torch.randint(len(train_data),size=(1,)).item() # 获取随机索引
    img,label = train_data[sample_index] # 找到随机索引下的图像和标签
    figure.add_subplot(rows,cols,i) # 增加子图，add_subplot面向对象，subplot面向函数
    plt.title(labels_map[label])
    plt.axis("off") # 关闭坐标轴
    print(img.size())
    print(img.squeeze())

    plt.imshow(img.squeeze(),cmap='gray') # 对图像进行处理,cmap颜色图谱
plt.show() # 显示图像
import os
import pandas as pd
from torchvision.io import read_image
class CustomImageDataset(Dataset):
    def __init__(self,annotations_file,img_dir,transform=None,\
                 target_transform=None):
        super(CustomImageDataset, self).__init__()
        self.img_labels=pd.read_csv(annotations_file)
        self.img_dir=img_dir
        self.transform=transform
        self.target_transform=target_transform
    def __len__(self):
        return len(self.img_labels)
    def __getitem__(self, item):
        img_path=os.path.join(self.img_dir,self.img_labels.iloc[item,0])
        image=read_image()
        label=self.img_labels.iloc[idx,1]
        if self.transform:
            image=self.transform(image)
        if self.target_transform:
            label=self.target_transform(label)
        return image,label
from torch.utils.data import DataLoader
train_dataloader=DataLoader(train_data,batch_size=64,shuffle=True)
test_dataloader=DataLoader(test_data,batch_size=64,shuffle=True)
from torchvision.transforms import ToTensor,Lambda
'''

import os
import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets,transforms
train_data=datasets.FashionMNIST(
    root="data",
    train=True,
    download=True,
    transform=ToTensor()
)
test_data=datasets.FashionMNIST(
    root="data",
    train=False,
    download=True,
    transform=ToTensor()
)
train_dataloader=DataLoader(train_data,batch_size=64)
test_dataloader=DataLoader(test_data,batch_size=64)

device='mps' if torch.backends.mps.is_available() else 'cpu'
print('using {} device'.format(device))

class network(nn.Module):
    def __init__(self):
        super(network,self).__init__()
        self.flatten=nn.Flatten()
        self.layers=nn.Sequential(
            nn.Linear(28*28,512),
            nn.ReLU(),
            nn.Linear(512,512),
            nn.ReLU(),
            nn.Linear(512,10),
            nn.Softmax(1)
        )
    def forward(self,x):
        x=self.flatten(x)
        values=self.layers(x)
        return values
model=network().to(device)
learn_rate=1e-3
batch_size=64
epochs=50
loss_fn=nn.CrossEntropyLoss()
optimizer=torch.optim.SGD(model.parameters(),lr=learn_rate)
def train_loop(dataloader,model,loss_fn,optimizer):

    size=len(dataloader.dataset)
    for number,(x,y) in enumerate(dataloader):
        x=x.to(device)
        y=y.to(device)
        y=torch.nn.functional.one_hot(y, num_classes=10)
        pred=model(x)
       # print(f'pred:{pred}')
       # print(y)
        loss=loss_fn(pred,y.type(torch.float))
       # print('ok')
       # print(f'loss:{loss}')

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if number % 100==0:
            loss,current=loss.item(),number*len(x)
            print(f'loss:{loss:>7f} [{current:>5d}/{size:>5d}]')
def test_loop(dataloader,model,loss_fn):
    size=len(dataloader.dataset)
    num_bater=len(dataloader)
    test_loss,correct=0,0
    with torch.no_grad():
        for x,y in dataloader:
            x=x.to(device)
            y=y.to(device)
            y1 = torch.nn.functional.one_hot(y, num_classes=10)
            pred=model(x)
            pred=pred.to(device)
            test_loss+=loss_fn(pred,y1.type(torch.float)).item()
           # print(pred.size())
           # print(y.size())

            correct+=(pred.argmax(1)==y).type(torch.float).sum().item()
    test_loss/=num_bater
    correct/=size
    print(f'Test Error:\n Accuracy:{(100*correct):>0.1f}%,Avg loss:{test_loss:>8f}')
for t in range(epochs):
    print(f"Epoch {t+1}\n-------------------------------")
    train_loop(train_dataloader, model, loss_fn, optimizer)
    test_loop(test_dataloader, model, loss_fn)
print("Done!")