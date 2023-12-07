

'''
# 分析数据集得到数据集的images、instance这些信息, 因为name是数字，直接使用数组即可
'''

import shutil
import os
import xml.etree.ElementTree as ET
anno_path = 'D:/dataset/ricedata/xml/'
files = os.listdir(anno_path)
t = 0
instance_num = 17
instance_arr = [0] * instance_num
images_arr = [0] * instance_num
for file in files:
    # 检索出所有的
    file_path = anno_path.strip() + file.strip()
    # 跳过不是xml文件的数据
    if not file.endswith(".xml"):
        continue
    if not os.path.exists(file_path):
        print('no this file : ' + file_path)

    xml_tree = ET.parse(file_path)
    xml_root = xml_tree.getroot()
    image_set = set()
    for obj in xml_root.iter('object'):
        obj_index = int(obj.find('name').text)
        # print(obj_index, file)
        instance_arr[obj_index] += 1
        if not file in image_set:
            image_set.add(file)
            images_arr[obj_index] += 1

print(instance_arr)
print(images_arr)

