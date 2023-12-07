import matplotlib.pyplot as plt
import numpy as np

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'SimHei'


# 给定数据和标签
data = [1, 2, 3, 4]
labels = ['数据1', '数据2', '数据3', '数据4']

# 绘制柱状图
fig, ax = plt.subplots()
ax.bar(labels, data)

# 添加图例
ax.legend(['柱状图'], loc='upper right')

# 添加标签和标题
ax.set_xlabel('数据')
ax.set_ylabel('数值')
ax.set_title('柱状图示例')

plt.show()
