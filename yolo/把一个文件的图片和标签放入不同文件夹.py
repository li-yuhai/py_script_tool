

"""
把图片放入一个文件夹，xml放入另一个文件夹
"""

import os
import shutil

# 源文件夹路径
source_folder = 'D:/rice_dataset_5/all'

# 目标文件夹路径，用于存放图片
image_folder = 'D:/rice_dataset_5/rice_data_5/images'

# 目标文件夹路径，用于存放XML文件
xml_folder = 'D:/rice_dataset_5/rice_data_5/Annotations'

# 确保目标文件夹存在，如果不存在则创建它们
os.makedirs(image_folder, exist_ok=True)
os.makedirs(xml_folder, exist_ok=True)

# 递归遍历目录并整理文件
def organize_files(source_dir):
    for root, dirs, files in os.walk(source_dir):
        for filename in files:
            source_file = os.path.join(root, filename)

            # 检查文件类型并移动到相应的目标文件夹
            if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp')):
                # 图片文件
                # shutil.move(source_file, os.path.join(image_folder, filename))
                shutil.copy(source_file, os.path.join(image_folder, filename))
            elif filename.lower().endswith('.xml'):
                # XML文件
                # shutil.move(source_file, os.path.join(xml_folder, filename))
                shutil.copy(source_file, os.path.join(xml_folder, filename))

organize_files(source_folder)
print("整理完成")


