# -*- coding: utf-8 -*-
# @Time : 2023/7/10 15:36
# @Author : YangYu
# @Email: yangyu.cs@outlook.com
# @File : 10.平均房价&访问地点数.py
# @Software: PyCharm
from collections import Counter
from math import log

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

base_line = 0


def get_entropy(X):
    numEntries = sum(list(X))
    # 地点总数
    m_bj = len(X)
    shannonEnt = 0.0
    for i in X:
        prob = float(i) / numEntries  # 计算p(xi)
        shannonEnt -= prob * log(prob, 2)  # log base 2
    entropy = shannonEnt / log(m_bj, 2)
    return entropy


def cal():
    nb1 = pd.read_csv('../data/宁波_level1.csv')
    nb2 = pd.read_csv('../data/宁波_level2.csv')
    nb3 = pd.read_csv('../data/宁波_level3.csv')
    nb4 = pd.read_csv('../data/宁波_level4.csv')
    nb5 = pd.read_csv('../data/宁波_level5.csv')
    nb_price = pd.read_csv('../data/宁波人口和房价.csv')
    nb1["e_id"] = nb1["e_id"].astype(int)
    nb2["e_id"] = nb2["e_id"].astype(int)
    nb3["e_id"] = nb3["e_id"].astype(int)
    nb4["e_id"] = nb4["e_id"].astype(int)
    nb5["e_id"] = nb5["e_id"].astype(int)
    # print(nb1)
    num_visitation = []
    ug = nb1.groupby("UserID")
    # 每个人访问了多少个地点
    u1_list = []
    # 都去了哪
    u1_place = []
    u1_price = []
    u_all = []
    u_place = []
    for u in ug:
        u_set = set()
        for row in u[1].values:
            u_set.add(row[-2])
            u_set.add(row[-1])
            u1_place.append(row[-2])
            u1_place.append(row[-1])
            u_place.append(row[-2])
            u_place.append(row[-1])

        u1_list.append(len(u_set))
        u_all.append(len(u_set))
    X1 = list(Counter(u1_place).values())
    e1 = get_entropy(X1)
    print(e1)
    num_visitation.append(np.mean(u1_list))

    for p in set(u1_place):
        pp = nb_price[nb_price["id"] == p]
        # print(pp["total"].values[0], type(pp["total"].values[0]))
        if not np.isnan(pp["total"].values[0]):
            # print(pp, pp["total"])
            u1_price.append(pp["total"].values[0])
    # print(u1_price)
    print(round(np.mean(u1_price), 0))

    ug = nb2.groupby("UserID")
    u2_list = []
    u2_place = []
    u2_price = []
    for u in ug:
        u_set = set()
        for row in u[1].values:
            u_set.add(row[-2])
            u_set.add(row[-1])
            u2_place.append(row[-2])
            u2_place.append(row[-1])
            u_place.append(row[-2])
            u_place.append(row[-1])
        u2_list.append(len(u_set))
        u_all.append(len(u_set))
    num_visitation.append(np.mean(u2_list))
    # 计算流量熵
    X2 = list(Counter(u2_place).values())
    e2 = get_entropy(X2)
    print(e2)
    for p in set(u2_place):
        pp = nb_price[nb_price["id"] == p]
        # print(pp["total"].values[0], type(pp["total"].values[0]))
        if not np.isnan(pp["total"].values[0]):
            # print(pp, pp["total"])
            u2_price.append(pp["total"].values[0])
    # print(u1_price)
    print(round(np.mean(u2_price), 0))

    ug = nb3.groupby("UserID")
    u3_list = []
    u3_place = []
    u3_price = []
    for u in ug:
        u_set = set()
        for row in u[1].values:
            u_set.add(row[-2])
            u_set.add(row[-1])
            u3_place.append(row[-2])
            u3_place.append(row[-1])
            u_place.append(row[-2])
            u_place.append(row[-1])
        u3_list.append(len(u_set))
        u_all.append(len(u_set))
    num_visitation.append(np.mean(u3_list))
    # 计算流量熵
    X3 = list(Counter(u3_place).values())
    e3 = get_entropy(X3)
    print(e3)
    for p in set(u3_place):
        pp = nb_price[nb_price["id"] == p]
        # print(pp["total"].values[0], type(pp["total"].values[0]))
        if not np.isnan(pp["total"].values[0]):
            # print(pp, pp["total"])
            u3_price.append(pp["total"].values[0])
    # print(u1_price)
    print(round(np.mean(u3_price), 0))

    ug = nb4.groupby("UserID")
    u4_list = []
    u4_place = []
    u4_price = []
    for u in ug:
        u_set = set()
        for row in u[1].values:
            u_set.add(row[-2])
            u_set.add(row[-1])
            u4_place.append(row[-2])
            u4_place.append(row[-1])
            u_place.append(row[-2])
            u_place.append(row[-1])
        u4_list.append(len(u_set))
        u_all.append(len(u_set))
    num_visitation.append(np.mean(u4_list))
    # 计算流量熵
    X4 = list(Counter(u4_place).values())
    e4 = get_entropy(X4)
    print(e4)
    for p in set(u4_place):
        pp = nb_price[nb_price["id"] == p]
        # print(pp["total"].values[0], type(pp["total"].values[0]))
        if not np.isnan(pp["total"].values[0]):
            # print(pp, pp["total"])
            u4_price.append(pp["total"].values[0])
    # print(u1_price)
    print(round(np.mean(u4_price), 0))

    ug = nb5.groupby("UserID")
    u5_list = []
    u5_place = []
    u5_price = []
    for u in ug:
        u_set = set()
        for row in u[1].values:
            u_set.add(row[-2])
            u_set.add(row[-1])
            u5_place.append(row[-2])
            u5_place.append(row[-1])
            u_place.append(row[-2])
            u_place.append(row[-1])
        u5_list.append(len(u_set))
        u_all.append(len(u_set))
    num_visitation.append(np.mean(u5_list))
    # 计算流量熵
    X5 = list(Counter(u5_place).values())
    e5 = get_entropy(X5)
    print(e5)
    for p in set(u5_place):
        pp = nb_price[nb_price["id"] == p]
        # print(pp["total"].values[0], type(pp["total"].values[0]))
        if not np.isnan(pp["total"].values[0]):
            # print(pp, pp["total"])
            u5_price.append(pp["total"].values[0])
    # print(u1_price)
    print(round(np.mean(u5_price), 0))
    u_price = []
    for p in set(u_place):
        pp = nb_price[nb_price["id"] == p]
        # print(pp["total"].values[0], type(pp["total"].values[0]))
        if not np.isnan(pp["total"].values[0]):
            # print(pp, pp["total"])
            u_price.append(pp["total"].values[0])
    print(round(np.mean(u_price), 0))

    num_avg = np.mean(u_all)
    # print(num_visitation)
    # print(num_avg)


#

if __name__ == '__main__':
    # cal()
    x = [1, 2, 3, 4, 5]
    jh_num = [7.418092909535452, 7.70757180156658, 7.389380530973451, 9.035087719298245, 6.833333333333333]
    jh_avg = 7.615050651230101
    nb_num = [5.805013927576602, 5.8971407352395095, 5.99219045219801, 5.945221445221446, 6.247111442415207]
    nb_avg = 5.942049469964664
    jh = [0.5766240191551895, 0.6727458052134465, 0.6384883023439074, 0.6285694101178438, 1.2954721734892787]
    jh1 = [1.71143443759501, 1.6889582104094716, 1.717911490036517, 1.5355707053387113, 5.984999999999999]
    nb = [0.8376809155457938, 0.9052812807243248, 0.8901565188288285, 0.9020770097792109, 0.8851032582417804]
    nb1 = [2.0695120874932496, 2.0946070747752095, 2.064158862022608, 2.1058259508769046, 2.1601223102814417]
    nb_avg = 0.8968956223985755
    jh_avg = 0.646899255234839

    fig1 = plt.figure()
    ax1 = fig1.add_subplot(1, 1, 1)
    ax1.plot(x, nb, color='#3e88ad', label='Ningbo')
    ax1.plot([1, 5], [nb_avg, nb_avg], alpha=0.6, linestyle='--', color='#3e88ad')
    ax1.plot(x, jh, color='orange', label='Jinghua')
    ax1.plot([1, 5], [jh_avg, jh_avg], alpha=0.6, linestyle='--', color='orange')
    ax1.set_ylabel("mean range of group activity", fontsize=16)
    ax1.set_xticks(x)
    ax1.legend()
    ax1.set_xlabel("category", fontsize=16)
    # fig1.savefig('../figure/fig15.mean range.pdf', bbox_inches='tight')
    fig1.show()

    fig2 = plt.figure()
    ax2 = fig2.add_subplot(1, 1, 1)
    jh_price = [415.0, 333.0, 286.0, 310.0, 114.0]
    # jh_price_avg = 329
    jh_price_avg = int(np.mean(jh_price))
    nb_price = [int(294.05745856353593), int(278.44575936883626), int(277.0701902748414), int(281.1363855421687),
                int(284.7492537313433)]
    nb_price_avg = np.mean(nb_price)
    # TODO:重新画一遍
    # ax2.plot(x, nb_price, color='#3e88ad', label='Ningbo')
    # ax2.plot([1, 5], [nb_price_avg, nb_price_avg], alpha=0.6, linestyle='--', color='#3e88ad')
    ax2.plot(x[:4], jh_price[:4], color='orange', label='Jinhua')
    ax2.plot([1, 4], [jh_price_avg, jh_price_avg], alpha=0.6, linestyle='--', color='orange')
    ax2.set_xticks(x)
    ax2.tick_params(labelsize=12)
    ax2.set_xlabel("category", fontsize=16)
    ax2.set_ylabel("average price of group activity", fontsize=16)
    ax2.legend()
    # fig2.savefig('../figure/fig14.average price.pdf', bbox_inches='tight')
    fig2.show()
    # plt.xticks(x)
    # plt.show()
    # plt.plot(x, jh_price)
    # plt.plot([1, 5], [jh_price_avg, jh_price_avg])
    # plt.xticks(x)
    # plt.show()
    fig3 = plt.figure()
    ax3 = fig3.add_subplot(1, 1, 1)
    jh_volume_entropy = [0.7936739014862049, 0.8532234058008169, 0.8171988658188964, 0.8234951160680781,
                         0.8976915212270171]
    nb_volume_entropy = [0.7871032484728104, 0.8328762391463381, 0.8231463631998077, 0.7878441820366949,
                         0.7379026694552102]
    ax3.plot(x, nb_volume_entropy, label='Ningbo', color='#3e88ad')
    ax3.plot(x, jh_volume_entropy, label='Jinhua', color='orange')
    ax3.legend()
    ax3.set_xlabel("category", fontsize=16)
    ax3.set_ylabel("entropy of flow volume", fontsize=16)
    ax3.set_xticks(x)
    ax3.tick_params(labelsize=12)
    # fig3.savefig('../figure/entropy of volume.pdf', bbox_inches='tight')
    # fig3.show()
