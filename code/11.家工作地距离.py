# -*- coding: utf-8 -*-
# @Time : 2023/7/14 17:56
# @Author : YangYu
# @Email: yangyu.cs@outlook.com
# @File : 11.家工作地距离.py
# @Software: PyCharm
from math import sin, radians, sqrt, asin, cos

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def geodistance(lng1, lat1, lng2, lat2):
    lng1, lat1, lng2, lat2 = map(radians, [float(lng1), float(lat1), float(lng2), float(lat2)])
    # lng1, lat1, lng2, lat2 = map(radians, [lng1, lat1, lng2, lat2])
    dlon = lng2 - lng1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    dis = 2 * asin(sqrt(a)) * 6371 * 1000  # 地球平均半径，6371km
    dis = round(dis / 1000, 3)
    return dis


NB_X = 121.548816000000002
NB_Y = 29.867888000000001
JH_X = 120.0564674102
JH_Y = 29.3031956777


def cal():
    # data = pd.read_csv('D:\QGISData\浙江省\\ningbo_500mc.csv')
    data = pd.read_csv('E:\QGISData\浙江省\\jinhua_200m.csv')
    id_ = data['id']
    x = data['x']
    y = data['y']
    dict1 = dict(zip(id_, zip(x, y)))
    data = pd.read_csv('../data/房价/金华用户分类(3).csv')
    # data = pd.read_csv('../data/房价/宁波用户分类(3).csv')
    # level = data['level']
    home = data['home']
    d1 = []
    for h in home:
        hx, hy = dict1[h]
        d = geodistance(hx, hy, NB_X, NB_Y)
        d1.append(d)
    work = data['work']
    d2 = []
    for w in work:
        wx, wy = dict1[w]
        d = geodistance(wx, wy, NB_X, NB_Y)
        d2.append(d)

    data['dh'] = d1
    data['dw'] = d2

    data2 = data.dropna()
    data['level'] = data2['level'].astype(int)
    level1 = data2[data2['level'] == 1]
    level2 = data2[data2['level'] == 2]
    level3 = data2[data2['level'] == 3]
    # level4 = data2[data2['level'] == 4]
    # level5 = data2[data2['level'] == 5]
    level1.to_csv('../data/level/过滤/3类/金华用户H-W_1.csv', index=False)
    level2.to_csv('../data/level/过滤/3类/金华用户H-W_2.csv', index=False)
    level3.to_csv('../data/level/过滤/3类/金华用户H-W_3.csv', index=False)
    data2.to_csv('../data/level/过滤/3类/金华用户H-W_ALL.csv', index=False)


def cal2():
    res = []
    for i in range(1, 4):
        data = pd.read_csv(f'../data/level/过滤/3类/宁波用户H-W_{i}.csv')
        dh = data['dh']
        dw = data['dw']
        dy = 0

        for j in range(len(dh)):
            if dh[j] > dw[j]:
                # 家比工作地到城市中心的距离更远
                dy += 1
        print(dy / len(dh), (1 - dy / len(dh)))
        res.append(dy / len(dh))
    print(res)


if __name__ == '__main__':
    cal()
    plt.figure(figsize=(8,7))
    # cal2()
    jh = [0.5183374083129584, 0.42732811140121846, 0.5132743362831859, 0.2982456140350877, 1.0]
    nb = [0.5829493087557603, 0.5186196849676773, 0.5013440860215054, 0.48801571709233793, 0.577259475218659]
    x = [1.0, 2.0, 3.0]
    # 分为3类
    jh = [0.547945205479452, 0.50414634146341463, 0.4756756756756757]
    nb = [0.5750111957008509, 0.51950084639090236, 0.51526588845654995]
    plt.plot([0.5, 3.5], [0.5, 0.5], color='slategray', linestyle='--')
    bar_width = 0.3
    x1 = [1.35, 2.35, 3.35]
    plt.bar(x1, jh, width=bar_width, color='#9999ff', label='Jinhua')
    plt.bar(x, nb, width=bar_width, color='#ff9999', label='Ningbo')

    # plt.bar(x1, jh, width=bar_width, color='', label='Jinhua')
    plt.legend()
    plt.xlabel('category', fontsize=16)
    plt.ylabel('fraction of $d_H$-$d_W$', fontsize=16)
    plt.ylim([0, 0.8])
    plt.xticks([1, 2, 3])
    plt.tick_params(labelsize=12)

    # plt.show()
    plt.savefig('../figure/3类/work_trip_outward_3.pdf', bbox_inches='tight')
    # plt.legend()
    plt.show()
