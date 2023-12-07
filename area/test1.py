#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  3 06:42:30 2018
@author: pc
"""

import os
from pyecharts.charts import Bar
import os.path
import xml.dom.minidom
import xml.etree.cElementTree as et
from scipy.ndimage import measurements


data = []
# 打开文件
with open('output_s1tld.txt', 'r') as f:
    # 逐行读取文件内容并将每行数据添加到列表中
    data = [float(line.strip()) for line in f]
# print(data)

lst = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0,
      1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]

def find_first_greater_index(value):
    for i, num in enumerate(lst):
        if num > value:
            return i
    # 如果没有找到大于给定值的元素，则返回列表的长度
    return len(lst)
res = [0] * 21

for v in data:
    index = find_first_greater_index(v) - 1
    res[index] += 1

print(res)

# res = [23754, 69366, 41535, 25162, 14533, 6391, 3366, 2128, 1598, 1394, 1198, 803, 506, 313, 186, 87, 50, 31, 11, 11, 1]

# s2tld数据集 [11694, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


