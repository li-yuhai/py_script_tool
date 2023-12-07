#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 06:42:30 2018
@author: pc
"""

"""
用作获取数据集的目标样本的相对尺寸和原图之间的大小对应关系, 将占比百分比写入txt文件中
"""

import os
# from pyecharts.charts import Bar
import os.path
import xml.dom.minidom
import xml.etree.cElementTree as et
from scipy.ndimage import measurements

path = "D:/dataset/S2TLD/VOCdevkit/VOC2007/Annotations"
files = os.listdir(path)
s = []

square_list = []  # 面积数组
side_list = []
sp_list = []  # 占比数组

# =============================================================================
# extensional filename
# =============================================================================
def file_extension(path):
    return os.path.splitext(path)[1]

for xmlFile in files:
    if not os.path.isdir(xmlFile):
        if file_extension(xmlFile) == '.xml':
            # print(os.path.join(path, xmlFile))
            tree = et.parse(os.path.join(path, xmlFile))
            root = tree.getroot()
            filename = root.find('filename').text
            #            print("filename is", path + '/' + xmlFile)
            for Object in root.findall('object'):
                #                name=Object.find('name').text
                #                print("Object name is ", name)
                bndbox = Object.find('bndbox')
                xmin = bndbox.find('xmin').text
                ymin = bndbox.find('ymin').text
                xmax = bndbox.find('xmax').text
                ymax = bndbox.find('ymax').text
                square = (int(ymax) - int(ymin)) * (int(xmax) - int(xmin))
                square_list.append(square)
                #                print(xmin,ymin,xmax,ymax)
                # print(square)
                sp_list.append(float(square) / (1270 * 720))

            for Object in root.findall('size'):
                side1 = Object.find('width').text
                side2 = Object.find('height').text
                side_list.append(int(side1))
                side_list.append(int(side2))
                #                print(xmin,ymin,xmax,ymax)
                # print(square)


print("square is ", square_list)
# print("side_list is", side_list)
print("ss_list is ", sp_list)
sp_list.sort()
with open('output_s1tld.txt', 'w') as f:
    for item in sp_list:
        f.write(str(item) + '\n')

# =============================================================================
# 画出直方图
# =============================================================================
# num = 400  # 最大面积
# histogram1 = measurements.histogram(square_list, 1, num, 10)  # 直方图
# histogram1 = list(map(int, histogram1))  # 转换成 int 格式
# print("histogram is ", histogram1)
#
# bar = Bar("目标面积直方图", "PZ")
# bar.use_theme("light")
# bar.add("数目",
#         [str(num / 10), str(num / 10 * 2), str(num / 10 * 3), str(num / 10 * 4), str(num / 10 * 5), str(num / 10 * 6),
#          str(num / 10 * 7), str(num / 10 * 8), str(num / 10 * 9), str(num / 10 * 10)],
#         histogram1, is_more_utils=True)
# bar.render(r"D:/object_detection/research/object_detection/RED/VOCdevkit/RED/second_chart.html")  # generate HTML file
# # =============================================================================
# # 画出直方图
# # =============================================================================
# num = 1000  # 最大边长
# histogram2 = measurements.histogram(side_list, 1, num, 10)  # 直方图
# histogram2 = list(map(int, histogram2))  # 转换成 int 格式
# print("histogram is ", histogram2)
#
# bar = Bar("图像边长直方图", "PZ")
# bar.use_theme("light")
# bar.add("数目",
#         [str(num / 10), str(num / 10 * 2), str(num / 10 * 3), str(num / 10 * 4), str(num / 10 * 5), str(num / 10 * 6),
#          str(num / 10 * 7), str(num / 10 * 8), str(num / 10 * 9), str(num / 10 * 10)],
#         histogram2, is_more_utils=True)
# bar.render(r"D:/object_detection/research/object_detection/RED/VOCdevkit/RED/third_chart.html")  # generate HTML file
# print("图像搞定")


