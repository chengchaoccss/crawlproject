print('这是一个爬虫项目')

import re
import requests
import os

def gethtml(url):
    r=requests.get(url,timeout=7)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    return r.text


def parsehtml(html):
    reg=r'"objURL":"(.*?[jpg|png|jepg])"'
    res=re.findall(reg,html)
    for i in res:
        return i

def downloadpic(i):
    root = ".//pics//"
    path = root + i.split('/')[-1]
    try:
        if not os.path.exists(root):
            os.mkdir(root)
        if not os.path.exists(path):
            r = requests.get(i)
            with open(path, 'wb') as f:
                f.write(r.content)  # r.content为返回内容的二进制表示
                f.close()
                print("文件"+path.split('//')[-1]+"下载完成！")
        else:
            print("文件已存在！")
    except:
        print("爬取失败！")

def main():
    word=input('关键字：')
    num=int(input('下载张数：'))
    for i in range(num):
        url='http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word='+word+'&pn='+str(i)
        html=gethtml(url)
        url=parsehtml(html)
        downloadpic(url)
main()