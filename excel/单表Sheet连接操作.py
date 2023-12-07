

import pandas as pd


'''
单表Sheet连接操作

'''


# 读取Excel文件，假设文件名为your_file.xlsx
file_path = 'test.xlsx'

# 读取Sheet0和Sheet1的数据
df_sheet0 = pd.read_excel(file_path, sheet_name='Sheet0')
df_sheet1 = pd.read_excel(file_path, sheet_name='Sheet1')

# 假设学号是用来关联的字段，如果不是学号，请替换为实际的关联字段
merged_df = pd.merge(df_sheet0, df_sheet1, on='学号', how='inner')  # 使用学号字段进行内连接合并

# 如果需要保存合并后的数据到新的Excel文件，可以使用以下代码
merged_file = 'merged_file.xlsx'
with pd.ExcelWriter(merged_file) as writer:
    merged_df.to_excel(writer, sheet_name='MergedSheet', index=False)

print("合并完成并保存到", merged_file)


