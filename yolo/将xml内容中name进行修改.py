import shutil
import os
import xml.etree.ElementTree as ET

def changeName(xml_fold, origin_name, new_name):
    '''
    xml_fold: xml存放文件夹
    origin_name: 原始名字，比如弄错的名字，原先要cow,不小心打成cwo
    new_name: 需要改成的正确的名字，在上个例子中就是cow
    '''
    files = os.listdir(xml_fold)
    cnt = 0
    for xmlFile in files:
        file_path = os.path.join(xml_fold, xmlFile)
        dom = ET.parse(file_path)
        root = dom.getroot()
        for obj in root.iter('object'):#获取object节点中的name子节点
            tmp_name = obj.find('name').text
            if tmp_name == origin_name: # 修改
                obj.find('name').text = new_name
                print("change %s to %s." % (origin_name, new_name))
                cnt += 1
        dom.write(file_path, xml_declaration=True)#保存到指定文件
    print("有%d个文件被成功修改。" % cnt)



# D:/rice_dataset_2/3_稻飞虱/labels

xml_fold = "D:/rice_dataset_2/cls/16_稻秆蝇幼虫/i_labels"

changeName(xml_fold, "12", "16")
