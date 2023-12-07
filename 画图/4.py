import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
matplotlib.rcParams['font.family'] = 'SimHei'



plt.figure(figsize=(13, 4))
# 构造x轴刻度标签、数据
# labels = ['G1', 'G2', 'G3', 'G4', 'G5']

labels = [6, 7, 34, 13, 36, 35, 8, 16, 5, 15, 32, 11, 14, 31, 1, 24, 25, 28, 29, 12, 3, 2, 10, 37]

first = [92.1, 83.4, 98.1, 87.7, 84.9, 60.5, 73.4, 50.4, 82, 64.8, 97.5, 55.6, 9.4, 93, 4.9,
         59.2, 76.6, 11, 59.4, 73.4, 72.9, 64.9, 77.2, 79.2]

second = [92.5, 84.3, 98.2, 89.1, 85.1, 60.6, 74.8, 54.9, 82.9, 69.4, 97.8, 57.5, 9.0,
         93.6, 5.9, 64.7, 75.2, 25.8, 69.3, 75.3, 74.6, 67.0, 80.1, 82.4]

# third = [21, 31, 37, 21, 28]

# fourth = [26, 31, 35, 27, 21]

#定义函数来显示柱子上的数值
# def autolabel(rects):
#     for rect in rects:
#         height = rect.get_height()
#         plt.text(rect.get_x()+rect.get_width()/2.-0.08, 1.03*height, '%s' % int(height), size=10, family="Times new roman")


def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2.-0.08, 1.03*height, '%s' % height, size=6, family="Times new roman")


# 两组数据
# plt.subplot(131)
x = np.arange(len(labels))  # x轴刻度标签位置
width = 0.25  # 柱子的宽度
# 计算每个柱子在x轴上的位置，保证x轴刻度标签居中
# x - width/2，x + width/2即每组数据在x轴上的位置
c1 = plt.bar(x - width/2, first, width, label='yolov5s' )
# autolabel(c1)
c2 =plt.bar(x + width/2, second, width, label='yolov5s改进')
autolabel(c2)

plt.ylabel('AP')
# plt.title('A')
# x轴刻度标签位置不进行计算
plt.xticks(x, labels=labels)
plt.legend()

# x轴刻度标签位置不进行计算
plt.xticks(x, labels=labels)
plt.legend()
plt.savefig('bar_chart.png', dpi=300, bbox_inches='tight')
plt.show()


