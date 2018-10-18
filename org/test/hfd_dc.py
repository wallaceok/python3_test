# -*- coding: UTF-8 -*-
import re
from urllib import request

import urllib
import http.cookiejar
import jsonpath
import json
import random

import time

url = "http://dc-hfd-api.fx.com"
postdata =urllib.parse.urlencode({
"username":"13212345670",
"password":"123456"
}).encode('utf-8')
header = {
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0"
}
req = urllib.request.Request('http://dc-hfd-api.fx.com/api/v1/user/login',postdata,header)
##print(urllib.request.urlopen(req).read().decode('utf-8'))

#自动记住cookie
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
r = opener.open(req)
#print(r.read().decode('utf-8'))


jsonobj = json.load(r)
print(jsonobj)

token = jsonpath.jsonpath(jsonobj,'$.token')
print(token)

req = urllib.request.Request("http://dc-hfd-api.fx.com/api/v1/new_community?pageIndex=1&limit=90&city=159&houseType=")
r1 = opener.open(req)
#print(r1.read().decode('utf-8'))
jsonobj1 = json.load(r1)
#print(jsonobj1)
#s1 = jsonpath.jsonpath(jsonobj1,'$.rows.(1).id')
list1 = []
for v in jsonobj1['rows']:
    #print("%s" % (v))
    #print(jsonpath.jsonpath(v,'$.id'))
    list1.append(jsonpath.jsonpath(v,'$.id')[0])
    #print(type(jsonpath.jsonpath(v,'$.id')))

print(list1)
for l in list1:
    print(l)

tokenss = "Bearer"+str(token[0])
#print(tokenss)
header1 = {
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:32.0) Gecko/20100101 Firefox/32.0",
"Content-Type":"application/x-www-form-urlencoded",
"Authorization":tokenss
}
count = 1
for l in list1:
    postdata1 =urllib.parse.urlencode({
    "city_id":"undefined",
    "premise":l,
    "name":"测试"+str(count),
    "telephone":"131"+str(random.randrange(10))+str(random.randrange(10))+str(random.randrange(10))+str(random.randrange(10))+str(random.randrange(10))+str(random.randrange(10))+str(random.randrange(10))+str(random.randrange(10)),
    "mobilePhone":"",
    "houseType":"",
    "budget":"",
    "arriveTime":"2018-10-12",
    "more":""
    }).encode('utf-8')
    #print(postdata1)
    time.sleep(2)
    req = urllib.request.Request('http://dc-hfd-api.fx.com/api/v1/customer/create',postdata1,header1)
    time.sleep(2)
    r = opener.open(req)
    print('count: '+str(count)+'  id: '+str(l)+'  result: '+r.read().decode('utf-8'))
    count=count+1





