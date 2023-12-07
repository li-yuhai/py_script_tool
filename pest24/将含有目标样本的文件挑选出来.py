import sys

import xml.etree.ElementTree as ET
import os


'''
# 在训练集中将'Rice planthopper'的文件挑选出来，来做数据扩充，增加样本数目
'''


target_name = 'Athetis lepigone'
target_dir_name = 'Athetis lepigone'
extend_name = 'Athetis lepigone'

annotation_path = 'D:/projects/Pest24_index_number/VOCdevkit/voc2007/Annotations/'
txt_path = 'D:/projects/Pest24_index_number/VOCdevkit/voc2007/ImageSets/train.txt'
file_name_txt = open(txt_path)

# map_all = {'Rice planthopper': 0, 'Rice Leaf Roller': 0,
#            'Striped rice bore': 0, 'Armyworm': 0,
#            'Bollworm': 0, 'Meadow borer': 0,
#            'Athetis lepigone': 0, 'Spodoptera litura': 0,
#            'Spodoptera exigua': 0, 'Stem borer': 0,
#            'Little Gecko': 0, 'Plutella xylostella': 0,
#            'Spodoptera cabbage': 0, 'Scotogramma trifolii Rottemberg': 0,
#            'Yellow tiger': 0, 'Land tiger': 0,
#            'eight-character tiger': 0, 'holotrichia oblita': 0,
#            'holotrichia parallela': 0, 'Anomala corpulenta': 0,
#            'Gryllotalpa orientalis': 0, 'Nematode trench': 0,
#            'Agriotes fuscicollis Miwa': 0, 'Melahotus': 0
#            }

file_set = set()  # 保存出现target的图片
for line_name in file_name_txt.readlines():
    # 检索出所有的train.xml文件名字
    file_path = annotation_path.strip() + line_name.strip() + ".xml"
    if not os.path.exists(file_path):
        print('no this file : ' + file_path)

    xml_tree = ET.parse(file_path)
    xml_root = xml_tree.getroot()
    for obj in xml_root.iter('object'):
        obj_name = obj.find('name').text
        if obj_name == target_name:
            file_set.add(line_name.strip())

# 打印出现照片的信息
print(len(file_set))
print(file_set)

'''
# 将这些照片复制到一个文件夹中并且把labels也复制进去
'''
import shutil
img_path = 'D:/projects/Pest24_index_number/VOCdevkit/images/train/'
anno_path = 'D:/projects/Pest24_index_number/VOCdevkit/voc2007/Annotations/'

target_path = 'D:/projects/' + target_dir_name +'/'
target_img_path = target_path + 'images/'
target_label_path = target_path + 'labels/'

# 创建必要的文件夹
if not os.path.exists(target_path):
    os.makedirs(target_path)
    os.makedirs(target_img_path)
    os.makedirs(target_label_path)
else:
    print("文件已经存在了...")
    sys.exit()

# 转移文件, 并且使用新的名字来命名
for item in file_set:
    source_img  = img_path + item + '.jpg'
    source_anno =  anno_path + item + '.xml'
    to_img = target_img_path + extend_name + item + '.jpg'
    to_label = target_label_path + extend_name + item + '.xml'
    shutil.copy(source_img, to_img)
    shutil.copy(source_anno, to_label)


