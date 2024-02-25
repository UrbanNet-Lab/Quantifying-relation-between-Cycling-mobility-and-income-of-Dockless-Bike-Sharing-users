# -*- coding: utf-8 -*-
# @Time : 2023/7/6 11:28
# @Author : YangYu
# @Email: yangyu.cs@outlook.com
# @File : 居住地熵值.py
# @Software: PyCharm

"""
居住多样性是一种衡量某个地区或社区居民多样性程度的指标，即不同群体或人口子群体的分布均衡程度。

在这里衡量的是某个收入类别，单车用户居住地点的分布均衡程度。反映的是一种收入类别中居住地的分布情况。

居住多样性的度量方法有很多种，其中一种常用的指标是熵指数（Entropy Index）。熵指数基于信息熵的概念，可以测量一个地区或社区中各群体之间的均衡程度。
在计算熵指数时，首先需要确定不同群体的比例或占比，并计算每个群体的独立指标值（例如，每个群体的人口比例的自然对数）。
然后，将每个群体的独立指标值乘以其相应的权重（通常为群体占比），最后对所有群体的加权指标值求和。熵指数的取值范围通常为0到1之间，值越接近1表示居住多样性越高，不同群体之间的分布越均衡。

如果熵值越接近0，意味着居住多样性越低，不同群体之间的分布越不均衡。
具体来说，当熵值接近0时，表示某个地区或社区中的居民主要集中在少数几个群体或人口子群体中，而其他群体的存在比例非常小。

较低的熵值可能表明存在居住隔离、种族或民族聚集现象，即不同群体的住所之间存在明显的分离，缺乏社区内部的交流和互动。这可能与社会、经济、文化等因素有关，例如收入差距、种族或民族关系、居住政策等。

根据熵指数判断居住隔离需要对不同群体的熵值进行比较和分析。较高的熵值表示较高的居住多样性和较均衡的分布，而较低的熵值可能暗示着居住隔离。

"""
from collections import Counter
from math import log

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def jh():
    data = pd.read_csv('../data/level/去掉日行程小于2/金华用户分级.csv')
    # data['id'] = data['id']
    data2 = data.dropna(subset=['level'], how='all')
    data2['level'] = data2['level'].astype(int)
    level_group = data2.groupby('level')
    groups = []
    for l in level_group:
        # print(l[1])
        groups.append(l[1]['home'].values)
    print(list(Counter(groups[2]).values()))
    groups[2] = groups[2].tolist()
    groups[2].extend(groups[3].tolist())
    print(list(Counter(groups[2]).values()))
    # print(list(Counter(groups[1]).values()))
    # print(list(Counter(groups[4]).values()))
    entropys = []
    for group in groups:
        # print(Counter(group).values()
        #       )
        vals = list(Counter(group).values())
        numEntries = sum(list(vals))
        # print(numEntries)
        m_bj = len(vals)
        shannonEnt = 0.0
        for i in vals:
            prob = float(i) / numEntries  # 计算p(xi)
            shannonEnt -= prob * log(prob, 2)  # log base 2
        entropy = shannonEnt / log(m_bj, 2)
        entropys.append(entropy)
    category = [1, 2, 3, 4]
    print(entropys)


def nb():
    data = pd.read_csv('../data/房价/宁波用户分类(3).csv')
    level_group = data[["home", "level"]].groupby('level')
    groups = []
    for l in level_group:
        groups.append(l[1]["home"].values.tolist())
    for group in groups:
        # print(Counter(group).values()
        #       )
        vals = list(Counter(group).values())
        numEntries = sum(list(vals))
        # print(numEntries)
        m_bj = len(vals)
        shannonEnt = 0.0
        for i in vals:
            prob = float(i) / numEntries  # 计算p(xi)
            shannonEnt -= prob * log(prob, 2)  # log base 2
        entropy = shannonEnt / log(m_bj, 2)
        print(entropy)


def fig():
    # 金华熵值
    jh_entro = [0.887559391521031, 0.8827391151942392, 0.7697795383887576, 0.6955734609778523, 0.5957965436937068]
    # jh_entro2 = [0.8117125044695996, 0.8812462032500589, 0.8310287559017319, 0.8194680461498933, 0.920619835714305]
    # jh_entro3=[0.8117125044695996, 0.8812462032500589, 0.8310287559017319, 0.8640345680174288]
    nb_entro = [0.8745000251324151, 0.9064492987051294, 0.896206850549239, 0.8978408942921102, 0.8723354506306944]
    # 新的熵值

    jh_entro = [0.814070279004985, 0.8535859633994378, 0.7810416685567126, 0.8671849775176456]
    # 合并3/4组
    jh_entro2 = [0.814070279004985, 0.8535859633994378, 0.7956931233676092]
    # 宁波(3类)
    nb_entro = [0.8871250257284433, 0.8915909447683023, 0.9041551560035902]

    plt.plot([1, 2, 3], jh_entro2[:], label='Jinhua',color='orange')
    plt.plot([1, 2, 3], nb_entro, label='Ningbo')

    plt.xlabel("category", fontsize=16)
    plt.ylabel("Residence diversity", fontsize=16)
    plt.tick_params(labelsize=12)
    category = [1, 2, 3]
    plt.xticks(category)
    plt.legend()
    # plt.savefig('D:/Python_code/北京上海骑行特征/文章中的图/entropy_population.pdf', bbox_inches='tight')
    plt.savefig('../figure/3类/fig10.Residence Diversity.pdf', bbox_inches='tight')
    plt.show()


# plt.plot(category, entropys)
# plt.xticks(category)
# plt.show()
# print(entropys)
if __name__ == '__main__':
    nb()
    fig()
