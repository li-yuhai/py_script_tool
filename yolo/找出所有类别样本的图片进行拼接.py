import os
import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw, ImageFont


# 脚本用途：对一个目标检测数据集，扣出数据集中指定类别的目标，并将目标以3x3的表格形式排列，并显示目标来源图像名称，每9个目标另存为一张大图
# 使用方法：只需要指定图像、标签和新图路径，以及当前需要筛选的类别即可！
# 可更改的：可以自己修改表格形式“3x3”或“10x10”，可以自定义图片名称字体的颜色

def parse_annotation(annotation_path, class_name):
    tree = ET.parse(annotation_path)
    root = tree.getroot()

    boxes = []
    for object in root.iter('object'):
        label = object.find('name').text
        # 扣出数据集中指定类别的目标
        if label == class_name:
            xmlbox = object.find('bndbox')
            b = [int(xmlbox.find('xmin').text), int(xmlbox.find('ymin').text),
                 int(xmlbox.find('xmax').text), int(xmlbox.find('ymax').text)]
            boxes.append((label, b))

       # # 有25个样本示例图就停止运行
        if len(boxes) >= 25:
            return boxes
    return boxes


# 以下分别为需要给定的图像文件夹路径、标签文件夹路径、新生成图片的文件夹路径
# image_dir = r'/Users/liyuhai/Downloads/lxl_suining_cqcb/10.10-11.5/images'
# annotation_dir = r'/Users/liyuhai/Downloads/lxl_suining_cqcb/10.10-11.5/labels'
# new_image_dir = r'/Users/liyuhai/Downloads/lxl_suining_cqcb/10.10-11.5/new_images'

image_dir = r'images'
annotation_dir = r'labels'
new_image_dir = r'new_images'
os.makedirs(new_image_dir, exist_ok=True)

files = os.listdir(annotation_dir)
name_set = set()  # 各个类别的名称
# 读取xml的数据
for file in files:
    anno_file = annotation_dir + '/' + file.strip()
    xml_tree = ET.parse(anno_file)
    xml_root = xml_tree.getroot()
    for obj in xml_root.iter('object'):
        name_set.add(obj.find('name').text)

print(name_set)
print(len(name_set))


parse_annotation
image_names = os.listdir(image_dir)
image_names.sort()

# 使用 for 循环遍历 name_set集合
for class_name in name_set:
    print(class_name)

    objects = []
    for image_name in image_names:
        image_path = os.path.join(image_dir, image_name)
        annotation_path = os.path.join(annotation_dir, image_name.split('.')[0] + '.xml')

        im = Image.open(image_path)
        boxes = parse_annotation(annotation_path, class_name)

        for label, box in boxes:
            obj = im.crop(box)
            draw = ImageDraw.Draw(obj)
            font = ImageFont.truetype("Arial.ttf", 15)
            # 显示目标来源图像的名字，如果需要修改文本颜色，指定color即可
            #draw.text((0, 0), image_name, font=font)
            objects.append(obj)

    for idx in range(0, len(objects), 24):
        width = max([obj.width for obj in objects[idx:idx + 24]])
        height = max([obj.height for obj in objects[idx:idx + 24]])
        big_image = Image.new('RGB', (width * 5, height * 5), (255, 255, 255))

        for i in range(5):
            for j in range(5):
                if idx + i * 5 + j < len(objects):
                    obj = objects[idx + i * 5 + j]
                    big_image.paste(obj, (j * width, i * height))

        big_image.save(os.path.join(new_image_dir, class_name+ '_image_{}.png'.format(idx // 24)))


