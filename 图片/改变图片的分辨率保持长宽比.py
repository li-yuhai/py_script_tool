from PIL import Image
import os

def change_resolution_maintaining_aspect_ratio(input_path, output_path, new_width):
    # 打开图像
    with Image.open(input_path) as image:
        # 计算新的高度以保持长宽比
        width_percent = (new_width / float(image.size[0]))
        new_height = int((float(image.size[1]) * float(width_percent)))
        # 改变图像的分辨率
        resized_image = image.resize((new_width, new_height))
        # 保存改变分辨率后的图像
        resized_image.save(output_path, format='JPEG')

# 示例：将图像的宽度改为500像素，并保持长宽比
# input_image_path = 'input_image.jpg'
# output_image_path = 'output_image.jpg'
new_width = 800

# change_resolution_maintaining_aspect_ratio(input_image_path, output_image_path, new_width)

#
# dir_path = 'D:/test/source_test_img/'
# output_path = 'D:/test/t/'
dir_path = './source/'
# output_path = ''
# output_path = 'D:/code/py_tool/图片/test/'
files = os.listdir(dir_path)
for file in files:
    file_path = dir_path + file
    # output_file_path = output_path + file
    print(file_path)
    # print(output_file_path)
    change_resolution_maintaining_aspect_ratio(file_path, file, new_width)

