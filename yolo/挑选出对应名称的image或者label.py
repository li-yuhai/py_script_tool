
import os
import shutil

"""
  将对应的图片和label放入不同文件夹
"""

# 设置image文件夹和label文件夹的路径
image_folder = 'D:/rice_dataset_5/rice_data_5/images'
label_folder = 'D:/rice_dataset_5/rice_data_5/Annotations'

# 获取image文件夹中的图像文件名（不包含文件扩展名）
image_files = set()
for filename in os.listdir(image_folder):
    if os.path.isfile(os.path.join(image_folder, filename)):
        # 获取文件名（不包含扩展名）
        base_name = os.path.splitext(filename)[0]
        image_files.add(base_name)

# 遍历label文件夹中的文件，如果文件名在image文件夹中存在，则复制到目标文件夹
destination_folder = 'D:/rice_dataset_5/rice_data_5/i_labels'
os.makedirs(destination_folder, exist_ok=True)

for filename in os.listdir(label_folder):
    label_file = os.path.join(label_folder, filename)
    # 获取文件名（不包含扩展名）
    base_name = os.path.splitext(filename)[0]

    # 如果文件名在image文件夹中存在，则复制到目标文件夹
    if base_name in image_files:
        shutil.copy(label_file, os.path.join(destination_folder, filename))

print("已复制匹配的label文件到目标文件夹")


