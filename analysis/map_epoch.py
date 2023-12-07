import csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy  as np
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号
df1 = pd.read_csv("yolov5s.csv")   #读取文件1
df2 = pd.read_csv("yolov5m.csv")   #读取文件1
df3 = pd.read_csv("carafe.csv")   #读取文件2
df4 = pd.read_csv("carafe-bifpn.csv")   #读取文件2
df5 = pd.read_csv("c2f.csv")   #读取文件4

epoch_1 = df1["               epoch"].values.tolist()                     #通过文件表头信息读取文件内容
mAP5_1  = df1["     metrics/mAP_0.5"].values.tolist()

epoch_2 = df2["               epoch"].values.tolist()                     #通过文件表头信息读取文件内容
mAP5_2  = df2["     metrics/mAP_0.5"].values.tolist()

epoch_3 = df3["               epoch"].values.tolist()                     #通过文件表头信息读取文件内容
mAP5_3  = df3["     metrics/mAP_0.5"].values.tolist()

epoch_4 = df4["               epoch"].values.tolist()                     #通过文件表头信息读取文件内容
mAP5_4  = df4["     metrics/mAP_0.5"].values.tolist()

epoch_5 = df5["               epoch"].values.tolist()                     #通过文件表头信息读取文件内容
mAP5_5  = df5["     metrics/mAP_0.5"].values.tolist()

plt.figure(figsize=(8, 5))
plt.plot(epoch_1,mAP5_1,color='red',  label='yolov5s')       #设置曲线相关系数
plt.plot(epoch_2,mAP5_2,color='orange',label='yolov5m')       #设置曲线相关系数
plt.plot(epoch_3,mAP5_3,color='yellow',label='carafe')       #设置曲线相关系数
plt.plot(epoch_4,mAP5_4,color='green',label='carafe-bifpn')       #设置曲线相关系数
plt.plot(epoch_5,mAP5_5,color='black',label='c2f')       #设置曲线相关系数

plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

plt.ylim(0, 0.75)
plt.xlim(0, 200)                        #设置坐标轴取值范围
plt.xlabel('epochs', fontsize=14)
plt.ylabel('mAP_0.5', fontsize=14)
plt.legend(fontsize=12,loc="best") #设置标签位置及大小
plt.savefig("test1.png",bbox_inches='tight')
plt.show()
