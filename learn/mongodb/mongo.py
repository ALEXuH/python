#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Author : ALEXuH
# @Created on : 2019/11/22
from pymongo import MongoClient as MC


class MongoUtils(object):
    def __init__(self, host, port, db):
        self.host = host
        self.port = port
        self.db = db
        self.mc = MC(self.host, self.port)
        self.con = self.mc[self.db]

    def change_db(self, db):
         self.con = self.mc[db]

    def insert(self, collection, post):
        if type(post) == dict:
            self.con[collection].insert_one(post)
        elif type(post) == list:
            self.con[collection].insert_many(post)
        else:
            raise Exception("please check your type is list or dict")

    def find(self,collction,  *args, **kwargs):
        return self.con[collction].find(*args, **kwargs)


def main():
    mongo = MongoUtils("192.168.60.166", 27017, "cc")
    mongo.insert("cc", {"name": "xzc", "age":24})
    mongo.insert("dd", [{"name": "xzc", "age":24}, {"name": "xz2c", "age":26}])
    for i in mongo.find("dd", {}):
        print(i)


if __name__ == '__main__':
    main()
