import openpyxl
import requests
from PIL import Image
from io import BytesIO
import time

# 打开Excel文件
excel_file = '稻曲病.xlsx'
workbook = openpyxl.load_workbook(excel_file)
sheet = workbook.active

# 列号和行号，根据你的Excel文件中图片地址的位置进行调整
url_column = 1  # 假设图片地址在第一列
output_directory = 'C:/Users/liyuhai/Downloads/daowenbing/'  # 存放下载图片的目录

for row in sheet.iter_rows(min_row=2, values_only=True):  # 从第2行开始，跳过标题行
    image_url = row[url_column - 1]  # 列索引从0开始
    response = requests.get(image_url)
    if response.status_code == 200:
        # 从响应中获取图片内容
        image_content = BytesIO(response.content)
        image = Image.open(image_content)

        # 使用当前时间戳作为唯一的文件名
        timestamp = int(time.time())
        image_name = f"{timestamp}.jpg"
        image_path = output_directory + image_name

        # 保存图片到指定目录
        image.save(image_path)

# 关闭Excel文件
workbook.close()
