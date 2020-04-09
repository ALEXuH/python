# coding=utf-8
# id,name,age,sex,star

import uuid as _uuid
import random as _random
stars = ["双子座", "双鱼座", "摩蝎座", "金牛座", "水瓶座"
, "巨蟹座", "处女座", "天秤座", "白羊座", "射手座", "狮子座"]
n = 100
# f = open("aa", "w+")
# while (n > 0):
#     id = _uuid.uuid1(node=10)
#     name = str(_uuid.uuid4())[0:4]
#     age = _random.randint(a=0, b=100)
#     star = stars[_random.randint(a=0, b=10)]
#     print("%s,%s,%s,%s" % (id, name, age, star))
#     f.write("%s,%s,%s,%s" % (id, name, age, star))
#     n -= 1
# f.close

str1 = "insert into mt values("
while (n > 0):
    id = _random.randint(1, 1000000000)
    name = str(_uuid.uuid4())[0:4]
    age = _random.randint(a=0, b=100)
    time = str(_random.randint(a=1000, b=2020)) + "-"+str(_random.randint(a=10, b=12)) + "-"+ str(_random.randint(a=10, b=12)) + " " + str(_random.randint(a=10, b=24))+ ":" + str(_random.randint(a=10, b=60))+ ":" + str(_random.randint(a=10, b=60))
    print("%s%s,'%s',%s,'%s');" % (str1,str(id),name,age,time))
    n -= 1



