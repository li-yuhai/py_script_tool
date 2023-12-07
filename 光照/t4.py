import os

import cv2
import numpy as np

# 读取图片
img = cv2.imread('extend_0000037.jpg')

# 将图像转换为HSV颜色空间
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 增加饱和度
# hsv[..., 1] = hsv[..., 1] * 1.5
hsv[..., 1] = hsv[..., 1] * 2.0

# 将图像转换回BGR颜色空间
bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

# 显示原始图像和处理后的图像
cv2.imshow('Original Image', img)
cv2.imshow('Increased Saturation Image', bgr)

# 等待按下任意键
cv2.waitKey(0)

# 释放窗口和资源
cv2.destroyAllWindows()

# path = 'D:/projects/Pest24 _improhsv/VOCdevkit/voc2007/images/'
# files = os.listdir(path)
# for file in files:
#     if not file.endswith(".xml"):
#         continue
#     filePath = path + file
#     print(filePath)
#     tree = ET.parse(filePath)
#     root = tree.getroot()
#     for obj in root.iter('object'):
#         name = obj.find('name').text
#         if name not in classes:
#             classes.append(name)
#             print(name)
#

