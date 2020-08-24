from requests_html import HTMLSession
from requests_html import HTML
import requests
import time
import json
import random
import sys
import os
import csv

from fake_useragent import UserAgent

session = HTMLSession()
url = 'https://car.autohome.com.cn/'
#https://car.autohome.com.cn/config/series/3862.html

USER_AGENTS = [
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10"
]
# 品牌列表
def get_bank():
    response = session.get(url)
    response.html.render()
    banks = response.html.find('.cartree ul li h3')
    for bank in banks:
        #print(bank.text)
        #print(bank.html)
        bk = bank.text
        start = bk.find("(")
        end = bk.find(")")
        print(bk[0:start])
        print(bk[start+1:end])
    print(banks)

# 汽车品牌
def get_url():
    current_dir = os.path.abspath('.')
    print(current_dir)
    file_name = os.path.join(current_dir, "data\\bank.csv")
    print(file_name)
    with open(file_name, 'wt', newline='')  as csvfile1:
        header = ['bank','count', 'url']
        writer = csv.writer(csvfile1)
        writer.writerow(header)
        #访问页面
        response = session.get(url)
        response.html.render()
        banks = response.html.find('.cartree ul li h3 a')
        for bank in banks:
            #print(bank.text)
            #格式化
            bk = bank.text
            start = bk.find("(")
            end = bk.find(")")
            bank1 = bk[0:start]
            Num = bk[(start+1):end]
            url2 = url + bank.attrs.get("href", None)
            print(url2)
            save2csc(writer,bank1,Num,url2)
        #print(banks)
    csvfile1.close()
#
#写入CSV文件
def save2csc(writer,bank,num,url):
        header = ['bank','num' 'url']
        #writer.writerow(header)
        csvrow1 = []
        csvrow1.append(bank)
        csvrow1.append(num)
        csvrow1.append(url)

        writer.writerow(csvrow1)
if __name__ == '__main__':
    print("开始处理")
    get_url()
    #get_bank()
    print("处理结束")


