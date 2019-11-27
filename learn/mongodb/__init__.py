#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Author : ALEXuH
# @Created on : 2019/11/21

from pymongo import MongoClient as MC
import pymongo
host = "192.168.60.166"
port = 27017
client = MC(host, port)
print(client)
db = client["aa"]
print(db.list_collection_names())
# 访问集合
collection = client["aa"]["inventory"]
print(collection.count())
records = collection.find({})
for i in records:
    print(i)
print("========")
# 插入数据
db = client["bb"]
for i in db["posts"].find({"age": {"$lte": 21}}).sort("age", pymongo.ASCENDING):
    print(i)
post = {"name": "alexuh11111", "age": 210}
posts = db["posts"]
post_id = posts.insert_one(post).inserted_id
print(post_id)

print(type([{"aa": "bb"}]))
print(type([{"aa": "bb"}]) == list)
print(type(db["posts"].find({"age": {"$lte": 21}})))