
"""
ip102数据集适合分类任务，将不同类别的害虫存放在不同的文件夹中，
xml文件中name是从 0 - 13 这14类害虫
"""

import sys
import os
import shutil
import xml.etree.ElementTree as ET

# 创建文件夹操作
def mkdir(target_path, target_img_path, target_label_path):
    # 创建必要的文件夹
    if not os.path.exists(target_path):
        os.makedirs(target_path)
        os.makedirs(target_img_path)
        os.makedirs(target_label_path)
    else:
        print("文件已经存在了...")
        sys.exit()


name_pic_map = {}
img_path = 'D:/rice_dataset_1/tx_rice_pest_origin/images/'
anno_path = 'D:/rice_dataset_1/tx_rice_pest_origin/i_labels/'

files = os.listdir(anno_path)
for file in files:
    # 检索出所有的
    file_path = anno_path.strip() + file.strip()
    # 跳过不是xml文件的数据
    if not file.endswith(".xml"):
        continue
    if not os.path.exists(file_path):
        print('no this file : ' + file_path)
    file_name = file.split(".")[0]  # 去除文件后缀
    xml_tree = ET.parse(file_path)
    xml_root = xml_tree.getroot()
    image_set = set()
    for obj in xml_root.iter('object'):
        name = obj.find('name').text
        if not name in name_pic_map:
            name_pic_map[name] = set()
        name_pic_map[name].add(file_name)

print(len(name_pic_map))

# 遍历字典的键值对
# for key, value in name_pic_map.items():
#     print(key, value)

out_path = 'D:/rice_dataset_1/test/'


extend_name = ''
for key, value in name_pic_map.items():
    target_img_path = out_path + key + '/images/'
    target_label_path = out_path + key + '/labels/'
    os.makedirs(target_img_path)
    os.makedirs(target_label_path)
    # mkdir(out_path, target_img_path, target_label_path)

    for item in value:
        source_img = img_path + item + '.jpg'
        source_anno = anno_path + item + '.xml'
        to_img = target_img_path + extend_name + item + '.jpg'
        to_label = target_label_path + extend_name + item + '.xml'
        shutil.copy(source_img, to_img)
        shutil.copy(source_anno, to_label)


# # 定义文件夹
# target_path = 'rice/'
# target_img_path = target_path + 'images/'
# target_label_path = target_path + 'labels/'
# extend_name = ''
#
# '''
# # 将这些照片复制到一个文件夹中并且把labels也复制进去
# '''
# t = 0
# with open('fig_name.txt', 'r') as f:
#     lines = f.readlines()
#     for item in lines:
#         t += 1
#         item = item.split(".")[0]
#         source_img = img_path + item + '.jpg'
#         source_anno = anno_path + item + '.xml'
#         to_img = target_img_path + extend_name + item + '.jpg'
#         to_label = target_label_path + extend_name + item + '.xml'
#         shutil.copy(source_img, to_img)
#         shutil.copy(source_anno, to_label)
#
# print(t)

