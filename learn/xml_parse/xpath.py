# !/usr/bin/python  
# -*- coding: UTF-8 -*- 
# @Author :  alexuh  
# @Created on ::  2019-11-28 10:44:06  

# 语法：https://www.runoob.com/xpath/xpath-syntax.html

from lxml import etree
s = """
<?xml version="1.0" encoding="ISO-8859-1"?>
<bookstore>
<book category="COOKING">
  <title lang="en">Everyday Italian</title>
  <author>Giada De Laurentiis</author>
  <year>2005</year>
  <price>30.00</price>
</book>
<book category="CHILDREN">
  <title lang="en">Harry Potter</title>
  <author>J K. Rowling</author>
  <year>2005</year>
  <price>29.99</price>
</book>
<book category="WEB">
  <title lang="en">XQuery Kick Start</title>
  <author>James McGovern</author>
  <author>Per Bothner</author>
  <author>Kurt Cagle</author>
  <author>James Linn</author>
  <author>Vaidyanathan Nagarajan</author>
  <year>2003</year>
  <price>49.99</price>
</book>
<book category="WEB">
  <title lang="en">Learning XML</title>
  <author>Erik T. Ray</author>
  <year>2003</year>
  <price>39.95</price>
</book>
</bookstore>
html = etree.html("")
"""

se = etree.HTML(s)
print(se.xpath("//bookstore")[0])
# 选取所有category属性为WEb的book节点
print(se.xpath("//book[@category='WEB']"))
values = se.xpath("//book[@category='WEB']/title/text()")
for v in values:
  print(v)

# 价格大于20
price_values = se.xpath("//book[price>20]/price/text()")
print(price_values)
print("===========")
values1 = se.xpath("//author/text()")
for v1 in values1:
  print(v1)