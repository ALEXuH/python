# #!/usr/bin/python
# # -*- coding: UTF-8 -*-
# # @Author : ALEXuH
# # @Created on : 2019/9/19 0019
#
# import collections
# d1={}
# d2 = collections.OrderedDict()
# d2['a']='A'
# d2['b']='B'
# d2['c']='C'
# d2['d']='D'   #此时的d1 = {'a':'A','b':'B','c':'C','d':'D'}
# type(d2)
# print(d2)
# for k,v in d2.items():
#     print k,v
#
# v = """
#     %s：%s万
#     品牌数量：%s
#      """  % ("das", 100.0, 88)
#
# print(v + "\n" + "da")
# aa = ["dsa"]
# # print(",".join(aa))
# aa = ["dasd", "dasd", "dsaddd"]
# for i in range(0, len(aa)):
#     print(i)

# f = 0.003
# a = "%.2f" % f
# print(a)
import re
line = "1200.0324"
print(re.match(r".*\.0{2,}", line))