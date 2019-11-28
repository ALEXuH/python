# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup as bs
html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

"""
解析器
html.paeser: 速度适中，容错能力强
lxml：第三方解析器需要安装（pip install lxml），速度快，容错能力强
html5lib: 速度慢，最好的容错性
"""
#soup = bs(html_doc, "html.parser")
#soup = bs(html_doc, "html5lib")
soup = bs(html_doc, "lxml")

#print(soup.prettify())
# Tag->[name,attributes,string,parent]
print(soup.name)
print(soup.title)
print(soup.title.name)
print(soup.title.string)
print(soup.title.parent.name)
print(soup.p["class"])
print(soup.p.attrs["class"])
print(soup.p.parent.name)

# 通过.来去tag只能取到第一个tag find_all取所有的Tag
# find_all() 和 find() 只搜索当前节点的所有子节点,孙子节点等
print(soup.body.a)
print(soup.findAll("a"))
print(soup.find(id="link1"))
print("---")
# 获取一个tag所有的直接子节点(可递归获取所有节点)
print(soup.body.contents)
print("========")
for child in soup.children:
    print(child.name)

for child in soup.body.children:
    print(child.name)

# 输出多个子节点的string
print("=========")
for i in soup.strings:
    print(repr(i))
print("---")
for i in soup.body.stripped_strings:
    print(repr(i))

# 包含href属性的
print(soup.findAll(href=True))
print(soup.findAll(href=True, id="link1"))
print(soup.findAll(href=True, id="link1", attrs={"data-das": "das"}))
print("===")
print(soup.findAll(class_="story"))

print("====")
# 获取所有a节点的href
for i in soup.find_all("a", href=True):
    print(i["href"])