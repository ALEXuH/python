# coding=utf-8
import re
import sys
import datetime
print(re.match("aaa", "aa dasaaadd"))
print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.match('com', 'www.runoob.com'))         # 不在起始位置匹配

line = "Cats are smarter than dogs"
match = re.match(r"(.*) are (.*?) .*", line, re.M|re.I)
print("----------")
print match.group()
print match.group(1)
print match.group(2)

print "----------"
print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.search('com', 'www.runoob.com'))         # 不在起始位置匹配

pattern = re.compile(r"\d+")
m = pattern.match("432fsd")
print m
print m.start(0)
print(m.group(0))
print(m.end(0))

str1 = "das809adsss8909ad"
pattern = re.compile(r"[a-z]*\d+.*")
result1 = pattern.findall(str1, re.I|re.M)
print result1
