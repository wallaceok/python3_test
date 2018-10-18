# -*- coding:utf8 -*-
print("程序运行中...")
import re
from urllib import request
import  urllib
import requests
import os
from pprint import pprint
from time import sleep
import random

from bs4 import BeautifulSoup

rooturl = "http://www.xgyw.cc/"

#获取分类连接
def getclass():
    headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
        ,'Host':'www.xgyw.cc','User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'}
    header = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Encoding": "utf-8",
        "Accept-Language": "zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3",
        "Connection": "keep-alive",
        "Host": "www.xgyw.cc",
        "Referer": "http://www.xgyw.cc/",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.90 Safari/537.36 2345Explorer/9.3.2.17331",
        "Upgrade-Insecure-Requests":"1"
    }
    #rec = re.compile('''class=lm10>\<a href="(/\w+/)\"\>(.+)\</a\>''')
    rec = re.compile(r"class=lm10><a href=\"(.+)\" title.*?>(.+)<\/a>")
    try:
        urllib.request.Request(rooturl,headers=header)
        txt = request.urlopen(rooturl).read().decode("gbk")

        #soup = BeautifulSoup(txt)
        #li = soup.find_all("a",class_=re.compile("lm10"))

        fl = rec.findall(txt)
    except Exception as ex :
        print("错误",ex)
        sleep(2)

    print("分类：")
    pprint(fl)
    return fl


fenlei = getclass()  # 下载所有分类下的图片

#只下载推女郎
# fenlei=[getclass()[-1]]
fenlei =[fenlei[2]]

print("推女郎开始下载:"+str(fenlei))

def getpagelist():
    plist = []

    for f, n in fenlei:
        f = f.replace('\"','')
        rec = re.compile('''(/[a-zA-Z]+/page_\d+?\.html)'''.format(f))
        try:
            txt = request.urlopen(rooturl + f).read().decode("gbk")
            t = sorted(set(rec.findall(txt) + [f]))
            plist += t
        except Exception as ex:
            print("错误", ex)
            sleep(3)

    # print("page_list:")
    # pprint(plist)
    return plist


pagelist = getpagelist()
pagelist

def getalbumlist():
    albumlist = []
    for r in pagelist:
        print(rooturl + r)
        try:
            txt = request.urlopen(rooturl + r).read().decode("gbk")
            for x in re.findall(r'''href=(/(\w+)/(\2)\d+.html)''', txt):
                albumlist += [x[0]]
        except Exception as ex:
            print("getalbumlist错误",ex)
            sleep(3)
    return albumlist


albumlist = getalbumlist()


def getfphoto():
    header = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, br-8",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Host": "www.xgyw.cc",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36",
        "Upgrade-Insecure-Requests": "1",
        "Pragma":"no-cache",
        "Cache-Control":"no-cache"
    }

    for r in albumlist:
        try:
            txt = request.urlopen(rooturl + r).read().decode("gbk")
            result = re.findall(r'''(/(\w+)/(\2)\d+_?\d*.html)''', txt)
            result = tuple(set(result))
        except Exception as ex:
            print("错误：",ex)
            sleep(1)

            pass
        for x in result:
            try:
                html = request.urlopen(rooturl + x[0]).read().decode("gbk")
                jpgresult = re.findall('''src=\"(/uploadfile.*?\d+/\w+\.jpg)\"''', html)
                print(jpgresult)
            except Exception as ex:
                print("错误：",ex)
                sleep(1)
            download(jpgresult)
            # for h in jpgresult:
            #     try:
            #         urllib.request.Request(rooturl+ h, headers=header)
            #         request.urlretrieve(rooturl + h, os.path.basename(h))
            #     except Exception as ex:
            #         print("下载错误：",ex)
            #         sleep(3)


def mkdir(path):
    # 引入模块
    import os

    # 去除首位空格
    path = path.strip()
    # 去除尾部 \ 符号
    path = path.rstrip("\\")

    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists = os.path.exists(path)

    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path)

        print(path + ' 创建成功')
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print
        path + ' 目录已存在'
        return False

robot='D:/pic/'
def download(List):
    for url in List:
        try:
            #创建中间目录
            mkdir(robot + url.split('/')[-2])
            #拼路径
            path=robot+url.split('/')[-2]+"/"+url.split('/')[-1]+url.split('/')[-1]+random.randint(0,999999).__str__()
            path = path.replace('.','')+".jpg"
            url=url.replace('\\','')
            r=requests.get(rooturl+url,timeout=30)
            r.raise_for_status()
            r.encoding=r.apparent_encoding
            if not os.path.exists(robot):
                os.makedirs(robot)
            if not os.path.exists(path):
                with open(path,'wb') as f:
                    f.write(r.content)
                    f.close()
                    print(path+' 文件保存成功')
            else:
                print('文件已经存在')
        except Exception as ex:
            print(ex)
            continue

getfphoto()