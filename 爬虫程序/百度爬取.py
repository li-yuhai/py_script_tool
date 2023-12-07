import re  #为了正则表达式
import requests#请求网页url
import os #操作系统
num=0    #给图片加数字
header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
        'Cookie':'  ',#这里看你们的浏览器里有没有，你先登录百度账号，才会有的
        'Accept':'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh;q=0.9'
        }  #请求头，谷歌浏览器里面有，具体在哪里找到详见我上一条csdn博客
#图片页面的url
# url='https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&sf=1&fmq=&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&fm=index&pos=history&word=%E5%A4%B4%E5%83%8F'
url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&logid=10147541854769187704&ipn=rj&ct=201326592&is=&fp=result&fr=&word=%E7%A8%BB%E6%9B%B2%E7%97%85&queryWord=%E7%A8%BB%E6%9B%B2%E7%97%85&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=1&expermode=&nojc=&isAsync=&pn=60&rn=30&gsm=3c&1696920240008='



#通过requests库请求到了页面
html=requests.get(url,headers=header)
#防止乱码
html.encoding='utf8'
#打印页面出来看看
print(html.text)

