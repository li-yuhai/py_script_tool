import re  #为了正则表达式
import requests#请求网页url
import os #操作系统
num=0    #给图片加数字
header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36'
}

#图片页面的url
url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&logid=10147541854769187704&ipn=rj&ct=201326592&is=&fp=result&fr=&word=%E7%A8%BB%E6%9B%B2%E7%97%85&queryWord=%E7%A8%BB%E6%9B%B2%E7%97%85&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=1&expermode=&nojc=&isAsync=&pn=60&rn=30&gsm=3c&1696920240008='

#通过requests库请求到了页面
html=requests.get(url,headers=header)

#防止乱码
html.encoding='utf8'

#打印页面出来看看
# print(html.text)

data = html.json()['data']
# print(data)

displayNum = html.json()['displayNum'] # 总共多少记录图片
print(displayNum)
url_list = []
print(len(data))
for i in range(displayNum):
        if 'middleURL' in data[i]:
                mid_pic_url = data[i]['middleURL']
                url_list.append(mid_pic_url)
                print(mid_pic_url)
        else:
                print('no middleURL!')


print(len(url_list))

