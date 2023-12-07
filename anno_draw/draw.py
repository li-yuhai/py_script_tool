import os

import cv2
import xml.etree.ElementTree as ET

import matplotlib.pyplot as plt

pest24_names =  {
        'Rice planthopper': 1,  'Rice Leaf Roller': 2, 'Striped rice bore':3,  'Armyworm': 5,  'Bollworm' : 6,
        'Meadow borer': 7,  'Athetis lepigone': 8, 'Spodoptera litura': 10,   'Spodoptera exigua': 11,
        'Stem borer':12,  'Little Gecko': 13,  'Plutella xylostella': 14, 'Spodoptera cabbage': 15,
        'Scotogramma trifolii Rottemberg': 16,  'Yellow tiger': 24, 'Land tiger': 25,  'eight-character tiger': 28,
         'holotrichia oblita':29,  'holotrichia parallela': 31,   'Anomala corpulenta': 32, 'Gryllotalpa orientalis': 34,
        'Nematode trench': 35, 'Agriotes fuscicollis Miwa': 36, 'Melahotus': 37

}
piture_path = 'D:/projects/Pest24_yolov6/VOC2007/val'
anno_path = 'D:/projects/Pest24_index_number/VOCdevkit/voc2007/Annotations'
out_file = 'D:/projects/draw_out'
files = os.listdir(piture_path)
for file in files:
    img=cv2.imread(piture_path + '/' + file)
    anno = anno_path + '/' + file.split('.')[0] + '.xml'

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
        print(name)
        cls  = pest24_names[name]
        font=cv2.FONT_HERSHEY_SIMPLEX  # 定义字体
        imgzi = cv2.putText(img, '{} '.format(cls), (b[0] - 5, a[1] - 5), font, 0.2, (0, 255, 255), 1)
        cv2.rectangle(img, a, b, (0, 0, 255), 2) # -1表示填充所有，1 表示粗细， rgb(162,68,57)

    cv2.imwrite(out_file + '/'+ file , img)


# a=(90,50)#(x1,y1)左上角
# b=(420,300)#(x2,y2)右下角坐标
# cv2.rectangle(img, a, b, (0, 255, 0), 2)
#plt.imshow(img)
#plt.show()
# a='bus'#类别名称
# b=0.9586#置信度
# font=cv2.FONT_HERSHEY_SIMPLEX  # 定义字体
# imgzi = cv2.putText(img, '{} {:.3f}'.format(a,b), (420, 50), font, 0.5, (0, 255, 255), 1)
#                 # 图像，文字内容，坐标(右上角坐标) ，字体，大小，颜色，字体厚度
# cv2.imwrite('./1.jpg',img)
# plt.imshow(img)
#plt.show()


