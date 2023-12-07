

import os

folder_path = 'D:/lxl_suining_cqcb/zhenghe_pest24_suining/i1'

# 遍历文件夹中的文件
for filename in os.listdir(folder_path):
    old_filepath = os.path.join(folder_path, filename)

    # 如果是文件而不是文件夹
    if os.path.isfile(old_filepath):
        # 去除文件名中的空格
        new_filename = filename.replace(" ", "_")

        # 构造新的文件路径
        new_filepath = os.path.join(folder_path, new_filename)

        # 重命名文件
        os.rename(old_filepath, new_filepath)
        print(f"文件 {filename} 重命名为 {new_filename}")


