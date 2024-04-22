# -*- coding: utf-8 -*-
# @Time : 2023/7/19 21:41
# @Author : YangYu
# @Email: yangyu.cs@outlook.com
# @File : 统计地点流量.py
# @Software: PyCharm
from collections import Counter
from math import log

import pandas as pd


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


def cal2(path):
    data = pd.read_csv(path)
    data['e_id'] = data['e_id'].astype(int)
    data.to_csv(path, index=False)
    s = data['s_id'].values.tolist()
    e = data['e_id'].values.tolist()
    all_place = s
    all_place.extend(e)
    # data4 = pd.read_csv('jinhua_level4.csv')
    # data4['e_id'] = data4['e_id'].astype(int)
    # data4.to_csv('jinhua_level4.csv', index=False)
    # all_place.extend(data4['s_id'].values.tolist())
    # all_place.extend(data4['e_id'].values.tolist())
    ids, nums = zip(*list(Counter(all_place).items()))
    return ids, nums


if __name__ == '__main__':
    path = '3类/ningbo_level3.csv'
    ids, nums = cal2(path)
    e = get_entropy(nums)
    data = pd.read_csv('../../房价/宁波有房价和用户的地点.csv')
    place = data['id']
    price = data['total']
    dict1 = dict(zip(place, price))
    data2 = pd.DataFrame(columns=['id', 'nums'])
    data2['id'] = ids
    data2['nums'] = nums
    price = []
    for ii in ids:
        if ii in dict1:
            price.append(dict1[ii])
        else:
            price.append(0)
    data2['price'] = price
    data2.to_csv('3类/宁波3类用户的流量分布.csv', index=False)
    # 0.7979453539213233 0.8562899559099179 0.837291491175352
