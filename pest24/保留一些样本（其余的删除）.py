import xml.etree.ElementTree as ET
import  os


# 要保留的对象名称列表
objects_to_keep_names = ["Plutella xylostella", "Rice planthopper", "eight-character tiger"]

anno_path = 'D:/lxl_suining_cqcb/Pest24/Annotations/'
output = os.getcwd() + '/out/'
files = os.listdir(anno_path)
for file in files:
    xml_file_path = anno_path + file
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    # 遍历XML树，删除不符合条件的<object>元素
    for object_element in root.findall(".//object"):
        name_element = object_element.find("name")

        if name_element is not None and name_element.text not in objects_to_keep_names:
            # 删除不符合条件的 <object> 元素
            root.remove(object_element)

    # 保存修改后的XML文件
    tree.write(output + file)
    print(output + file)



