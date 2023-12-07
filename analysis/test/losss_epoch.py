import csv
import matplotlib.pyplot as plt
import pandas as pd
import numpy  as np
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号
df1 = pd.read_csv("results_yolov5s.csv")   #读取文件1
df2 = pd.read_csv("results_c3x3.csv")   #读取文件2
df3 = pd.read_csv("results_c3x3_carafe.csv")   #读取文件3
df4 = pd.read_csv("results_c3x3_carafe_bifpn.csv")   #读取文件4
df5 = pd.read_csv("results_c3x3_carafe_bifpn_gfpn(8).csv")   #读取文件5

epoch_1 = df1["               epoch"].values.tolist()                     #通过文件表头信息读取文件内容
mAP5_1  = df1["      train/box_loss"].values * 0.4 + df1["      train/obj_loss"].values * 0.3 + df1["      train/cls_loss"].values * 0.3
mAP5_1 = mAP5_1.tolist()

# tolist()
epoch_2 = df2["               epoch"].values.tolist()                     #通过文件表头信息读取文件内容
mAP5_2  = df2["      train/box_loss"].values * 0.4 + df2["      train/obj_loss"].values * 0.3 + df2["      train/cls_loss"].values * 0.3
mAP5_2 = mAP5_2.tolist()

epoch_3 = df3["               epoch"].values.tolist()                     #通过文件表头信息读取文件内容
mAP5_3  = df3["      train/box_loss"].values * 0.4 + df3["      train/obj_loss"].values * 0.3 + df3["      train/cls_loss"].values * 0.3
mAP5_3 = mAP5_3.tolist()

epoch_4 = df4["               epoch"].values.tolist()                     #通过文件表头信息读取文件内容
mAP5_4  = df4["      train/box_loss"].values * 0.4 + df4["      train/obj_loss"].values * 0.3 + df4["      train/cls_loss"].values * 0.3
mAP5_4 = mAP5_4.tolist()

epoch_5 = df5["               epoch"].values.tolist()                     #通过文件表头信息读取文件内容
mAP5_5  = df5["      train/box_loss"].values * 0.4 + df5["      train/obj_loss"].values * 0.3 + df5["      train/cls_loss"].values * 0.3
mAP5_5 = mAP5_5.tolist()

plt.figure(figsize=(8, 5))
plt.plot(epoch_1,mAP5_1,color='blue',  label='YOLOv5s')       #设置曲线相关系数
plt.plot(epoch_2,mAP5_2,color='orange',label='YOLOv5s-a')       #设置曲线相关系数
plt.plot(epoch_3,mAP5_3,color='purple',label='YOLOv5s-ab')       #设置曲线相关系数
plt.plot(epoch_4,mAP5_4,color='green',label='YOLOv5s-abc')       #设置曲线相关系数
plt.plot(epoch_5,mAP5_5,color='red',label='YOLOv5s-CCBG')       #设置曲线相关系数

plt.xticks(fontsize=10)
plt.yticks(fontsize=10)

plt.ylim(0, 0.1)
plt.xlim(0, 200)                        #设置坐标轴取值范围
plt.xlabel('epochs', fontsize=14)
plt.ylabel('mAP_0.5', fontsize=14)
plt.legend(fontsize=12,loc="best") #设置标签位置及大小
plt.savefig("test1.png",bbox_inches='tight')
plt.show()
