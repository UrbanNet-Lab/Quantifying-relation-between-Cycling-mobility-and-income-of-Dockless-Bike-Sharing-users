# -*- coding: utf-8 -*-
# @Time : 2023/7/10 10:51
# @Author : YangYu
# @Email: yangyu.cs@outlook.com
# @File : 7.用户分类.py
# @Software: PyCharm
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def jh():
    data = pd.read_csv('../data/房价/金华用户分类(3).csv')
    ul = data['level']
    userid = data['userid']
    dict2 = dict(zip(userid, ul))
    data3 = pd.read_csv('../data/金华订单数据（200栅格）.csv')
    print(f"金华订单数量：{len(data3)}")
    level1 = []
    level2 = []
    level3 = []

    level = []
    for u in dict2.items():
        # print(data3[data3['UserID'] == u[0]].values)
        trips = data3[data3['UserID'] == u[0]].values
        # if trips.shape[0]>2:
        #     print(list(trips))
        #     break
        if u[1] == 1:
            level1.extend(trips)
            level.extend(trips)
        elif u[1] == 2:
            level2.extend(trips)
            level.extend(trips)
        elif u[1] == 3:
            level3.extend(trips)
            level.extend(trips)

    # print(level1)
    df1 = pd.DataFrame(level1)
    df1.columns = data3.columns
    print(len(df1) / len(df1.groupby("UserID")))
    df2 = pd.DataFrame(level2)
    df2.columns = data3.columns
    print(len(df2) / len(df2.groupby("UserID")))

    df3 = pd.DataFrame(level3)
    df3.columns = data3.columns
    print(len(df3) / len(df3.groupby("UserID")))



    # df5 = pd.DataFrame(level5)
    # df5.columns = data3.columns
    df_all = pd.DataFrame(level)
    df_all.columns = data3.columns
    users = df_all.groupby('UserID')
    print(f"用户数量：{len(users)}")
    print(f"订单数量:{len(df_all)}")
    # df1.to_csv('../data/level/过滤/3类/jinhua_level1.csv', index=False)
    # df2.to_csv('../data/level/过滤/3类/jinhua_level2.csv', index=False)
    # df3.to_csv('../data/level/过滤/3类/jinhua_level3.csv', index=False)
    # df_all.to_csv('../data/level/过滤/3类/jinhua_level_all.csv', index=False)


def nb():
    """
    已经得到用户分类的情况下，
    根据用户分类将订单分级
    :return:
    """
    data = pd.read_csv('../data/房价/宁波用户分类(3).csv')
    ul = data['level']
    userid = data['userid']
    dict2 = dict(zip(userid, ul))
    data3 = pd.read_csv('../data/宁波OD数据（500m栅格）.csv')
    print(f"宁波订单数量：{len(data3)}")

    level1 = []
    level2 = []
    level3 = []
    level = []
    for u in dict2.items():
        trips = data3[data3['UserID'] == u[0]].values

        if u[1] == 1:
            level1.extend(trips)
            level.extend(trips)
        elif u[1] == 2:
            level2.extend(trips)
            level.extend(trips)
        elif u[1] == 3:
            level3.extend(trips)
            level.extend(trips)

    df1 = pd.DataFrame(level1)
    df1.columns = data3.columns
    print(len(df1) / len(df1.groupby("UserID")))
    df2 = pd.DataFrame(level2)
    df2.columns = data3.columns
    print(len(df2) / len(df2.groupby("UserID")))

    df3 = pd.DataFrame(level3)
    print(len(df3) / len(df3.groupby("UserID")))

    df3.columns = data3.columns

    df_all = pd.DataFrame(level)
    df_all.columns = data3.columns
    users = df_all.groupby("UserID")
    print(f"用户数量：{len(users)}")
    print(f"订单数量:{len(df_all)}")
    # df1.to_csv('../data/level/过滤/3类/ningbo_level1.csv', index=False)
    # df2.to_csv('../data/level/过滤/3类/ningbo_level2.csv', index=False)
    # df3.to_csv('../data/level/过滤/3类/ningbo_level3.csv', index=False)
    # df_all.to_csv('../data/level/过滤/3类/宁波_level_all.csv', index=False)


if __name__ == '__main__':
    jh()
    nb()
