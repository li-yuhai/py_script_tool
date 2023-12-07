import sys

import xml.etree.ElementTree as ET
import os


'''
# 将数据集中包含该目标害虫的图片挑选出来
'''

# 只需要填写这三个参数
target_name = 'Bollworm'  # 目标害虫的名称
annotation_path = 'D:/dataset/Pest24/VOCdevkit/voc2007/Annotations/' # xml标签文件的路径
picture_path = 'D:/dataset/Pest24/VOCdevkit/voc2007/images/'      # 图片的地址

file_set = set()  # 保存出现target的图片
files = os.listdir(annotation_path)
for file in files:
    file_path = annotation_path.strip() + file
    if not os.path.exists(file_path):
        print('no this file : ' + file_path)

    xml_tree = ET.parse(file_path)
    xml_root = xml_tree.getroot()
    for obj in xml_root.iter('object'):
        obj_name = obj.find('name').text
        if obj_name == target_name:
            file_set.add(file.strip().split(".")[0])
            print(file)
            break

'''
# 将这些照片复制到一个文件夹中并且把labels也复制进去
'''
import shutil
current_directory = os.getcwd()
target_img_path = current_directory + '/images/'
target_label_path = current_directory + '/labels/'

# 创建必要的文件夹
if not os.path.exists(target_img_path):
    os.makedirs(target_img_path)
if not os.path.exists(target_label_path):
    os.makedirs(target_label_path)
else:
    print("文件已经存在了...")
    sys.exit()

print("开始挑选图片：总共有图片：", len(file_set))
# 转移文件, 并且使用新的名字来命名
for item in file_set:
    source_img  = picture_path + item + '.jpg'
    source_anno =  annotation_path + item + '.xml'
    to_img = target_img_path  + item + '.jpg'
    to_label = target_label_path  + item + '.xml'
    shutil.copy(source_img, to_img)
    shutil.copy(source_anno, to_label)


