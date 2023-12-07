

'''
# 分析数据集得到数据集的images、instance这些信息,
'''

import shutil
import os
import xml.etree.ElementTree as ET
# anno_path = 'D:/rice_dataset_5/rice_data_5/Annotations/'
# anno_path = 'D:/test/ricedata_cqcb/Annotations/'
# anno_path = 'D:/lxl_suining_cqcb/lxl_suining_cqcb/10.10-11.5/labels/'
# anno_path = 'D:/test/ricedata_cqcb/Annotations/'
anno_path = '/Users/liyuhai/Desktop/tt_labels/'
files = os.listdir(anno_path)

pic_map = {} # 类别图片数量
instance_map = {} # 类别样本数量

for file in files:
    # 检索出所有的
    file_path = anno_path.strip() + file.strip()

    # 跳过不是xml文件的数据
    if not file.endswith(".xml"):
        continue
    if not os.path.exists(file_path):
        print('no this file : ' + file_path)
        continue


    xml_tree = ET.parse(file_path)
    xml_root = xml_tree.getroot()

    yangben_name_set = set()  # 保证一个文件的多个相同类别样本 不会 造成对pic_map造成影响

    for obj in xml_root.iter('object'):
        obj_name = obj.find('name').text

        # 处理instance的操作逻辑
        if not obj_name in instance_map:
            instance_map[obj_name] = 1
        else:
            instance_map[obj_name] += 1

        if not obj_name in yangben_name_set:
            yangben_name_set.add(obj_name)
            # 处理pic_map的操作
            if not obj_name in pic_map:
                pic_map[obj_name] = 1
            else:
                pic_map[obj_name] += 1


print(pic_map)
print(instance_map)

name_set = set()
for key in pic_map.keys():
    name_set.add(key)

print("样本名称:", len(name_set))
print(name_set)

name_set1 = set()
for key in instance_map.keys():
    name_set1.add(key)

print("样本名称:", len(name_set1))
print(name_set1)
# aa_pic = {}
# bb_instance = {}
# for key in pic_map.keys():
#     aa_pic[int(key)] = pic_map[key]
#     bb_instance[int(key)] = instance_map[key]
#
#
# sorted_dict = dict(sorted(aa_pic.items()))
# sorted_dict1 = dict(sorted(bb_instance.items()))
# print("各个类的图片数量:")
# print(sorted_dict)
# print("各个类的样本数量:")
# print(sorted_dict1)


# print("图片的信息：", pic_map)
# print("实例样本的信息：", instance_map)

# f = zip(sorted_dict.keys(), sorted_dict.values())
# f1 = zip(sorted_dict1.keys(), sorted_dict1.values())
#
# aa = {}
# bb = {}
# a_total = 0
# b_total = 0
# for key in sorted_dict.keys():
#     aa[int(key)] = a[key]
#     bb[int(key)] = b[key]
#     a_total += a[key]
#     b_total += b[key]
#
#
# sorted_dict = dict(sorted(aa.items()))
# sorted_dict1 = dict(sorted(bb.items()))
# print(sorted_dict)
# print(sorted_dict1)
# print("=======================")
# print(a_total)
# print(b_total)

