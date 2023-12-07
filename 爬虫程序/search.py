
import requests
import os

# 在Google开发者控制台创建项目并启用Custom Search API，然后获取API密钥
API_KEY = 'YOUR_API_KEY'
# 在Google Custom Search控制台创建一个搜索引擎，并获取其ID
SEARCH_ENGINE_ID = 'YOUR_SEARCH_ENGINE_ID'

# 要搜索的查询关键字
query = 'your query here'

# 设置搜索结果的起始索引
start = 1

# 设置每个请求返回的结果数量
num = 10

# 创建保存图片的文件夹
os.makedirs(query, exist_ok=True)

# 定义Google Custom Search API的URL
url = f'https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&searchType=image&start={start}&num={num}'

# 发送GET请求
response = requests.get(url)

# 解析JSON响应
data = response.json()

# 下载图片
for item in data['items']:
    try:
        image_url = item['link']
        response = requests.get(image_url)
        image_data = response.content
        with open(os.path.join(query, f'{item["title"]}.jpg'), 'wb') as f:
            f.write(image_data)
    except Exception as e:
        print(f"Error downloading {item['link']}: {str(e)}")

print('Download completed.')

