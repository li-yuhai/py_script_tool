

'''
# 分通过txt获取分布的数据集
'''

import shutil
import os
import xml.etree.ElementTree as ET
anno_path = 'D:/rice_pest_1/Annotations/'
txt_path = 'D:/rice_pest_1/ImageSets/test.txt'

files = os.listdir(anno_path)
# instance_num = 17   # 样本的数组
# instance_arr = [0] * instance_num
# images_arr = [0] * instance_num

# pic_map = {'0 BrownSpot': 0, '1 RiceBlast': 0, '2 BacterialBlight': 0, '3 Tungro': 0}
# instance_map = {'0 BrownSpot': 0, '1 RiceBlast': 0, '2 BacterialBlight': 0, '3 Tungro': 0}
pic_map = {}
instance_map = {}

# 读取txt的数据
for line in  open(txt_path, 'r').readlines():
    anno_file = anno_path + line.strip() + '.xml'
    # 是否存在该文件
    if not os.path.exists(anno_file):
        print('no this file : ' + anno_file)
    xml_tree = ET.parse(anno_file)
    xml_root = xml_tree.getroot()
    img_set = set()
    for obj in xml_root.iter('object'):
        # obj_index = int(obj.find('name').text)
        obj_name =obj.find('name').text
        if not obj_name in instance_map:
            instance_map[obj_name] = 1
        else:
            instance_map[obj_name] += 1

        if not obj_name in img_set:
            img_set.add(obj_name)
            if not obj_name in pic_map:
                pic_map[obj_name] = 1
            else:
                pic_map[obj_name] += 1


aa_pic = {}
bb_instance = {}
for key in pic_map.keys():
    aa_pic[int(key)] = pic_map[key]
    bb_instance[int(key)] = instance_map[key]


sorted_dict = dict(sorted(aa_pic.items()))
sorted_dict1 = dict(sorted(bb_instance.items()))
print(sorted_dict)
print(sorted_dict1)


# print(instance_arr)
# print(instance_map)
# print(pic_map)

