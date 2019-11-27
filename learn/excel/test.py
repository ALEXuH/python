#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Author : ALEXuH
# @Created on : 2019/9/16 0016
import sys
import lib2to3.fixes.fix_raw_input
print("hello")
from os import path as _path
path = _path.join(_path.dirname(__file__), "aa")
print(path)
print(_path.dirname(sys.argv[0]))
print(_path.join(_path.dirname(sys.argv[0]), "cc"))
raw_input()
