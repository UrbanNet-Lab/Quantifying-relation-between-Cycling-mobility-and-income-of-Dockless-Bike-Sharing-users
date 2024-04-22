# -*- coding: utf-8 -*-
# @Time : 2023/12/25 15:12
# @Author : YangYu
# @Email: yangyu.cs@outlook.com
# @File : travel_time.py
# @Software: PyCharm
from collections import Counter

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit


def power_law(x, a, b):
    return a * pow(x, b)


def t_power_law(x, a, b1, b2):
    return a * pow(x, -b1) * np.exp((-b2) * x)


def travel_time():
    plt.figure(figsize=(8, 6))
    nb_path = 'ningbo_level3.csv'
    jh_path = 'jinhua_level3.csv'
    data = pd.read_csv(jh_path)
    # data["StartTime"] = pd.to_datetime(data["StartTime"])
    # data["day"] = data["StartTime"].dt.day
    u_group = data.groupby('UserID')["TripID"].count()
    # days = []
    trips = u_group.values
    print(trips)
    trips1 = []
    for t in trips:
        if t < 130:
            trips1.append(t)
    # print(days)
    x, y = zip(*sorted(list(Counter(trips1).items())))
    y = np.array(y) / np.sum(y)
    # prob = [_y / len(trips) for _y in y]
    # print(x)
    # print(y)
    # print(prob)
    # plt.scatter(x,y)
    cut = -1
    popt, pcov = curve_fit(t_power_law, x[:cut], y[:cut], maxfev=100000)  # popt数组中，三个值分别是待求参数a,b,c
    print(popt)
    fy = [t_power_law(i, popt[0], popt[1], popt[2]) for i in x]
    plt.plot(x[:cut], fy[:cut], '--', color='red')
    plt.scatter(x[:cut], y[:cut], c='orange')
    # plt.scatter(x, y)
    freq = y / np.sum(y)
    ccdf = 1 - np.cumsum(freq)
    # plt.plot(x, ccdf)
    # plt.xlim(right=125)
    plt.yscale('log')
    plt.xscale('log')
    # plt.savefig("../figure/fig4.金华用户次数分布.pdf", bbox_inches='tight')
    plt.xlabel('# trips', fontsize=16)
    plt.ylabel('P(#)', fontsize=16)
    # plt.ylabel('CCDF', fontsize=16)
    plt.tick_params(labelsize=14)
    # plt.savefig('travel_time_jinhua.pdf', bbox_inches='tight')
    # plt.savefig('travel_time_jinhua.png', bbox_inches='tight')
    # plt.savefig('travel_time_ningbo.pdf', bbox_inches='tight')
    # plt.savefig('travel_time_ningbo.png', bbox_inches='tight')
    plt.show()


if __name__ == '__main__':
    travel_time()
