# -*- coding: UTF-8 -*-
from urllib import request
from urllib import parse

if __name__ == "__main__":
    # 访问网址
    url = 'http://test-member.fx.com/login'
    # 这是代理IP
    proxy = [{'http': '211.94.69.74:8080'}, {'http': '113.128.90.252:48888'}, {'http': '127.0.0.1:8888'}]
    # 创建ProxyHandler
    proxy_support = request.ProxyHandler(proxy[2])
    # 创建Opener
    opener = request.build_opener(proxy_support)
    # 添加User Angent

    values = {'mobile': '18500256896', 'password': '123456'}
    test_data  =parse.urlencode(values).encode('utf-8')

    opener.addheaders = [('application/x-www-form-urlencoded'
                          , 'application/x-www-form-urlencoded'),('for-test','1'),('Accept','text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8')]
    response=opener.open(url,test_data)

   #读取相应信息并解码
    html = response.read().decode("utf-8")
   #打印信息
    print(html)

