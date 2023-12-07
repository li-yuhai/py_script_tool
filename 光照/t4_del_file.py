import os

import cv2
import numpy as np



# # 读取图片
# img = cv2.imread('extend_0000037.jpg')
# # 将图像转换为HSV颜色空间
# hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# # 增加饱和度
# # hsv[..., 1] = hsv[..., 1] * 1.5
# hsv[..., 1] = hsv[..., 1] * 2.0
# # 将图像转换回BGR颜色空间
# bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)


path = 'D:/projects/Pest24 _improhsv/VOCdevkit/voc2007/images/'
save_path = 'D:/projects/del_image_1.5/'
files = os.listdir(path)
for file in files:
    filePath = path + file

    img = cv2.imread(filePath)
    # 将图像转换为HSV颜色空间
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    # 增加饱和度
    hsv[..., 1] = hsv[..., 1] * 1.5
    # hsv[..., 1] = hsv[..., 1] * 2.0
    bgr = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    cv2.imwrite(save_path + file, bgr)
    print(file)




