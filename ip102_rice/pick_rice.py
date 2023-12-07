
import sys
import xml.etree.ElementTree as ET
import os

'''
# 数据集中把水稻虫害的图像挑选出来, 名字存放在txt文件中
'''

target_name = 'Athetis lepigone'
target_dir_name = 'Athetis lepigone'
extend_name = 'Athetis lepigone'

annotation_path = 'D:/dataset/IP102_Detection/VOC2007/Annotations/'


# 打开文件，如果文件不存在则创建
txt_file = open("fig_name.txt", "w")

# 水稻虫害的索引下标
index_name = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
f_arr = [0] * 14

# 获取标签文件夹下所有的标签文件
files = os.listdir(annotation_path)

total = 0

for file in files:
    # 检索出所有的
    file_path = annotation_path.strip() + file.strip()
    # 跳过不是xml文件的数据
    if not file.endswith(".xml"):
        continue
    if not os.path.exists(file_path):
        print('no this file : ' + file_path)
    # print(file_path)
    xml_tree = ET.parse(file_path)
    xml_root = xml_tree.getroot()
    for obj in xml_root.iter('object'):
        obj_index = int( obj.find('name').text)
        if obj_index in index_name:
            txt_file.write(file)
            txt_file.write("\n")
            total += 1
            f_arr[obj_index] += 1

# 打印满足要求的数量
print(total)

print(f_arr)
# 关闭文件
txt_file.close()




# '''
# # 将这些照片复制到一个文件夹中并且把labels也复制进去
# '''
# import shutil
# img_path = 'D:/projects/Pest24_index_number/VOCdevkit/images/train/'
# anno_path = 'D:/projects/Pest24_index_number/VOCdevkit/voc2007/Annotations/'
#
# target_path = 'D:/projects/' + target_dir_name +'/'
# target_img_path = target_path + 'images/'
# target_label_path = target_path + 'labels/'
#
# # 创建必要的文件夹
# if not os.path.exists(target_path):
#     os.makedirs(target_path)
#     os.makedirs(target_img_path)
#     os.makedirs(target_label_path)
# else:
#     print("文件已经存在了...")
#     sys.exit()
#
# # 转移文件, 并且使用新的名字来命名
# for item in file_set:
#     source_img  = img_path + item + '.jpg'
#     source_anno =  anno_path + item + '.xml'
#     to_img = target_img_path + extend_name + item + '.jpg'
#     to_label = target_label_path + extend_name + item + '.xml'
#     shutil.copy(source_img, to_img)
#     shutil.copy(source_anno, to_label)


