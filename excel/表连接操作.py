
import pandas as pd
'''
将两个表通过字段进行连接后生成新的表

'''

# 读取表A和表B的Excel文件
file_a = 'table_a.xlsx'
file_b = 'table_b.xlsx'

# 读取表A和表B的数据
df_a = pd.read_excel(file_a)
df_b = pd.read_excel(file_b)

# 假设学号是用来关联的字段，如果不是学号，请替换为实际的关联字段
merged_df = pd.merge(df_a, df_b, on='学号', how='inner')  # 使用学号字段进行内连接合并

# 如果需要保存合并后的数据到新的Excel文件，可以使用以下代码
merged_file = 'merged_table.xlsx'
merged_df.to_excel(merged_file, index=False)

print("合并完成并保存到", merged_file)

