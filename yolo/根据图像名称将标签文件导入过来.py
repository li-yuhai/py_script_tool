
"""
根据数据集中图像的名称，将之前数据集的标签文件导入
"""


import sys
import os
import shutil
import xml.etree.ElementTree as ET

img_path = 'D:/test/t/images/'
anno_path = 'D:/test/t/Annotations/'

extend_name = ''
target_label_path = 'D:/test/t/an/'

files = os.listdir(img_path)
for file in files:
    # 检索出所有的
    file_path = anno_path.strip() + file.strip()
    file_name = file.split(".")[0]  # 去除文件后缀
    source_anno = anno_path + file_name + '.xml'
    to_label = target_label_path + extend_name + file_name + '.xml'
    shutil.copy(source_anno, to_label)




