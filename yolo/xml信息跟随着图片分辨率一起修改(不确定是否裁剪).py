

import xml.etree.ElementTree as ET
import os

def resize_bounding_box(value, original_resolution, new_resolution):
    # 计算缩放比例
    scale_factor_x = new_resolution[0] / original_resolution[0]
    scale_factor_y = new_resolution[1] / original_resolution[1]

    # 调整坐标值
    return int(value * scale_factor_x), int(value * scale_factor_y)


# 读取XML文件
anno_file_path = './Annotations/'
output = os.getcwd() + '/out/'
files = os.listdir(anno_file_path)

for file in files:
    xml_file_path = anno_file_path + file
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    # 原始分辨率和新分辨率
    # original_resolution = (800, 600)
    new_resolution = (800, 600)  # 你想要调整的新分辨率

    # 修改图片分辨率信息
    size_element = root.find(".//size")
    width_element = size_element.find("width")
    height_element = size_element.find("height")

    # 原始分辨率和新分辨率 处理逻辑
    original_resolution = (int(width_element.text), int(height_element.text))

    width_element.text = str(new_resolution[0])
    height_element.text = str(new_resolution[1])

    # 修改每个 <object> 元素中的坐标信息
    for object_element in root.findall(".//object"):
        bndbox_element = object_element.find("bndbox")
        xmin_element = bndbox_element.find("xmin")
        ymin_element = bndbox_element.find("ymin")
        xmax_element = bndbox_element.find("xmax")
        ymax_element = bndbox_element.find("ymax")

        # 调整坐标值
        xmin_value = int(xmin_element.text)
        ymin_value = int(ymin_element.text)
        xmax_value = int(xmax_element.text)
        ymax_value = int(ymax_element.text)

        xmin_value, ymin_value = resize_bounding_box(xmin_value, original_resolution, new_resolution)
        xmax_value, ymax_value = resize_bounding_box(xmax_value, original_resolution, new_resolution)

        # 更新坐标值
        xmin_element.text = str(xmin_value)
        ymin_element.text = str(ymin_value)
        xmax_element.text = str(xmax_value)
        ymax_element.text = str(ymax_value)

    # 保存修改后的XML文件
    tree.write(output + file)
