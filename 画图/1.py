import matplotlib.pyplot as plt

import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family'] = 'SimHei'


# 给定数据
data = [1511, 1240, 1285, 8880, 28014, 16516, 30339, 1951, 7263, 1804, 4279, 953,
        2304, 4679, 1686, 475, 168, 108, 11675, 53347, 6528, 167, 6484, 768]


labels = ['1', '2', '3', '5', '6', '7', '8',
          '10', '11', '12', '13', '14', '15', '16',
          '24', '25', '28', '29', '31',
          '32', '34', '35', '36', '37' ]


# 设置 x 轴刻度标签
# labels = ['稻飞虱', '稻纵卷叶螟', '二化螟', '粘虫', '棉铃虫', '草地螟', '二点委夜蛾', '斜纹贪夜蛾',
#           '甜菜夜蛾', '大螟', '小地老虎', '小菜蛾', '甘蓝夜蛾', '三叶草夜蛾', '黄地老虎',
#           '大地老虎', '八字地老虎', '华北大黑鳃金甲', '暗黑腮金龟', '铜绿异丽金龟',
#           '东方蝼蛄', '线虫', '细胸金针虫', '褐纹金针虫' ]

pest24_names =  {
        'Rice planthopper': 1,  'Rice Leaf Roller': 2, 'Striped rice bore':3,  'Armyworm': 5,  'Bollworm' : 6,
        'Meadow borer': 7,  'Athetis lepigone': 8, 'Spodoptera litura': 10,   'Spodoptera exigua': 11,
        'Stem borer':12,  'Little Gecko': 13,  'Plutella xylostella': 14, 'Spodoptera cabbage': 15,
        'Scotogramma trifolii Rottemberg': 16,  'Yellow tiger': 24, 'Land tiger': 25,  'eight-character tiger': 28,
         'holotrichia oblita':29,  'holotrichia parallela': 31,   'Anomala corpulenta': 32, 'Gryllotalpa orientalis': 34,
        'Nematode trench': 35, 'Agriotes fuscicollis Miwa': 36, 'Melahotus': 37

}


# 旋转横坐标标签
# plt.xticks(rotation=75)

# 在柱子顶部显示数值
for i, v in enumerate(data):
    plt.text(i, v, str(v), color='black', fontweight='bold', va="bottom", ha="center", fontsize=7)


# 保存图像
# plt.savefig('bar_chart.jpg', dpi=300, bbox_inches='tight')


plt.bar(labels, data)

# 显示图形
plt.show()


