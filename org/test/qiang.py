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
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Referer": "http://www.liqiang365.com/pc/html/login.html"
}

req = urllib.request.Request(url, postdata, header)

# 自动记住cookie
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
r = opener.open(req)

jsonobj = json.load(r)
print(jsonobj['resobj']['id'])  # id
print(jsonobj['resobj']['token'])  # token

token = jsonobj['resobj']['token']

list_id = {'7e12aae386e800','fd254248a1d54527931cb46ba6abe3','7e12aae8ad5900','55b71f97713c455f810430f46fd1d0','0a111942fd514c99919d6ec25d7054',
           '3c52d15ab1674c64ab1c98820afc2f','c1867c0ee77045b6af867dbdc7f2a9','ec741725ae574531be0357cfd0a564','7e12aaed744e00','7e12aae6c8f200'}

postdata = urllib.parse.urlencode({
    "courseid": "7e12aae386e800",
    "page": "1",
    "type": "1",
    "updateVersion": "V3.0",
    "version": "V3.0",
    "clientType": "1",
    "token": token,
    "channelType": "pc",
    "channel": "pc"
}).encode('utf-8')

req = urllib.request.Request('https://api.liqiang365.com/video/list', postdata, header)
r1 = opener.open(req)
jsonobj1 = json.load(r1)

result = [(item.get('name', ''), item.get('url1', ''), item.get('url2', ''), item.get('url3', 'NA')) for item in
          jsonobj1['resobj']['rows']]
print(result)

for item in result:
    for i in range(1, 4):
        if '' != item[i]:
            print(item[i])
            print(item)
            do_load_media(item[i],r'e:/liqiang/'+item[0]+'.mp4')
            break


