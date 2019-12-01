#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Author : ALEXuH
# @Created on : 2019/9/14 0014
import requests
res = requests.get("https://www.runoob.com/python/python-json.html")
# print(res.status_code)
# reponse header
# print(res.headers)
# request headers
# print(res.request.headers)
# print(res.encoding)
# print(res.next)
# print(res.cookies)
print(res.json())
# print(res.content)
# print(res.text)
# print(res.encoding)

# data = {"user": "aa"}
# res = requests.get("https://api.github.com/events", data=data)
# print(res.text)
# print(res.url)
#
# payload = {'key1': 'value1', 'key2': ['value2', 'value3']}
# res1 = requests.get("https://api.github.com/events", params=payload)
# print(res1.text)
# print(res1.url)
# print(res1.encoding)
# print(res1.content)
#
# print("----")
# print(res1.json())
#
# res2 = requests.get("https://api.github.com/events", stream=True)
# print(res2.raise_for_status())
# print(res2.raw)
#
#
# with open("./aa.txt", "wb") as fd:
#     for chunk in res1.iter_content(1000):
#         fd.write(chunk)
#
# url = "https://api.github.com/events"
# headers = {'user-agent': 'my-app/0.0.1'}
# res3 = requests.get(url, headers=headers)
# print(res3.status_code)
#
#
# res4 = requests.post(url, data=payload)
# print(res4.status_code)
# print(res4.text)
#
# url1 = 'http://httpbin.org/post'
# files = {'file': ('report.xls', open('./aa.txt', 'rb'), 'application/vnd.ms-excel', {'Expires': '0'})}
# files1 = {'file': ('report.csv', 'some,data,to,send\nanother,row,to,send\n')}
# # res5 = requests.post(url1, files=files)
# res5 = requests.post(url1, files=files1)
# print(res5.status_code)
# print(res5.text)
#
# print(res5.headers)


# res6 = requests.get("http://httpbin.org/status/404")
# print(res6.status_code)
# res6.raise_for_status()

# url2 = "http://httpbin.org/cookies"
# cookie = {"cookies_are": "working"}
# res7 = requests.get(url2, cookies=cookie)
# print(res7.text)
# print(res7.headers)
# print(res5.history)

# requests.get("http://github.com", timeout=0.0001)

# advance
# url3 = "http://httpbin.org/cookies/set/sessioncookie/123456789"
# url4 = "http://httpbin.org/cookies"
# cookie = {"cookie1": "value1"}
# with requests.session() as s:
#     r1 = s.get(url3, cookies=cookie)
#     print(r1.text)
#     r = s.get(url4)
#     print(r.text)

# requests.get('https://requestb.in', verify=True)
# s = requests.session()
# # ca
# s.verify = '/path/aa.txt'
# a = "dasd"
# print(a.split(".")[0])
# print(len(a.split(".")))
#
# proxies = {
#     'http': 'http://120.26.110.59:8080',
#     'http': 'http://120.52.32.46:80',
#     'http': 'http://218.85.133.62:80',
# }
# print(proxies["http"])

# url = "http://localhost:8888/"
# res = requests.post(url)
# print(res.headers)
# print(res.request.headers)
# print(res.text)

# res1 = requests()

import json as _json
url = "http://wthrcdn.etouch.cn/weather_mini?city=常州"
res = requests.get(url)
#print(res.text)
#print(res.json())
data = res.json()["data"]["yesterday"]["type"]
print(data)
