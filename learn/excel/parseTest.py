#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Author : ALEXuH
# @Created on : 2019/9/14 0014
import configparser

cf = configparser.ConfigParser()
cf.read("source.ini", encoding="utf-8")
options = cf.options("Excel")
print(cf.get("Excel", "file1"))
print(cf.get("Excel", "file2"))
print(cf.get("Excel", "file3"))
print(int(cf.get("Excel", "number")))
print(cf.get("Excel", "special_event"))
print(cf.get("Excel", "passenger_flow"))