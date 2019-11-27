#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Author : ALEXuH
# @Created on : 2019/9/17 0017

import numpy as np
import pandas as pd


dates = pd.date_range('20130101', periods=6)
# print(dates)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
df.describe()
# print(df)
# print("\n")
# print(df.dtypes)
# print(df.A)
# print("---")
# print(df.B)
# print("---")
# print(df.head(3))
# print("--")
# print(df.tail(1))
# print("--")
# print(df.index)
# print("===")
# df.describe()
# df.T
# print(df.sort_index(axis=0, ascending=False))
# print(df.sort_values(by="B"))
# print("---")
# print(df["A"])
# print(df[0:2])
# print(df['2013-01-02':'2013-01-04'])
# print(df['20130102':'20130104'])

#xls = pd.read_excel("111.xlsx")
#print(xls)
# with pd.ExcelFile("111.xlsx") as xls:
#     df1 = pd.read_excel(xls, "Sheet1", index_col=1, na_values=["NA"], usecols=[0,1,2], header=1)
#     print(df1)
def unify(v):
    if v is None:
        return v
    if isinstance(v, unicode):
        return v.encode("utf8")
    if isinstance(v, str):
        return v
    return str(v)
# with pd.ExcelFile("222.xlsx") as xls:
#     df1 = pd.read_excel(xls, unicode("销售", "utf-8"),names=["yt", "floor", "partition", "sales"], usecols=[2, 4, 6, 9], skiprows=[1, 2, 3, 4])
#     print(df1)
#     print(df1.dropna(how="any", subset=["yt", "floor", "partition"]))
#     # for row in df1.itertuples(name="RowData"):
#     #     print(row)
import sys
reload(sys)
sys.setdefaultencoding('utf8')
print(type("主题街"))
with pd.ExcelFile("222.xlsx") as xls:
    df1 = pd.read_excel(xls, unicode("销售", "utf-8"),names=["yt", "floor", "partition", "sales"], usecols=[2, 4, 6, 23], skiprows=[1, 2, 3, 4])
    #print(df1)
    # for row in df1.itertuples(name="RowData"):
    #     print(row)
    df2 = df1.dropna(how="any", subset=["yt", "floor", "partition"])
    print(df2[df2["floor"] == unify("主题街")]["sales"].sum())
    df3 = df2[df2["floor"] == "主题街"]
    print(df3.sort_values(by="sales", ascending=False))
    print("===")
    print(type(df3.sort_values(by="sales", ascending=False).iloc[0]))