# -*- coding: utf-8 -*-
# @File  : PreProcessing.py
# @Author: ddmm
# @Date  : 2020/5/25
# @Desc  : 同步缩放图片（等比例缩放无失真）和xml文件标注的anchor size

import glob
import xml.dom.minidom
import cv2


img = cv2.imread("./demo.jpg")
height, width = img.shape[:2]

# 定义缩放信息 以等比例缩放到416为例
scale=416/height
height=416
width=int(width*scale)

dom = xml.dom.minidom.parse("./demo.xml")
root = dom.documentElement

# 读取标注目标框
objects = root.getElementsByTagName("bndbox")

for object in objects:
    xmin=object.getElementsByTagName("xmin")
    xmin_data=int(float(xmin[0].firstChild.data))
    # xmin[0].firstChild.data =str(int(xmin1 * x))
    ymin =object.getElementsByTagName("ymin")
    ymin_data = int(float(ymin[0].firstChild.data))
    xmax=object.getElementsByTagName("xmax")
    xmax_data = int(float(xmax[0].firstChild.data))
    ymax=object.getElementsByTagName("ymax")
    ymax_data = int(float(ymax[0].firstChild.data))

    # 更新xml
    width_xml=root.getElementsByTagName("width")
    width_xml[0].firstChild.data=width
    height_xml = root.getElementsByTagName("height")
    height_xml[0].firstChild.data = height

    xmin[0].firstChild.data = int(xmin_data*scale)
    ymin[0].firstChild.data = int(ymin_data*scale)
    xmax[0].firstChild.data = int(xmax_data*scale)
    ymax[0].firstChild.data = int(ymax_data*scale)

    # 另存更新后的文件
    with open('demo2.xml', 'w') as f:
        dom.writexml(f, addindent='  ', encoding='utf-8')
    # 测试缩放效果
    img = cv2.resize(img, (width, height))
    # xmin, ymin, xmax, ymax分别为xml读取的坐标信息
    left_top = (int(xmin_data*scale), int(ymin_data*scale))
    right_down= (int(xmax_data*scale), int(ymax_data*scale))
    cv2.rectangle(img, left_top, right_down, (255, 0, 0), 1)

cv2.imwrite("result.jpg",img)
