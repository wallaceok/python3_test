#coding=utf-8
"""
python抓取性感尤物美女图.py
2016年5月4日 00:51:00 codegay

参考资料: Python3学习笔记（urllib模块的使用）
http://www.cnblogs.com/Lands-ljk/p/5447127.html

以下例子是python2的代码，并且用到lxml,requests 库
我用python3标准库和正则写一个下载全站美女图的程序

使用python来批量抓取网站图片
http://www.cnblogs.com/TeyGao/p/5225940.html
"""
print("程序运行中...")
import re
from urllib import request
import os
from pprint import pprint
from time import sleep

rooturl = "http://www.xgyw.cc/"
# handler=request.ProxyHandler()
# opener=request.build_opener()
# request.install_opener(opener)
#  rec = re.compile('''align=center\>\<a href="(/\w+/)\"\>(.+)\</a\>''')  <a href="[^<>]*?>\w*(.*?)\s*</a>
def getclass():
    rec = re.compile('''<a href="[^<>]*?>\w*(.*?)\s*</a>''')
    try:
        txt = request.urlopen(rooturl).read().decode("gbk")
        fl = rec.findall(txt)
    except Exception as ex:
        print("错误",ex)
        sleep(1)

    print("分类：")
    pprint(fl)
    return fl


fenlei = getclass()  # 下载所有分类下的图片


# fenlei=[getclass()[-1]]#只下载推女郎

def getpagelist():
    plist = []
    for f, n in fenlei:
        rec = re.compile('''({}page_\d+?\.html)'''.format(f))
        try:
            txt = request.urlopen(rooturl + f).read().decode("gbk")
            t = sorted(set(rec.findall(txt) + [f]))
            plist += t
        except Exception as ex :
            print("错误", ex)
            sleep(1)

    # print("page_list:")
    # pprint(plist)
    return plist


pagelist = getpagelist()


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
            sleep(1)
    return albumlist


albumlist = getalbumlist()


def getfphoto():
    for r in albumlist:
        try:
            txt = request.urlopen(rooturl + r).read().decode("gbk")
            result = re.findall(r'''(/(\w+)/(\2)\d+_?\d*.html)''', txt)
            print(result)
        except:
            sleep(1)

            pass
        for x in result:
            try:
                html = request.urlopen(rooturl + x[0]).read().decode("gbk")
                jpgresult = re.findall('''src=\"(/uploadfile.*?\d+/\w+\.jpg)\"''', html)
                print(jpgresult)
            except:
                sleep(1)
            for h in jpgresult:
                try:
                    request.urlretrieve(rooturl + h, os.path.basename(h))
                except:
                    print(3)
                    sleep(1)


getfphoto()