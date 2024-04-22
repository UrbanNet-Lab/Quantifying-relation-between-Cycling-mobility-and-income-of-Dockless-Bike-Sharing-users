# -*- coding: utf-8 -*-
# @Time : 2023/7/20 10:21
# @Author : YangYu
# @Email: yangyu.cs@outlook.com
# @File : 0.过滤订单属于小于2.py
# @Software: PyCharm
import pandas as pd


def jh():
    df = pd.read_csv('金华用户职住数据(去掉日行程少于2).csv')
    user_list = df["userid"].values
    print(len(user_list))
    raw_data = pd.read_csv('../data/金华订单数据（200栅格）.csv')
    filter_data = raw_data[raw_data['UserID'].isin(user_list)]
    print(len(filter_data))
def nb():
    df = pd.read_csv('宁波用户职住数据(过滤).csv')
    user_list = df["userid"].values
    print(len(user_list))
    raw_data = pd.read_csv('../data/宁波OD数据（500m栅格）.csv')
    filter_data = raw_data[raw_data['UserID'].isin(user_list)]
    print(len(filter_data))

if __name__ == '__main__':
    jh()
    nb()
