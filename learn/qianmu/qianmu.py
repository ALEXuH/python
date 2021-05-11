#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Author : ALEXuH
# @Created on : 2020/12/15 19:16

import requests as r
from lxml import etree as e
import json as _json

# 获取数据
resp = r.get('http://www.qianmu.org/ranking/1528.htm')
selector = e.HTML(resp.text)
links = selector.xpath('//div[@class="rankItem"]//tr[position()>1]//td/a/@href')
problem = []


# 获取数据
def fetch(url):
    res = r.get(url)
    if res.status_code != 200:
        res.raise_for_status()
    else:
        return res.text


# 解析数据
def parse_line(link):
    data = {}
    uniInfo = r.get(link)
    unionXml = e.HTML(uniInfo.text)
    # 获取标题，表格信息
    title = unionXml.xpath("//div[@class='wikiContent']/h1[@class='wikiTitle']/text()")
    keys = unionXml.xpath("//div[@class='wikiContent']/div[@class='infobox']//tbody//td[1]")
    values = unionXml.xpath("//div[@class='wikiContent']/div[@class='infobox']//tbody//td[2]")
    vs = []
    ks = []
    data['大学名称'] = ''.join(title).strip()
    for k in keys:
        ks.append(''.join([str.replace(i, '\t', '').strip() for i in k.xpath('.//text()')]))
    for v in values:
        vs.append(''.join([str.replace(j, '\t', '').strip() for j in v.xpath('.//text()')]))
    if len(ks) != len(vs):
        problem.append(title[0])
    for i in range(len(vs)):
        data[ks[i]] = vs[i]
    return data


# 存储数据
def process_data(data):
    with open("data.txt", mode="a+", encoding="UTF-8") as f:
        f.write(_json.dumps(data, ensure_ascii=False))
        f.write("\n")


if __name__ == '__main__':
    print("start-------------")
    url = "http://www.qianmu.org/ranking/1528.htm"
    selector = e.HTML(fetch(url))
    # 获取大学所有链接
    links = selector.xpath('//div[@class="rankItem"]//tr[position()>1]//td/a/@href')
    for link in links:
        #print(link)s
        process_data(parse_line(link))
    print("process link: %d" % len(link))
    print(problem)
    print("end-------------")
