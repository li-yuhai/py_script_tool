
"""
根据数据集中图像的名称，将之前数据集的标签文件导入
"""


import sys
import os
import shutil
import xml.etree.ElementTree as ET

img_path = 'D:/test/t/img/'
anno_path = 'D:/test/t/ano/'

extend_name = ''
target_label_path = 'D:/test/t/i/'

files = os.listdir(anno_path)
for file in files:
    # 检索出所有的
    # file_path = img_path.strip() + file.strip()
    file_name = file.split(".")[0]  # 去除文件后缀
    source_img = img_path + file_name + '.jpg'

    if not os.path.exists(source_img):
        print(source_img)
        continue
    to_img = target_label_path + extend_name + file_name + '.jpg'
    shutil.copy(source_img, to_img)




