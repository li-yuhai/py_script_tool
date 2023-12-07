import os
import cv2
import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

"""
将xml的标注信息显示在框上
"""

piture_path = 'D:/test/t/images/1.jpg'
anno = 'D:/code/py_tool/anno_draw/rice_leaf_roller_random_20.xml'
out_file = 'D:/code/py_tool/anno_draw'
img=cv2.imread(piture_path)

xml_tree = ET.parse( anno )
xml_root = xml_tree.getroot()
for obj in xml_root.iter('object'):
    obj_name = obj.find('bndbox').text
    a1 = int(obj.find('bndbox').find('xmin').text)
    a2 = int(obj.find('bndbox').find('ymin').text)
    b1 = int(obj.find('bndbox').find('xmax').text)
    b2 = int(obj.find('bndbox').find('ymax').text)
    a = (a1, a2)
    b = (b1, b2)
    name = obj.find('name').text
    cls = name  # 直接将name显示在标注框上
    font=cv2.FONT_HERSHEY_SIMPLEX  # 定义字体
    imgzi = cv2.putText(img, '{} '.format(cls), (b[0] - 5, a[1] - 5), font, 0.2, (0, 255, 255), 1)
    cv2.rectangle(img, a, b, (0, 0, 255), 3) # -1表示填充所有，1 表示粗细， rgb(162,68,57)

# cv2.imwrite(out_file + '/' + 'test.jpg', img)

#======= 显示图片
cv2.imshow('img' ,img)
cv2.waitKey(0)
cv2.destroyAllWindows()