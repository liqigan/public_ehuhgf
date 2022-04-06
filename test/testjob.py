import json

import requests as requests
import xlwt #execl操作
from bs4 import BeautifulSoup #网页解析
import urllib.request, urllib.error #获取网页
import re #正则表达式
import sqlite3  #数据库操作
from urllib import parse
from lxml import etree

def main():

    baseUrl='https://search.51job.com/list/060000,000000,0000,00,9,99,Python,2,1.html'
    # html=askURL(baseUrl)
    # print(html)
    getpage(baseUrl)

findname=re.compile(r'"job_name": "(.*?)"')

def askURL(url):
    head={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"
          }#用户代理，反爬
    request=urllib.request.Request(url,headers=head)
    html=""
    try:
        respon=urllib.request.urlopen(request)
        html=respon.read().decode('utf-8')
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)

    return html

def getpage(baseurl):
    data=[]
    a=0
    result = open('BOOS.html', 'r', encoding='gbk')
    soup = BeautifulSoup(result, 'html.parser')
    for item in soup.find_all('script')[7]:
        item=str(item)
        # print(item)
        job_name=re.findall(findname,item)
        # print(job_name)
        data.append(job_name)









if __name__ =="__main__":
     main()
