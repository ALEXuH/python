# coding=utf-8
import math
import random
print("hello word")
print("你好，中国")

# 缩进
if 1 < 3:
    print("true")
else:
    print("false")

# 多行语句 [],(),{}不需要换行符
a1 = "a1"
a2 = "a2"
a3 = "a3"
value = a1 + \
        a2 + \
        a3
print(value)

days = ["das", "das1"]
print(days)

# '',"",""" """
word = 'word'
word1 = "word1"
word2 = """word2
word3"""

# 注释
'''
这是一个注释
'''

'''
type: number::String::List::Tuple::Dictionary
'''
# String
str1 = "alexu like eating"
print(str1[0])
print(str1[0:3])
print(str1[0:6:2])
print(str1[0:])
print(str1[2:])
print(str1 * 3)
print(str1 + "test1")

# List
names = ["xiaoming", "xiaohong", "xiaohei", "xiaohei1", "xiaohei2"]
names2 = ["name1"]
print(names[0])
print(names[1:3])
print(names[2:])
print(names[0:4:2])
print(names * 2)
print(names + names2)

# tuple2
tuple2 = ("tuple21", "tuple22","tuple23","tuple24","tuple25")
tuple21 = ("tuple27", "das")
print(tuple2[0])
print(tuple2[1:3])
print(tuple2[1:4:2])
print(tuple2 * 2)
print(tuple2 + tuple21)

# Dictory
dict = {}
dict["name1"] = "alexuh"
dict[2] = "dasdas"
second = {"name": "joion", "name1": 111,111: 222}
print(second["name1"])
print(dict[2])
print(second.keys())
print(second.values())

# type transform
print(int("30"))
print(str(30))
print(repr("30"))
print(eval("30"))
print(list(tuple2))
# print(tuple(list))
# print(set(list))
# print(dict())
print(chr(40))
print(ord('a'))
print(hex(30))
print(oct(10))

# and or not
a = "true"
b = bool(0)
if a and b:
    print("true")
else:
    print("false")

if a or b:
    print("true")
else:
    print("false")

if not(a and b):
    print("true")
else:
    print("false")

print(id(a))

# in / not in
if a in names:
    print("true")
else:
    print("false")

if a not in names:
    print("true")
else:
    print("false")

num = 10
if (num == 3):
    print("3")
elif (num == 4):
    print("4")
elif (num == 5):
    print("5")
else:
    print("other")

# while for
count = 0
while (count < 9):
    print('count: ',count)
    count += 1

for n in names:
    print("name:",n)

for index in range(len(names)):
    print("name: ",names[index])

# break continue pass
print("--------------")
list2 = ["xiaohei"]
for name1 in names:
    print(name1)
    if (name1 == "xiaoming"):
        break
    if name1 in list2:
        pass # 占位符
    if name1 in list2:
        print(name1)

print(dir(math))

print(random.choice(range(1, 100, 2)))

import time
# time module
ticks = time.time()
print("time: ", ticks)
print(time.localtime(ticks))
print(time.asctime(time.localtime(ticks)))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# calendar
import calendar
cal = calendar.month(2016, 1)
print(cal)

# dataTime
import datetime
date = datetime.datetime.now()

def hello(name, age = 20):
    print("hello function",name,age)

hello("xiaomn")

def names(*name):
    for name2 in name:
        print(name2)
names("xa",32)

sum1 = lambda x,y: x + y
print(sum1(10,400))

# IO/File
# str = raw_input("input: ")
# print("inpout content:", str)

file = open("aa","w+", 1000)
file.write("aaa")
print(file.read(10))
print(type(file))
file.close()

# exception
try:
    fh = open("test", "w")
except IOError:
    print("can not find file")
else:
    print("it is ok")
    fh.close()

try:
    fh = open("test", "w")
    try:
        fh.write("aaa")
    finally:
        print("close file")
        fh.close()
except IOError:
    print("can not find file")

# 内置函数inner function
print(abs(-210))
#print(cmp(1, 2))
print(bool(1))
print(int(20.11))

# 函数式编程 lamada param_list:expr
a = lambda x,y : x + y
print(a(14,39))

# map, reduce, filter, sorted等内置函数式编程函数
func = lambda x : x**x
list = [1,2,10]
#print(list(map(func, list))) #返回迭代器对象
#print(filter(lambda x: x%2 == 0, list))

# 列表解析式 [expr for param in list if expr] 底层c语言实现效率更高
print([i for i in list])
print([i*2 for i in list])
print([i for i in list if i%2 == 0])

# enumerate 同时遍历index和value
for i,v in enumerate(list):
    print(str(i)+ ":" + str(v))


# 迭代器生成器

# 