import os
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'simhei']
# path = r"D:\Personal_Growth\Research_Careers\研一下\pest24-yolov7"
# txt = "pest24_classes.txt"
# imgpath = os.path.join(path, txt)
# classnames = []
# with open(imgpath, 'r', encoding='utf-8') as f:
#     classnames = f.readlines()
#     for i, j in enumerate(classnames):
#         classnames[i] = j.strip()
# f.close()

name = ['稻风虱', '稻纵卷叶螟', '二化螟', '粘虫', '棉铃虫', '草地螟', '二点委夜蛾', '斜纹贪夜蛾', '甜菜夜蛾', '大螟', '小地老虎', '小菜蛾', '甘蓝夜蛾', '三叶草夜蛾',
        '黄地老虎', '大地老虎', '八字地老虎', '华北大黑鳃金甲', '暗黑腮金龟', '铜绿异丽金龟', '东方蝼蛄', '线虫', '细胸金针虫', '褐纹金针虫']
data = [0.0969, 0.705, 0.791, 0.855, 0.94, 0.875, 0.799, 0.818, 0.637, 0.78, 0.907, 0.108, 0.758, 0.723, 0.689,
        0.802, 0.45, 0.689, 0.952, 0.979, 0.986, 0.748, 0.883, 0.804]
my_dict = {}
# 使用 zip() 函数将两个数组合并为一个字典
for k, v in zip(name, data):
    my_dict[k] = v
# 按字典值排序,得到排序后的元组列表
sorted_data = sorted(my_dict.items(), key=lambda item: item[1])
# 将元组列表转换为两个数组
name, values = zip(*sorted_data)
# 设置图像大小
plt.figure(figsize=(12, 8), dpi=150)
# 添加标签
for i, v in enumerate(values):
    plt.text(v, i, str(v), color='black', fontweight='bold', va="center", ha="left", fontsize=12)
# 设置标题、x轴、y轴标签
plt.title('Yolov8x-Pest24', fontsize=20, fontweight='bold')
plt.xlabel('mAP50', fontsize=16)
# plt.ylabel('Label', fontsize=16)
# 打印输出结果
print(sorted_data)
# 画图
plt.matplotlib.rc('font', family='SimHei', weight='bold')
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
# plt.barh(name, values, color="blue", height=0.6)
plt.bar(name, values, color="blue", height=0.6)
plt.show()
