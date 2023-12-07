


import os

all_img =  "D:/rice_dataset_5/rice_data_5/images"

# 创建一个文本文件用于存储文件名
output_file = 'train.txt'
val_txt_path = 'D:/rice_dataset_5/rice_data_5/set/val.txt'

val_set = set()
for line in open(val_txt_path, 'r').readlines():
    val_set.add(line.strip())

print(val_set)

# 打开文本文件以写入模式
with open(output_file, 'w') as file:
    # 遍历文件夹中的所有文件和子文件夹
    for f in os.listdir(all_img):
        file_name = f.split('.')[0]
        if file_name not in val_set:
            # 将文件名写入文本文件，每个文件名一行
            file.write(file_name + '\n')

print(f'文件名已经写入到 {output_file}')
