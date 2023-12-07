
import sys
import xml.etree.ElementTree as ET
import os

'''
# 根据名字在txt文件中，将文件进行转移
'''

import shutil
img_path = 'D:/dataset/IP102_Detection/VOC2007/JPEGImages/'
anno_path = 'D:/dataset/IP102_Detection/VOC2007/Annotations/'

# 定义文件夹
target_path = 'rice/'
target_img_path = target_path + 'images/'
target_label_path = target_path + 'labels/'

extend_name = ''

# 创建必要的文件夹
if not os.path.exists(target_path):
    os.makedirs(target_path)
    os.makedirs(target_img_path)
    os.makedirs(target_label_path)
else:
    print("文件已经存在了...")
    sys.exit()

'''
# 将这些照片复制到一个文件夹中并且把labels也复制进去
'''
t = 0
with open('fig_name.txt', 'r') as f:
    lines = f.readlines()
    for item in lines:
        t += 1
        item = item.split(".")[0]
        source_img = img_path + item + '.jpg'
        source_anno = anno_path + item + '.xml'
        to_img = target_img_path + extend_name + item + '.jpg'
        to_label = target_label_path + extend_name + item + '.xml'
        shutil.copy(source_img, to_img)
        shutil.copy(source_anno, to_label)

print(t)


