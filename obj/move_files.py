# -*- coding:UTF-8 -*-
import shutil

f_txt = open('D:/projects/Pest24_index_number/VOCdevkit/voc2007/ImageSets/Main/train.txt', 'r')
f_train = 'D:/dataset/VOCdevkit/VOC2007/train'

context = list(f_txt)
for imagename in context:
    imagename = imagename[0:6]
    imagename = imagename + '.jpg'
    imagepath = 'D:/projects/Pest24_index_number/VOCdevkit/voc2007/images/'+ imagename
    shutil.copy(imagepath,f_train)
    # 删除训练集和验证集，剩余图片为测试集
    # os.remove(imagepath)

#处理Annotations同理只需将.jpg改为.xml

