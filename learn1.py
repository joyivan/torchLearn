import torch
from torch.utils.data import Dataset
from torchvision import datasets
from torchvision.transforms import ToTensor
import matplotlib.pyplot as plt

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
