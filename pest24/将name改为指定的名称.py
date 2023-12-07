
import xml.etree.ElementTree as ET
import os

# anno_path = 'D:/test/new/Annotations/'
anno_path = 'D:/lxl_suining_cqcb/lxl_suining_cqcb/10.10-11.5/labels/'
output = os.getcwd() + '/out/'
files = os.listdir(anno_path)
for file in files:
    xml_file_path = anno_path + file
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    # 遍历XML树，修改 <object> 元素的 <name> 子元素
    for object_element in root.findall(".//object"):
        name_element = object_element.find("name")

        if name_element.text == "MLC":
            name_element.text = "Bollworm"

        # if name_element.text == "XCE":
        #     name_element.text = "Plutella xylostella"

    # 保存修改后的XML文件
    tree.write(output + file)
    print(output + file)

