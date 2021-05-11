# !/usr/bin/python  
# -*- coding: UTF-8 -*- 
# @Author :  alexuh  
# @Created on ::  2019-11-28 11:03:15  
import requests
from bs4 import BeautifulSoup as bs4
import io
import sys

# 获取首页数据
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
url = "http://www.xiachufang.com/"
headers = {"User-Agent": "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)"}
r = requests.get(url, headers=headers)
html = r.text


# 解析数据获取图片连接
import urllib.parse as parse
def get_src(value):
    return value.split("@")[0]
def parse_url(value):
    v = parse.urlparse(value)
    return v.scheme + "://"+ v.netloc + v.path
result = []
soup = bs4(html, "lxml")
for i in soup.find_all("img"):
    if i.has_attr("data-src"):
        result.append(parse_url(get_src(i["data-src"])))
    else:
        result.append(parse_url(get_src(i["src"])))

# 存储数据
import os as _os
image_dir = _os.path.join(_os.curdir, "images")
if not _os.path.isdir(image_dir):
    _os.makedirs(image_dir)
j = 0
count = 0
error_img = []
for img in result:
    if '.' not in img:
        error_img.append(img)
    else:
        print(img)
        res = requests.get(img)
        res.raise_for_status
        filename = img.split("/")[-1]
        print(filename)
        count += 1;
        filepath = _os.path.join(image_dir, filename)
        with open(filepath, "wb") as f:
            for chunk in res.iter_content(4096):
                f.write(chunk)
print(len(result))
print(count)
print(error_img)
