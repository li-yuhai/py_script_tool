
import os
path = 'D:/dataset/S2TLD（720x1280）/normal_1/JPEGImages/'      # 输入文件夹地址
files = os.listdir(path)   # 读入文件夹
num_png = len(files)       # 统计文件夹中的文件个数
print(num_png)             # 打印文件个数

f = open('val.txt', 'w')
# 输出所有文件名
print("所有文件名:")
for file in files:
    # total = total + len(os.listdir(path + file))
    f.write(file.split('.')[0] + '\n')





