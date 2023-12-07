

'''
# 分通过txt获取分布的数据集
'''

import shutil
import os
import xml.etree.ElementTree as ET


anno_path = 'D:/dataset/S2TLD/VOCdevkit/VOC2007/Annotations/'
img_path = 'D:/dataset/S2TLD/VOCdevkit/VOC2007/images/'

txt_path = 'D:/dataset/S2TLD/VOCdevkit/VOC2007/ImageSets/val.txt'

out_anno_path = 'D:/test/Annotations/'
out_img_path = 'D:/test/images/'


t = 0
# 读取txt的数据
for line in  open(txt_path, 'r').readlines():
    anno_name = line.strip() + '.xml'
    img_name  = line.strip() + '.jpg'

    anno_file = anno_path + anno_name
    img_file = img_path + img_name

    # 是否存在该标签文件
    if not os.path.exists(anno_file) :
        print('no this file : ' + anno_file)
    # 是否存在该图像文件
    if not os.path.exists(img_file):
        print('no this file : ' + img_file)

    #将标签和图像复制过去
    shutil.copy(anno_file, os.path.join(out_anno_path, anno_name))
    shutil.copy(img_file, os.path.join(out_img_path, img_name))
    t += 1


print("复制成功，总共复制", t)

# pic_map = {}
# instance_map = {}
#
# # 读取txt的数据
# for line in  open(txt_path, 'r').readlines():
#     anno_file = anno_path + line.strip() + '.xml'
#     # 是否存在该文件
#     if not os.path.exists(anno_file):
#         print('no this file : ' + anno_file)
#     xml_tree = ET.parse(anno_file)
#     xml_root = xml_tree.getroot()
#     img_set = set()
#     for obj in xml_root.iter('object'):
#         # obj_index = int(obj.find('name').text)
#         obj_name =obj.find('name').text
#         if not obj_name in instance_map:
#             instance_map[obj_name] = 1
#         else:
#             instance_map[obj_name] += 1
#
#         if not obj_name in img_set:
#             img_set.add(obj_name)
#             if not obj_name in pic_map:
#                 pic_map[obj_name] = 1
#             else:
#                 pic_map[obj_name] += 1
#
#
# aa_pic = {}
# bb_instance = {}
# for key in pic_map.keys():
#     aa_pic[int(key)] = pic_map[key]
#     bb_instance[int(key)] = instance_map[key]
#
#
# sorted_dict = dict(sorted(aa_pic.items()))
# sorted_dict1 = dict(sorted(bb_instance.items()))
# print(sorted_dict)
# print(sorted_dict1)

