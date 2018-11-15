# -*- coding: UTF-8 -*-


'''
盘客宝 新盘列表访问
'''
import re
from urllib import request

import urllib
import http.cookiejar
import jsonpath
import json
import demjson

import time

url = "http://www.pankebao.com"
data={"id":"13523715133","password":"098123","version":"5.4.3","appType":0,"type":1,"mobileRelease":"8.1.0","channelId":"3548118442517466292","userId":"1148330423733559280","longitude":"113.756252","latitude":"34.767774","deviceType":3}
postdata =urllib.parse.urlencode({
"json":json.dumps(data)
}).encode('utf-8')
header = {
"Content-Type":"application/x-www-form-urlencoded",
"Accept-Encoding":"gzip"
}
req = urllib.request.Request(url+'/rs/user/login',postdata,header)
##print(urllib.request.urlopen(req).read().decode('utf-8'))

#自动记住cookie
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
r = opener.open(req)
#print(r.read().decode('utf-8'))


jsonobj = json.load(r)
#print(jsonobj)

token = jsonpath.jsonpath(jsonobj,'$..session')
#print(token)

token_session = {"session":token[0],"pagination":{"count":10,"page":1},"isShowFiling":True,"hot":"","filter":{"tag_id":3,"selectable":0,"areaId":"2249","size":0},"areaId":2249,"type":0,"price":0}
print(token_session)

postdata1 =urllib.parse.urlencode({
"json":json.dumps(token_session)
}).encode('utf-8')
time.sleep(1)
req = urllib.request.Request(url+'/rs/realty/getRealtyList',postdata1,header)
time.sleep(1)
r = opener.open(req)
print(r.read())
#jsonobj1 = json.loads(r)

#print(jsonobj1)



