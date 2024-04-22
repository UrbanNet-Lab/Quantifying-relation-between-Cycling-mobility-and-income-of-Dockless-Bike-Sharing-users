# -*- coding: utf-8 -*-
# @Time : 2023/7/6 17:19
# @Author : YangYu
# @Email: yangyu.cs@outlook.com
# @File : 1.计算栅格平均房价.py
# @Software: PyCharm
import pandas as pd

data = pd.read_csv("../data/金华房价2&3.csv")
# print(data.dtypes)
data = data.drop('300_id', axis=1)
aa = data.groupby("200_id")
print(aa.size())
b = aa.mean()
b.to_csv("../data/金华平均房价200m.csv", index=True)
