# -*- coding: UTF-8 -*-
import re
from urllib import request

import urllib
import http.cookiejar
import jsonpath
import json
import random

import time

url = "https://api.liqiang365.com/login/in.ph"
postdata =urllib.parse.urlencode({
"account":"13523715133",
"password":"a123456a",
"oneType":"0",
"updateVersion":"V3.0",
"version":"V3.0",
"clientType":"1"
}).encode('utf-8')
header = {
"Accept":"application/json, text/javascript, */*; q=0.01",
"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:45.0) Gecko/20100101 Firefox/45.0",
"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
"Referer":"http://www.liqiang365.com/pc/html/login.html"
}

req = urllib.request.Request(url,postdata,header)

#自动记住cookie
cj = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
r = opener.open(req)

jsonobj = json.load(r)
print(jsonobj['resobj']['id'])  #id
print(jsonobj['resobj']['token']) #token

token = jsonobj['resobj']['token']

postdata =urllib.parse.urlencode({
"courseid":"fd254248a1d54527931cb46ba6abe3",
"page":"1",
"type":"1",
"updateVersion":"V3.0",
"version":"V3.0",
"clientType":"1",
"token":token,
"channelType":"pc",
"channel":"pc"
}).encode('utf-8')


req = urllib.request.Request('https://api.liqiang365.com/video/list',postdata,header)
r1 = opener.open(req)
jsonobj1 = json.load(r1)

result = [(item.get('name','NA'),item.get('url1','NA'),item.get('url2','NA'),item.get('url3','NA')) for item in jsonobj1['resobj']['rows'] ]
print(result)

for item in result:
    if 'NA'!=item[1]:
        print()