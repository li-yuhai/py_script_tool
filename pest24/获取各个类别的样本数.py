import xml.etree.ElementTree as ET
import os

annotation_path = 'D:/projects/obj/Pest24/VOCdevkit/voc2007/Annotations/'
txt_path = 'D:/projects/obj/Pest24/VOCdevkit/voc2007/ImageSets/train.txt'

map_all = {'Rice planthopper': 0, 'Rice Leaf Roller': 0,
           'Striped rice bore': 0, 'Armyworm': 0,
           'Bollworm': 0, 'Meadow borer': 0,
           'Athetis lepigone': 0, 'Spodoptera litura': 0,
           'Spodoptera exigua': 0, 'Stem borer': 0,
           'Little Gecko': 0, 'Plutella xylostella': 0,
           'Spodoptera cabbage': 0, 'Scotogramma trifolii Rottemberg': 0,
           'Yellow tiger': 0, 'Land tiger': 0,
           'eight-character tiger': 0, 'holotrichia oblita': 0,
           'holotrichia parallela': 0, 'Anomala corpulenta': 0,
           'Gryllotalpa orientalis': 0, 'Nematode trench': 0,
           'Agriotes fuscicollis Miwa': 0, 'Melahotus': 0
           }

file_name_txt = open(txt_path)

for line_name in file_name_txt.readlines():
    # 检索出所有的train.xml文件名字
    file_path = annotation_path.strip() + line_name.strip() + ".xml"
    if not os.path.exists(file_path):
        print('no this file : ' + file_path)

    # print(file_path)
    xml_tree = ET.parse(file_path)
    xml_root = xml_tree.getroot()
    for obj in xml_root.iter('object'):
        obj_name = obj.find('name').text
        map_all[obj_name] = map_all[obj_name] + 1



print(map_all)
print(len(map_all))
for name in map_all.keys():
    print(name + ": " + str(map_all[name]))
