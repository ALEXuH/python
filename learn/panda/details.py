#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Author : ALEXuH
# @Created on : 2019/9/19 0019

import pandas as pd
import collections

import configparser
import os
from os import path as _path

cf = configparser.ConfigParser()
config_path = _path.join(_path.dirname(os.path.realpath(__file__)), "source.ini")
cf.read(config_path, encoding="utf-8")
#options = cf.options("Detail")
file1 = _path.join(_path.dirname(os.path.realpath(__file__)), cf.get("Detail", "use_file"))
file2 = _path.join(_path.dirname(os.path.realpath(__file__)), cf.get("Detail", "detail_file_name"))
number = int(cf.get("Detail", "day"))

def getCol():
    map = {}
    a = 8
    for i in range(1, 32):
        map[i] = a
        a += 1
    return map

import re as _re
def handleSales(sale):
    sale1 = sale / 10000.0
    sale_str = _re.match(r".*\.0{2,}", str(sale1))
    if sale_str is None:
        return "%.2f" % (sale / 10000.0)
    else:
        return sale1

class Rank:
    topic = None
    head = None
    tail = None
    total = 0.0
    count = 0
    def __init__(self, topic, head, tail, total, count):
        self.topic = topic
        self.head = head
        self.tail = tail
        self.total = total
        self.count = count
    def show(self):
        result = "%s：%s万 \n品牌数量：%s" % (self.topic, "%.2f" % (self.total / 10000.0), self.count)
        str = "销售前三："
        a = 1
        for k,v in self.head.items():
            str1 = "0%s、%s：%s万" % (a, "/".join(v), k / 10000.0)
            str = str + "\n" + str1
            a += 1
        str1 = ""
        b = 3
        for k,v in self.tail.items():
            str2 = "0%s、%s：%s万" % (b, "/".join(v), k / 10000.0)
            str1 = str2 + "\n" + str1
            b -= 1
        str1 = "销售后三："+ "\n" + str1
        return result + "\n" + str + "\n" + str1
def unify(v):
    if v is None:
        return v
    if isinstance(v, unicode):
        return v.encode("utf8")
    if isinstance(v, str):
        return v
    return str(v)
def getList(df, sale):
    df1 = df[df["sales"] == sale]
    v = []
    for row in df1.itertuples(name="RowData"):
        v.append(row.partition)
    return v

def getValues(value, topic):
    total = value["sales"].sum()
    size = value["sales"].size
    df1 = value.drop_duplicates(["sales"]).sort_values(by="sales", ascending=False)
    head = df1.head(3)
    tail = df1.tail(3)
    d1 = collections.OrderedDict()
    for row in head.itertuples(name="RowData"):
        sale = row.sales
        v = getList(value, sale)
        d1[sale] = v
    d2 = collections.OrderedDict()
    for row in tail.itertuples(name="RowData"):
        sale = row.sales
        v = getList(value, sale)
        d2[sale] = v
    rank = Rank(topic, d1, d2, total, size)
    return rank

def getValuesYt(value, topic):
    total = value["sales"].sum()
    size = value["sales"].size
    # remove 主题街
    # for row in value.itertuples(name="RowData"):
    #     floor1 = unify(str(row.floor).strip())
    #     if floor1 in floor_partition:
    #         value.drop(index=row.Index, inplace=True)
    df1 = value.drop_duplicates(["sales"]).sort_values(by="sales", ascending=False)
    head = df1.head(3)
    tail = df1.tail(3)
    d1 = collections.OrderedDict()
    for row in head.itertuples(name="RowData"):
        sale = row.sales
        v = getList(value, sale)
        d1[sale] = v
    d2 = collections.OrderedDict()
    for row in tail.itertuples(name="RowData"):
        sale = row.sales
        v = getList(value, sale)
        d2[sale] = v
    rank = Rank(topic, d1, d2, total, size)
    return rank


import sys
reload(sys)
sys.setdefaultencoding('utf8')
floor_partition = ["主题街"]
yt_partition_detail = ["主次力店及主题餐厅"]
yt_partition = ["餐饮", "服装", "生活配套", "服饰配套"]
yt_child = ["儿童业态"]
not_need_list = ["装修", "未进场", ""]
day = getCol()[number]

with pd.ExcelFile(file1) as xls:
    df = pd.read_excel(xls, unicode("销售", "utf-8"),names=["yt", "floor", "partition", "sales"], usecols=[2, 4, 6, day], skiprows=[1, 2, 3, 4])\
        .dropna(how="any", subset=["yt", "floor", "partition"])
    for row in df.itertuples(name="RowData"):
        sale = unify(str(row.sales).strip())
        if sale in not_need_list:
            df.drop(index=row.Index, inplace=True)
    result_list = []
    result1 = ""
    result_list_1 = []
    result_list_2 = []
    for i in yt_partition_detail:
        value = df[df["yt"] == unify(i)]
        total = value["sales"].sum()
        c = 1
        he = i + ": " + "%.2f" % (total / 10000.0) + "万\n0"
        for row in value.itertuples(name="RowData"):
            if c < 10:
                he = he + "0" + str(c) + "、" + row.partition + ": "+str(row.sales / 10000.0) + "万\n"
            else:
                he = he + str(c) + "、" + row.partition + ": "+str(row.sales / 10000.0) + "万\n"
            c += 1
        result1 = he
    for i in floor_partition:
        value = df[df["floor"] == unify(i)]
        result = getValues(value, i)
        result_list.append(result)
    pd.options.mode.chained_assignment = None
    for i in yt_partition:
        list_k = i.split(",")
        list_v = []
        for j in range(0, len(list_k)):
            v = df[df["yt"] == unify(list_k[j])]
            list_v.append(v)
        value = list_v[0]
        if len(list_v) > 1:
            for m in list_v:
                value = pd.merge(value, m, "outer")
        result = getValuesYt(value, i)
        result_list_1.append(result)
        
    for i in yt_child:
        value = df[df["yt"] == unify(i)]
        result = getValuesYt(value, i)
        result_list_2.append(result)    
    
    f = open(file2, "w+")
    for dep in result_list:
        f.write(dep.show())
        f.write("\n")
    f.write("\n")
    f.write(result1)
    f.write("\n")
    for dep in result_list_1:
        f.write("\n")
        f.write(dep.show())
    for dep in result_list_2:
        f.write("\n")
        f.write(dep.show())
    f.close()
print("Success generate Details file")
raw_input()
