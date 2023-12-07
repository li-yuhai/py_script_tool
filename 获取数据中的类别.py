
'''
获取数据中有哪些类别
'''
import xml.etree.ElementTree as ET
import os
# path = 'fire'
# files = os.listdir(path)

classes = []
# path = '/Users/liyuhai/Documents/dataset/pp_smoke/Annotations/'
# path = '/Users/liyuhai/Documents/数据集/roadsign_voc/Annotations/'
path = 'D:/projects/obj/after_Pest24/VOCdevkit/voc2007/Annotations/'
files = os.listdir(path)
print(len(files))

for file in files:
    if not file.endswith(".xml"):
        continue
    filePath = path + file
    print(filePath)
    tree = ET.parse(filePath)
    root = tree.getroot()
    for obj in root.iter('object'):
        name = obj.find('name').text
        if name not in classes:
            classes.append(name)
            print(name)

print(classes)
print(len(classes))


