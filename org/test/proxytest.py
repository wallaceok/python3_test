# -*- coding: UTF-8 -*-
from urllib import request

import  random
if __name__ == "__main__":
    #访问网址
    url = 'http://www.xgyw.cc/html/qiaokehan.html'
    #这是代理IP
    proxy = [{'http':'211.94.69.74:8080'},{'http':'113.128.90.252:48888'}
             ,{'http':'127.0.0.1:8888'}]
    #创建ProxyHandler
    proxy_support = request.ProxyHandler(proxy[2
                                         ])
    #创建Opener
    opener = request.build_opener(proxy_support)
    #添加User Angent
    opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
   #安装OPener
   # request.install_opener(opener)
   #使用自己安装好的Opener
   # response = request.urlopen(url)
   #如果不想安装也可以直接使用opener来执行
    response=opener.open(url)
   #读取相应信息并解码
    html = response.read().decode("utf-8")
   #打印信息
    print(html)