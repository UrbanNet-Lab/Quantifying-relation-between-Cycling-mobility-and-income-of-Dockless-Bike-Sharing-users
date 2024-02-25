# -*- coding: utf-8 -*-
# @Time : 2023/7/7 12:47
# @Author : YangYu
# @Email: yangyu.cs@outlook.com
# @File : 4.按地点分类用户比率图.py
# @Software: PyCharm
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def log_pdf(x, y):
    # bins=np.logspace(2, 4, 20,base=10)#北京
    # bins=np.logspace(1.9, 3.8, 20,base=10)#上海
    bins = np.logspace(1.9, 4, 20, base=10)
    bins2 = list(bins)
    bins_all = {}
    for i in range(len(bins)):
        bins_all[bins[i]] = []
    # widths = (bins[1:] - bins[:-1])
    for i in range(len(x)):
        if (x[i] > 0):
            for j in range(len(bins)):
                if (x[i] < bins[j]):
                    bins_all[bins[j - 1]].append(y[i])
                    break
                if (x[i] == bins[j]):
                    bins_all[bins[j]].append(y[i])
                    break
    x_new = []
    y_new = []
    bar = []
    for key, value in bins_all.items():
        if (len(value) > 0):
            #            index_this=bins2.index(key)
            #            y_new.append(np.sum(value)/widths[index_this])
            # print(value)
            y_new.append(np.mean(value))
            #             v = np.log10(value)
            # bar.append(np.std(value,ddof=1))

            x_new.append(key)
    return x_new, y_new


def log_pdf(x, y, num):
    #    bins=np.logspace(0, 4, 20,base=2)
    bins = np.logspace(0, 4, num)
    # print(bins)
    bins2 = list(bins)
    bins_all = {}
    for i in range(len(bins) - 1):
        bins_all[bins[i]] = []
    widths = (bins[1:] - bins[:-1])
    for i in range(len(x)):
        if (x[i] >= 1):
            for j in range(len(bins)):
                #    bins[j]<=xi<bins[j+1],放到bins[j]里面去
                if (x[i] < bins[j]):
                    bins_all[bins[j - 1]].append(y[i])
                    break
                if (x[i] == bins[j]):
                    bins_all[bins[j]].append(y[i])
                    break
    x_new = []
    y_new = []
    for key, value in bins_all.items():
        if (len(value) > 0):
            index_this = bins2.index(key)
            # 1.bins里面的和除以宽度
            #            y_new.append(np.sum(value)/widths[index_this])
            # 2.bins里面的平均值
            y_new.append(np.mean(value))
            x_new.append(key)

    return x_new, y_new


# data = pd.read_csv("../data/金华用户比率.csv")
data = pd.read_csv("../data/房价/金华有房价和用户的地点.csv")
data1 = pd.read_csv("../data/房价/宁波有房价和用户的地点.csv")
plt.figure(figsize=(7,6))
price = data["total"].values
print(max(price))
ur = data["user_ratio"].values

k = 25
temp = list(sorted(zip(price, ur)))
x, y = zip(*temp)
x, y = log_pdf(x, y, k)

price = data1["total"].values
print(max(price))
ur = data1["user_ratio"].values

temp = list(sorted(zip(price, ur)))
x1, y1 = zip(*temp)
x1, y1 = log_pdf(x1, y1, k)
# plt.scatter(x, y, edgecolor='blue', facecolor='none', s=10, linewidths=1.5)
# plt.plot(x, y, label='Jinghua')
# plt.scatter(x1, y1)
plt.loglog(x, y, label='Jinhua', color="orange")
plt.loglog(x, y, '.', color="orange", markersize=10, marker='o', markerfacecolor='white')

plt.loglog(x1, y1, label='Ningbo')
plt.loglog(x1, y1, '.', color="b", markersize=10, marker='o', markerfacecolor='white')


plt.xscale('log')
plt.yscale('log')
plt.xlabel(r'$\rm log_{10}\langle total\ price \rangle\ (10^4 RMB/house)$',fontsize=20)
plt.ylabel(r'$\rm log_{10}(user\ ratio)$',fontsize=20)
plt.legend(fontsize=14)
plt.tick_params(labelsize=14)
# plt.xlabel(r'$\rm log_{10}house\ price\ (10^4 RMB/house)$', fontsize=18)
# plt.ylabel(r'$\rm log_{10}(user ratio)$', fontsize=18)
# plt.savefig('../figure/3类/ratio_total_price_2.pdf', bbox_inches='tight')
plt.show()
