

# 打开文本文件
with open('mobileNetv3', 'r') as file:
    # 逐行读取文件内容
    lines = file.readlines()

# 用列表推导式筛选以'['开头的行
filtered_lines = [line for line in lines if line.startswith('[')]

# 打印筛选结果
for line in filtered_lines:
    print(line.strip())
