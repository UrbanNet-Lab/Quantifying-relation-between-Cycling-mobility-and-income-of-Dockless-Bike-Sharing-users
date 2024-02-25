# -*- coding: utf-8 -*-
# @Time : 2023/7/10 14:35
# @Author : YangYu
# @Email: yangyu.cs@outlook.com
# @File : 8.gyration.py
# @Software: PyCharm
from math import radians, sin, asin, sqrt, cos

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


def pdf1(data, step):
    all_num = len(data)
    x_range = np.arange(0, 100, step)
    #    y=np.zeros((len(x_range)-1), dtype=np.int)
    y = np.zeros(len(x_range) - 1)
    x = x_range[:-1] + step / 2

    for data1 in data:
        a = int(data1 // step)
        y[a] = y[a] + 1
    y = y / all_num
    x1 = []
    y1 = []
    for i in range(len(x)):
        if (y[i] != 0):
            x1.append(x[i])
            y1.append(y[i])
    return x1, y1


# def gyration(bikeid_random1, endx, endy):
#     dict_gy = {}
#     for i, j, k in zip(bikeid_random1, endx, endy):
#         if (i != np.nan):
#             if i not in dict_gy.keys():
#                 dict_gy[i] = [[j, k]]
#             else:
#                 dict_gy[i].append([j, k])
#     bike_end = []
#     for key, value in dict_gy.items():
#         bike_point1_array = np.array(value)
#         endx_mid = np.mean(bike_point1_array[:, 0])
#         endy_mid = np.mean(bike_point1_array[:, 1])
#         dis1 = 0
#         for point1 in value:
#             dis1 = dis1 + geodistance(point1[0], point1[1], endx_mid, endy_mid)
#         bike_end.append(dis1 / len(value))
#     bike_end = [no for no in bike_end if no < 100 and no >= 1]
#     gy_x, gy_y = pdf1(bike_end, 1)
#     return gy_x, gy_y

def gyration(endx, endy):
    r_end = []
    endx_mid = np.mean(endx)
    endy_mid = np.mean(endy)
    dis1 = 0
    for ix, jy in zip(endx, endy):
        dis1 = dis1 + geodistance(ix, jy, endx_mid, endy_mid)
    r_end.append(dis1 / len(endx))
    return r_end


def mean_gyration(bikeid_random1, endx, endy):
    dict_gy = {}
    for i, j, k in zip(bikeid_random1, endx, endy):
        if (i != np.nan):
            if i not in dict_gy.keys():
                dict_gy[i] = [[j, k]]
            else:
                dict_gy[i].append([j, k])
    bike_end = []
    for key, value in dict_gy.items():
        bike_point1_array = np.array(value)
        endx_mid = np.mean(bike_point1_array[:, 0])
        endy_mid = np.mean(bike_point1_array[:, 1])
        dis1 = 0
        for point1 in value:
            dis1 = dis1 + geodistance(point1[0], point1[1], endx_mid, endy_mid)
        bike_end.append(dis1 / len(value))
    bike_end = [no for no in bike_end if no < 100]
    return np.mean(bike_end)


# def mean_gyration(bikeid_random1, endx, endy):
#     dict_gy = {}
#     for i, j, k in zip(bikeid_random1, endx, endy):
#         if (i != np.nan):
#             if i not in dict_gy.keys():
#                 dict_gy[i] = [[j, k]]
#             else:
#                 dict_gy[i].append([j, k])
#     bike_end = []
#     for key, value in dict_gy.items():
#         bike_point1_array = np.array(value)
#         endx_mid = np.mean(bike_point1_array[:, 0])
#         endy_mid = np.mean(bike_point1_array[:, 1])
#         dis1 = 0
#         for point1 in value:
#             dis1 = dis1 + geodistance(point1[0], point1[1], endx_mid, endy_mid)
#         bike_end.append(dis1 / len(value))
#     bike_end = [no for no in bike_end if no < 100]
#     return np.mean(bike_end)


def cal():
    for i in range(1, 4):
        data = pd.read_csv(f'../data/level/过滤/3类/jinhua_level{i}.csv')
        # userid = data['UserID'].values
        endx1, endy1 = data['EndLng'].values, data['EndLat'].values
        # print(endx1, endy1)
        # m = mean_gyration(userid, endx1, endy1)
        # print(m)
        r = gyration(endx1, endy1)
        print(r)
    # data = pd.read_csv('../data/level/ningbo_level.csv')
    #
    # userid = data['UserID'].values
    #
    # endx, endy = data['EndLng'], data['EndLat']
    # m = mean_gyration(userid, endx, endy)
    # print(m)
    # data = pd.read_csv('../data/level/jinhua_level.csv')
    # userid = data['UserID'].values
    #
    # endx, endy = data['EndLng'], data['EndLat']
    # m = mean_gyration(userid, endx, endy)
    # print(m)


jh_x1 = [0.5, 1.5, 2.5, 3.5, 4.5]
jh_y1 = [0.8557457212713936, 0.1100244498777506, 0.02444987775061125, 0.004889975550122249, 0.004889975550122249]
jh_x2 = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5]
jh_y2 = [0.7963446475195822, 0.1496953872932985, 0.04264577893820714, 0.007832898172323759, 0.0008703220191470844,
         0.0017406440382941688, 0.0008703220191470844]
jh_x3 = [0.5, 1.5, 2.5, 3.5, 4.5, 6.5]
jh_y3 = [0.7920353982300885, 0.1592920353982301, 0.033185840707964605, 0.008849557522123894, 0.004424778761061947,
         0.0022123893805309734]
jh_x4 = [0.5, 1.5, 2.5]
jh_y4 = [0.8245614035087719, 0.14035087719298245, 0.03508771929824561]
jh_x5 = [0.5, 5.5]
jh_y5 = [0.8333333333333334, 0.16666666666666666]

nb_x1 = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5]
nb_y1 = [0.7423398328690808, 0.15088207985143917, 0.06128133704735376, 0.031569173630454965, 0.008356545961002786,
         0.00510677808727948, 0.00046425255338904364]

nb_x2 = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 14.5]
nb_y2 = [0.7108665563919927, 0.1737501265908247, 0.06336292745501806, 0.03058434324680147, 0.014853323431117713,
         0.004523512135840394, 0.0016541201093744726, 0.0003375755325254026, 3.375755325254026e-05,
         3.375755325254026e-05]

nb_x3 = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5]
nb_y3 = [0.7110467313263635, 0.17420330016374858, 0.06505857160851493, 0.031742033001637485, 0.012973926187177227,
         0.0039047739009950874, 0.0009447033631439728, 0.00012596044841919638]
nb_x4 = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5]
nb_y4 = [0.7121212121212122, 0.1652097902097902, 0.0673076923076923, 0.03671328671328671, 0.013986013986013986,
         0.004079254079254079, 0.0005827505827505828]

nb_x5 = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5]
nb_y5 = [0.7349981364144614, 0.16026835631755498, 0.04696235557212076, 0.029444651509504285, 0.019381289601192696,
         0.007454342154304882, 0.0011181513231457323, 0.0003727171077152441]
jh = [0.5766240191551895, 0.6727458052134465, 0.6384883023439074, 0.6285694101178438, 1.2954721734892787]
jh1 = [1.71143443759501, 1.6889582104094716, 1.717911490036517, 1.5355707053387113, 5.984999999999999]
nb = [0.8376809155457938, 0.9052812807243248, 0.8901565188288285, 0.9020770097792109, 0.8851032582417804]
nb1 = [2.0695120874932496, 2.0946070747752095, 2.064158862022608, 2.1058259508769046, 2.1601223102814417]


def fig_nb_3():
    color = [(185 / 255, 94 / 255, 19 / 255),
             (254 / 255, 217 / 255, 78 / 255),
             (254 / 255, 130 / 255, 21 / 255),
             (64 / 255, 184 / 255, 204 / 255),
             (61 / 255, 118 / 255, 127 / 255)
             ]
    """
    宁波分三类
    :return:
    """
    nb_x1 = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5]
    nb_y1 = [0.6945812807881774, 0.1921182266009852, 0.06851768920734438, 0.033139274518584866, 0.006717420510523959,
             0.0049261083743842365]

    nb_x2 = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 14.5]
    nb_y2 = [0.6725986370936239, 0.19892356439081557, 0.07187811971005686, 0.03407265940361995, 0.015365250227874473,
             0.004817917444333521, 0.0018664004514084812, 0.0003906419549459612, 4.3404661660662356e-05,
             4.3404661660662356e-05]
    nb_x3 = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5]
    nb_y3 = [0.6721141374837873, 0.19993514915693905, 0.07120622568093385, 0.036381322957198446, 0.01536964980544747,
             0.004085603112840467, 0.0008430609597924773, 6.485084306095979e-05]

    fig2 = plt.figure(figsize=(8, 6))
    ax2 = fig2.add_subplot(1, 1, 1)
    ax2.plot(nb_x1, nb_y1, label='1', color=color[0], linewidth=2)
    ax2.plot(nb_x2, nb_y2, label='2', color=color[2], linewidth=2)
    ax2.plot(nb_x3, nb_y3, label='3', color=color[4], linewidth=2)
    ax2.legend()
    ax2.set_xscale('log')
    ax2.set_yscale('log')
    ax2.set_xlabel('log' + r'$\rm_{10}r_g(km)$', fontsize=18)
    ax2.set_ylabel('log' + r'$\rm_{10}P(r_g)$', fontsize=18)
    plt.tick_params(labelsize=14)

    fig2.savefig('../figure/3类/radius_of_gyration_ningbo.pdf', bbox_inches='tight')
    fig2.show()


def fig_jh_3():
    color = [(185 / 255, 94 / 255, 19 / 255),
             (254 / 255, 217 / 255, 78 / 255),
             (254 / 255, 130 / 255, 21 / 255),
             (64 / 255, 184 / 255, 204 / 255),
             (61 / 255, 118 / 255, 127 / 255)
             ]
    jh_x1 = [0.5, 1.5, 2.5, 3.5, 4.5]
    jh_y1 = [0.8253424657534246, 0.1404109589041096, 0.0273972602739726, 0.003424657534246575, 0.003424657534246575]
    jh_x2 = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5]
    jh_y2 = [0.751219512195122, 0.18536585365853658, 0.04878048780487805, 0.01097560975609756, 0.0012195121951219512,
             0.0012195121951219512, 0.0012195121951219512]
    jh_x3 = [0.5, 1.5, 2.5, 3.5, 4.5]
    jh_y3 = [0.7567567567567568, 0.1918918918918919, 0.043243243243243246, 0.002702702702702703, 0.005405405405405406]
    fig2 = plt.figure(figsize=(8, 6))
    ax2 = fig2.add_subplot(1, 1, 1)
    ax2.plot(jh_x1, jh_y1, label='1', color=color[0], linewidth=2)
    ax2.plot(jh_x2, jh_y2, label='2', color=color[2], linewidth=2)
    ax2.plot(jh_x3, jh_y3, label='3', color=color[4], linewidth=2)
    ax2.legend()
    ax2.set_xscale('log')
    ax2.set_yscale('log')
    ax2.set_xlabel('log' + r'$\rm_{10}r_g(km)$', fontsize=18)
    ax2.set_ylabel('log' + r'$\rm_{10}P(r_g)$', fontsize=18)
    plt.tick_params(labelsize=14)

    fig2.savefig('../figure/3类/radius_of_gyration_jinhua.pdf', bbox_inches='tight')
    fig2.show()


if __name__ == '__main__':
    # fig_nb_3()
    # fig_jh_3()
    cal()
    # cal()
    # plt.plot([1, 2, 3, 4, 5], nb)
    # plt.xticks([1, 2, 3, 4, 5])
    # plt.show()
    # fig1 = plt.figure()
    # ax1 = fig1.add_subplot(1, 1, 1)
    # ax1.plot(jh_x1, jh_y1, label='1')
    # ax1.plot(jh_x2, jh_y2, label='2')
    # ax1.plot(jh_x3, jh_y3, label='3')
    # ax1.plot(jh_x4, jh_y4, label='4')
    # ax1.plot(jh_x5, jh_y5, label='5')
    # ax1.legend()
    # ax1.set_xscale('log')
    # ax1.set_yscale('log')
    # ax1.set_xlabel('log' + r'$_{10}r_g$', fontsize=16)
    # ax1.set_ylabel('log' + r'$_{10}P(r_g)$', fontsize=16)
    # fig1.savefig('../figure/fig11.金华gyration.pdf', bbox_inches='tight')
    # fig1.show()
    # z`
    # fig2 = plt.figure()
    # ax2 = fig2.add_subplot(1, 1, 1)
    # ax2.plot(nb_x1, nb_y1, label='1')
    # ax2.plot(nb_x2, nb_y2, label='2')
    # ax2.plot(nb_x3, nb_y3, label='3')
    # ax2.plot(nb_x4, nb_y4, label='4')
    # ax2.plot(nb_x5, nb_y5, label='5')
    # ax2.legend()
    # ax2.set_xscale('log')
    # ax2.set_yscale('log')
    # ax2.set_xlabel('log' + r'$_{10}r_g$', fontsize=16)
    # ax2.set_ylabel('log' + r'$_{10}P(r_g)$', fontsize=16)
    # fig2.savefig('../figure/fig11.宁波gyration.pdf', bbox_inches='tight')
    #
    # fig2.show()
