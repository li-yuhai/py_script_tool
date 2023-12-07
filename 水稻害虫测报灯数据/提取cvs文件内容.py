

# 筛选的编号为[ 6、7、8、9、10、105、310 ]


# import pandas as pd
#
# # 读取原始 CSV 文件，假设文件名为 your_file.csv
# file_path = 'data.csv'
#
# # 读取 CSV 文件数据
# df = pd.read_csv(file_path)
#
# # 提取虫子编号等于 3 或者等于 5 的行数据
# selected_rows = df[(df['虫子编号'] == 3) | (df['虫子编号'] == 5)]
#
# # 如果需要保存提取后的数据到新的 CSV 文件，可以使用以下代码
# output_file = 'selected_data.csv'
# selected_rows.to_csv(output_file, index=False)
#
# print("虫子编号等于 3 或者等于 5 的行数据已保存到", output_file)


import pandas as pd

# 读取原始 CSV 文件，假设文件名为 your_file.csv
file_path = 'data.csv'

# 读取 CSV 文件数据
df = pd.read_csv(file_path, encoding='gbk')

# 虫子编号集合
target_bug_numbers = {6 ,7, 9, 10, 105, 310}

# 提取虫子编号在集合中的行数据
selected_rows = df[df['虫子编号'].isin(target_bug_numbers)]

# 如果需要保存提取后的数据到新的 CSV 文件，可以使用以下代码
output_file = 'selected_data.csv'
selected_rows.to_csv(output_file, index=False)

print(f"虫子编号在集合 {target_bug_numbers} 中的行数据已保存到", output_file)



