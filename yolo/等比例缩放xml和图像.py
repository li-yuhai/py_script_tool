import math
import xml.etree.ElementTree as ET  # 导入xml模块
import pickle
import os
from os import listdir, getcwd
from os.path import join
from PIL import Image
import glob

'''
xml_dir:xml文件所在的路径
out_dir:xml文件输出的路径
img_w:resize后的图片宽
img_h:resize后的图片高
xml_index:xml文件的索引(用于文件命名)
'''


def xml2xml(xml_dir, out_dir, img_w, img_h, xml_name):
    xml_file = open(xml_dir)
    xml = ET.parse(xml_file)
    # 获取原图的长宽
    old_w = float(xml.find('size').find('width').text)
    old_h = float(xml.find('size').find('height').text)
    # 更改长宽
    xml.find('size').find('width').text = str(img_w)
    xml.find('size').find('height').text = str(img_h)
    # 图片缩小倍数
    factor_x = img_w / old_w
    factor_y = img_h / old_h

    for obj in xml.iter('object'):
        # 原始 bobox 左上和右下坐标
        xmin = float(obj.find('bndbox').find('xmin').text)
        ymin = float(obj.find('bndbox').find('ymin').text)
        xmax = float(obj.find('bndbox').find('xmax').text)
        ymax = float(obj.find('bndbox').find('ymax').text)

        # 更改图片尺寸之后的 bbox 左上和右下坐标
        obj.find('bndbox').find('xmin').text = str(math.ceil(xmin * factor_x))
        obj.find('bndbox').find('ymin').text = str(math.ceil(ymin * factor_y))
        obj.find('bndbox').find('xmax').text = str(math.ceil(xmax * factor_x))
        obj.find('bndbox').find('ymax').text = str(math.ceil(ymax * factor_y))
        # Labelplot=((str(xmin/factor_x),str(ymin/factor_y)),(str(xmax/factor_x),str(ymax/factor_y)))
    # xml_index = str('%08d' % xml_index)
    xml.write(os.path.join(out_dir) + xml_name)  # 保存到另一个目录
    xml_file.close()
    # print("%s更改成功\n" % xml_dir)


def main():
    filepath = 'Annotations/'  # xml的路径
    out_dir = 'out/'
    # 读取XML文件
    files = os.listdir(filepath)
    for file in files:
        xml_file_path = filepath + file
        xml2xml(xml_file_path, out_dir, img_w=800, img_h=600, xml_name=file)


if __name__ == '__main__':
    main()

