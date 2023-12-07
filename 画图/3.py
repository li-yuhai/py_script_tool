import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'SimHei'

# 给定两组数据
data1 = [92.1, 83.4, 98.1, 87.7, 84.9, 60.5, 73.4, 50.4, 82, 64.8, 97.5, 55.6 , 9.4, 93, 4.9,
         59.2, 76.6, 11, 59.4, 73.4, 72.9, 64.9 , 77.2, 79.2]

data2 = [92.6, 84.6, 98.1, 88.9, 85.7, 70, 74.5, 56.1, 83.3 , 68.7, 97.7, 58.6, 9.6,
         93.7, 6.1, 63.2, 76.3, 26, 62.5, 73.8 ,75.9, 65.4, 80.3, 81.5]
# [6, 7, 34, 13, 36, 35, 8, 16, 5, 15, 32, 11, 14, 31, 1, 24, 25, 28, 29, 12, 3, 2, 10, 37]
labels = []

names = ['Bollworm', 'Meadow borer', 'Gryllotalpa orientalis', 'Little Gecko', 'Agriotes fuscicollis Miwa', 'Nematode trench',
        'Athetis lepigone', 'Scotogramma trifolii Rottemberg', 'Armyworm', 'Spodoptera cabbage', 'Anomala corpulenta',
        'Spodoptera exigua', 'Plutella xylostella', 'holotrichia parallela', 'Rice planthopper', 'Yellow tiger',
        'Land tiger', 'eight-character tiger', 'holotrichia oblita', 'Stem borer', 'Striped rice bore',
        'Rice Leaf Roller', 'Spodoptera litura', 'Melahotus']

pest24_names =  {
        'Rice planthopper': 1,  'Rice Leaf Roller': 2, 'Striped rice bore':3,  'Armyworm': 5,  'Bollworm' : 6,
        'Meadow borer': 7,  'Athetis lepigone': 8, 'Spodoptera litura': 10,   'Spodoptera exigua': 11,
        'Stem borer':12,  'Little Gecko': 13,  'Plutella xylostella': 14, 'Spodoptera cabbage': 15,
        'Scotogramma trifolii Rottemberg': 16,  'Yellow tiger': 24, 'Land tiger': 25,  'eight-character tiger': 28,
         'holotrichia oblita':29,  'holotrichia parallela': 31,   'Anomala corpulenta': 32, 'Gryllotalpa orientalis': 34,
        'Nematode trench': 35, 'Agriotes fuscicollis Miwa': 36, 'Melahotus': 37
}

for i in names:
    labels.append(int(pest24_names[i]))

print(labels)
# 创建 x 轴的位置信息
# x = np.arange(len(labels))

# 设置每组数据的宽度
# width = 0.35

# 绘制两组数据的柱状图
fig, ax = plt.subplots()
ax.bar(labels, data1, label='数据1')
ax.bar(labels, data2, label='数据2')

#
# rects1 = ax.bar(labels, data1, label='数据1')
# rects2 = ax.bar(labels, data2, label='数据2')

# 添加图例
ax.legend()

# 添加标签和标题

# 在每个柱子的顶部显示数值
# for rect1, rect2 in zip(rects1, rects2):
#     height1 = rect1.get_height()
#     height2 = rect2.get_height()
#     ax.annotate('{}'.format(height1), xy=(rect1.get_x() + rect1.get_width() / 2, height1),
#                 xytext=(0, 3), textcoords="offset points", ha='center', va='bottom')
#     ax.annotate('{}'.format(height2), xy=(rect2.get_x() + rect2.get_width() / 2, height2),
#                 xytext=(0, 3), textcoords="offset points", ha='center', va='bottom')

# 设置横坐标标签
ax.set_xticklabels(labels)

plt.show()
