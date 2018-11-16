# -*- coding: UTF-8 -*-
import re
from urllib import request
from urllib.request import urlretrieve
import requests
import urllib
import http.cookiejar
import os
import json
import random
import time


def report(a, b, c):
    '''
    a:已经下载的数据块
    b:数据块的大小
    c:远程文件的大小
    '''
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    print('%.2f%%' % per)

def do_load_media(url, path):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.3.2.1000 Chrome/30.0.1599.101 Safari/537.36"}
        pre_content_length = 0
        # 循环接收视频数据
        while True:
            # 若文件已经存在，则断点续传，设置接收来需接收数据的位置
            if os.path.exists(path):
                headers['Range'] = 'bytes=%d-' % os.path.getsize(path)
            res = requests.get(url, stream=True, headers=headers)

            content_length = int(res.headers['content-length'])
            # 若当前报文长度小于前次报文长度，或者已接收文件等于当前报文长度，则可以认为视频接收完成
            if content_length < pre_content_length or (
                    os.path.exists(path) and os.path.getsize(path) == content_length):
                break
            pre_content_length = content_length

            # 写入收到的视频数据
            with open(path, 'ab') as file:
                file.write(res.content)
                file.flush()
                print('receive data，file size : %d   total size:%d' % (os.path.getsize(path), content_length))
    except Exception as e:
        print(e)

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
        print(path + ' 目录已存在')
        return False

url = "https://api.liqiang365.com/login/in.ph"
postdata = urllib.parse.urlencode({
    "account": "13523715133",
    "password": "a123456a",
    "oneType": "0",
    "updateVersion": "V3.0",
    "version": "V3.0",
    "clientType": "1"
}).encode('utf-8')
header = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:45.0) Gecko/20100101 Firefox/45.0",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8"
}

req = urllib.request.Request(url, postdata, header)

# 自动记住cookie
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
r = opener.open(req)

jsonobj = json.load(r)
# print(jsonobj['resobj']['id'])  # id
# print(jsonobj['resobj']['token'])  # token
# uid = jsonobj['resobj']['id']

token = jsonobj['resobj']['token']

#类别id
list_id = {'7e128a91092000','7e128a914b1500','7e128a929d0e00','7e12aa958cc500'}


#课程类型数据
class_c = []
# 类目下的所有课程id和总条数转换成数组

header1 = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Accept-Encoding":"gzip, deflate, br",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.90 Safari/537.36 2345Explorer/9.5.0.17997",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Referer":"http://www.liqiang365.com/pc/html/new_shipin.html",
    "Host":"api.liqiang365.com",
    "Origin":"http://www.liqiang365.com"
}
for l in list_id:
    postdata1 = urllib.parse.urlencode({
        "page":"1",
        "id": l,
        "type": "1",
        "updateVersion": "V3.0",
        "version": "V3.0",
        "clientType": "1",
        "token": token,
        "channelType": "pc",
        "channel": "pc"
    }).encode('utf-8')

    #获取总页数，然后进行分页循环获取所有视频
    req_count = urllib.request.Request('https://api.liqiang365.com/videocourse/list',postdata1,header1)
    r0 = opener.open(req_count)
    countobj = json.load(r0)

    #1、课程名字 2、课程id 3、视频总个数
    class_c = class_c + [(item.get('name', ''), item.get('id', ''),
                        item.get('videocount', '')) for item in
                       countobj['resobj']['rows']]


print(type(class_c))



#所有视频连接类型和名称
result =[]
num_n = 1
for c in class_c:
    count_num = int(c[2]/10+2)
    for j in range(1,count_num):
        postdata2 = urllib.parse.urlencode({
            "courseid": c[1],
            "page":j,
            "type": "1",
            "updateVersion": "V3.0",
            "version": "V3.0",
            "clientType": "1",
            "token": token,
            "channelType": "h5",
            "channel": "h5"
        }).encode('utf-8')
        #获取每页的视频
        req = urllib.request.Request('https://api.liqiang365.com/video/list', postdata2, header)
        r1 = opener.open(req)
        jsonobj1 = json.load(r1)
        print(jsonobj1)
        result= result+[(str(num_n)+item.get('name', '').replace('(','').replace(')',''), item.get('url1', ''), item.get('url2', ''), item.get('url3', 'NA')) for item in
                  jsonobj1['resobj']['rows']]
    num_n=num_n+1
print(result)
print(len(result))
for item in result:
    for i in range(1, 4):
        if '' != item[i]:
            print(item[i])
            print(item)
            do_load_media(item[i],r'e:/liqiang/'+item[0]+'.mp4')
            break
