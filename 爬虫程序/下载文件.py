
import openpyxl
import requests
import time

# 打开Excel文件
excel_file = 'Bing水稻细菌性条斑病.xlsx'
workbook = openpyxl.load_workbook(excel_file)
sheet = workbook.active

# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36
header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
}

# 列号和行号，根据你的Excel文件中文件地址的位置进行调整
url_column = 1  # 假设文件地址在第一列
output_directory = 'C:/Users/liyuhai/Downloads/水稻细菌性条斑病/'  # 存放下载文件的目录

for row in sheet.iter_rows(min_row=2, values_only=True):  # 从第2行开始，跳过标题行
    file_url = row[url_column - 1]  # 列索引从0开始
    time.sleep(2)
    response = requests.get(file_url, header)
    if response.status_code == 200:
        # 获取文件名，可以根据文件地址来提取
        timestamp = int(time.time())
        file_name = f"{timestamp}.jpg"
        # file_name = file_url.split("/")[-1]
        file_path = output_directory + file_name

        # 保存文件到指定目录
        with open(file_path, 'wb') as file:
            file.write(response.content)

        print(file_path)

# 关闭Excel文件
workbook.close()


