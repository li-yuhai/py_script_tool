from PIL import Image

# 打开原始图片
original_image_path = 'path/to/your/original/image.jpg'
image = Image.open(original_image_path)

# 计算缩放比例
width, height = 800, 500
aspect_ratio = width / height
original_aspect_ratio = image.width / image.height

if original_aspect_ratio > aspect_ratio:
    new_width = int(height * original_aspect_ratio)
    new_height = height
else:
    new_width = width
    new_height = int(width / original_aspect_ratio)

# 创建缩略图（保持整个图像）
resized_image = image.resize((new_width, new_height))

# 创建一个新的画布
canvas = Image.new("RGB", (width, height), (255, 255, 255))

# 将缩略图粘贴到画布中心
x_offset = (width - new_width) // 2
y_offset = (height - new_height) // 2
canvas.paste(resized_image, (x_offset, y_offset))

# 保存缩放后的图片
output_path = 'path/to/your/output/image_resized.jpg'
canvas.save(output_path)

# 关闭原始图片
image.close()
