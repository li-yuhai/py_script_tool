from PIL import Image

def change_resolution(input_path, output_path, new_width, new_height):
    # 打开图像
    with Image.open(input_path) as image:
        # 改变图像的分辨率
        resized_image = image.resize((new_width, new_height))
        # 保存改变分辨率后的图像
        resized_image.save(output_path)

# 示例：将图像的分辨率改为新的宽度为500像素，高度为300像素
input_image_path = 'input_image.jpg'
output_image_path = 'output_image.jpg'
new_width = 500
new_height = 300

change_resolution(input_image_path, output_image_path, new_width, new_height)
