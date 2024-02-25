# -*- coding: utf-8 -*-
# @Time : 2023/7/7 12:24
# @Author : YangYu
# @Email: yangyu.cs@outlook.com
# @File : 根据房价对用户进行分类.py
# @Software: PyCharm

"""
1.根据地点的房价对用户进行分类
2.得到每个有房价的地区的用户数量，用户比率
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# 用户ID,用户家的位置
def nb_category():
    user = pd.read_csv("宁波用户职住数据(过滤).csv")
    user = user[user["home"] != -1]
    user = user[user["work"] != -1]
    loc_data = pd.read_csv("../data/房价/宁波有房价的地点(3类).csv")
    loc = loc_data['id'].values.tolist()
    level = loc_data['level'].values.tolist()
    dict1 = dict(zip(loc, level))
    home = user['home'].values.tolist()
    ulevel = []
    for h in home:
        if h in dict1:
            ulevel.append(dict1[h])
        else:
            ulevel.append(-1)
    user['level'] = ulevel
    user.to_csv('宁波用户分类(3类).csv', index=False)


def func():
    user = pd.read_csv("宁波用户职住数据(过滤).csv")
    user["work"] = user["work"].astype(int)
    # user.to_csv("金华用户职住数据(去掉日行程少于2).csv",index=False)
    user = user[user["home"] != -1]
    user = user[user["work"] != -1]

    # 地点的人口、平均房价、类别
    place = pd.read_csv("../data/房价/金华有房价的地点.csv").dropna()

    # 地点用户数，总人数，房价，地点等级
    # 查询
    pid = place["id"].values
    user_count = []
    # 地点用户人数字典
    dict1 = dict(user.groupby("home").size())
    for p in pid:
        if p not in dict1:
            dict1[p] = 0
        user_count.append(dict1[p])
    place["user_count"] = user_count
    # 过滤掉用户数小于0的
    data2 = place[place['user_count'] > 0]

    price = data2["total"].values
    user_count = data2["user_count"].values
    pop_sum = data2["pop_sum"].values
    id = place["id"]
    level = place["level"].astype(int)
    level_dict = dict(zip(id, level))
    # print(level_dict)
    # 计算用户用户比率
    ur = []
    for i in range(len(user_count)):
        ur.append(user_count[i] / pop_sum[i])
    data2["user_ratio"] = ur

    home = user["home"]
    level = []
    for h in home:
        if h not in level_dict:
            level.append(np.nan)
        else:
            level.append(int(level_dict[h]))
    user["level"] = level
    # user.to_csv("金华用户分类3.csv", index=False)

    # data2.to_csv("../data/金华用户比率.csv", index=False)
    # print(len(pid))

    data3 = data2[['level', 'user_count', 'pop_sum']]
    data4 = data3.groupby('level').sum()
    y1 = data4["user_count"].values
    y2 = data4["pop_sum"].values
    y1[2] += y1[3]
    y2[2] += y2[3]
    print(y1)
    print(y2)
    y = [y1[i] / y2[i] for i in range(3)]
    x = [1, 2, 3]
    print(y)
    # y = [328 / 8068.825507, 1066 / 30873.465519, 370 / 7224.040227, 44 / 2339.525625, 12 / 1577.785122]
    plt.plot(x, y)
    plt.xticks(x)
    plt.xlabel(r'category', fontsize=18)
    plt.ylabel(r'user ratio', fontsize=18)
    plt.legend()
    # # plt.savefig('../figure/fig9.b分类用户比例.pdf', bbox_inches='tight')
    plt.show()

if __name__ == '__main__':
    nb_category()