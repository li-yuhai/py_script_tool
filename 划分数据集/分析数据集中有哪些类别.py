

'''
# 通过分析数据集中的xml文件，得到有哪些类别
'''

import shutil
import os
import xml.etree.ElementTree as ET

anno_path = 'D:/rice_pest/anno/'

files = os.listdir(anno_path)
name_set = set()

# 读取txt的数据
for file in files:
    anno_file = anno_path + file.strip()
    xml_tree = ET.parse(anno_file)
    xml_root = xml_tree.getroot()
    for obj in xml_root.iter('object'):
        name_set.add(obj.find('name').text)

print(name_set)
name_set = {'15', '12', '13', '11', '1', '7', '10', '16', '9', '6', '14', '8', '2', '5'}
sorted(name_set)
print(name_set)

