# -*- coding: utf-8 -*-
# @Time : 2023/7/2 14:17
# @Author : YangYu
# @Email: yangyu.cs@outlook.com
# @File : distribution.py
# @Software: PyCharm


import pandas as pd
from matplotlib import pyplot as plt


def ningbo():
    gap = 2500
    b=40
    plt.figure(figsize=(8, 6))
    data = pd.read_csv("../data/房价/ningbo平均房价.csv")
    data['price1'] = data['单价']
    _len = int(max(data['price1']) / gap)
    print(max(data['price1']), _len)
    bins = [i * gap for i in range(b+1)]
    labels = [i * gap for i in range(b)]
    data["price_label"] = pd.cut(x=data['price1'], bins=bins, labels=labels)

    # print(data["price_label"])
    vc = data.value_counts('price_label', normalize=True)
    xx = vc.index.tolist()
    yy = vc.values.tolist()
    pp = list(zip(xx, yy))
    print(pp)
    pp.sort()
    print(pp)
    xx, yy = zip(*pp)
    plt.plot(xx, yy, label='Location')

    data = pd.read_csv("../data/房价/ningbo房价.csv")
    data['price1'] = data['单价']
    print(data)
    print(max(data['price1']))
    bins = [i * gap for i in range(b+1)]
    labels = [i * gap for i in range(b)]
    data["price_label"] = pd.cut(x=data['price1'], bins=bins, labels=labels)

    # print(data["price_label"])
    vc = data.value_counts('price_label', normalize=True)
    xx = vc.index.tolist()
    yy = vc.values.tolist()
    pp = list(zip(xx, yy))
    print(pp)
    pp.sort()
    print(pp)
    xx, yy = zip(*pp)
    plt.plot(xx, yy, label='House')
    plt.xlabel(r'$\rm \langle$price$\rangle$($\rm RMB/m^2$)', fontsize=18)
    plt.ylabel(r'$\rm $fraction', fontsize=18)
    plt.tick_params(labelsize=14)
    plt.legend(fontsize=18)

    plt.savefig('../figure/3类/fig2-宁波单价分布200.pdf', bbox_inches='tight')
    plt.show()

def jinhua():
    gap = 2800
    b=25
    plt.figure(figsize=(8, 6))
    data = pd.read_csv("../data/金华平均房价200m.csv")
    data['price1'] = data['unit']
    _len = int(max(data['price1']) / gap)
    print(max(data['price1']), _len)
    bins = [i * gap for i in range(b+1)]
    labels = [i * gap for i in range(b)]
    data["price_label"] = pd.cut(x=data['price1'], bins=bins, labels=labels)

    # print(data["price_label"])
    vc = data.value_counts('price_label', normalize=True)
    xx = vc.index.tolist()
    yy = vc.values.tolist()
    pp = list(zip(xx, yy))
    print(pp)
    pp.sort()
    print(pp)
    xx, yy = zip(*pp)
    plt.plot(xx, yy, label='Location')

    data = pd.read_csv("../data/金华房价2&3.csv")
    data['price1'] = data['unit']
    print(data)
    print(max(data['price1']))
    bins = [i * gap for i in range(b+1)]
    labels = [i * gap for i in range(b)]
    data["price_label"] = pd.cut(x=data['price1'], bins=bins, labels=labels)

    # print(data["price_label"])
    vc = data.value_counts('price_label', normalize=True)
    xx = vc.index.tolist()
    yy = vc.values.tolist()
    pp = list(zip(xx, yy))
    print(pp)
    pp.sort()
    print(pp)
    xx, yy = zip(*pp)
    plt.plot(xx, yy, label='House')
    plt.xlabel(r'$\rm \langle$price$\rangle$($\rm RMB/m^2$)', fontsize=18)
    plt.ylabel(r'$\rm $fraction', fontsize=18)
    plt.tick_params(labelsize=14)
    plt.legend(fontsize=18)

    plt.savefig('../figure/3类/fig2-金华单价分布200_.pdf', bbox_inches='tight')
    plt.show()


if __name__ == '__main__':
    ningbo()
    jinhua()
# plt.show()
# print(a, b)
# print(bins)
# price = data['price1'].tolist()
# print(max(price))
# pd.cut(price)
# vc = data.value_counts('price1',normalize=True)
# xx = vc.index.tolist()
# yy = vc.values.tolist()
# pp = list(zip(xx,yy))
# print(pp)
# pp.sort()
# print(pp)
# xx,yy = zip(*pp)
# plt.plot(xx,yy)
# plt.show()
