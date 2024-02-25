# -*- coding: utf-8 -*-
# @Time : 2023/7/10 15:05
# @Author : YangYu
# @Email: yangyu.cs@outlook.com
# @File : 9.distance.py
# @Software: PyCharm
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt


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


def trips_d(bikeid_random1, dis_all):
    dict1 = {}
    for i, j in zip(bikeid_random1, dis_all):
        if (i != np.nan):
            if i not in dict1.keys():
                dict1[i] = [j]
            else:
                dict1[i].append(j)
    bike_count1 = []
    bike_dis1 = []
    for key, value in dict1.items():
        bike_count1.append(len(value))
        bike_dis1.append(round(np.mean(value), 3))
    #    print(np.sum(bike_count1))
    count_full1 = pd.Series(bike_count1).value_counts(normalize=True)
    dis_x1, dis_y1 = pdf1(bike_dis1, 1)
    trips_x1, trips_y1 = (list(t) for t in zip(*sorted(zip(count_full1.index, count_full1.values))))
    return trips_x1, trips_y1, dis_x1, dis_y1


jh_dis_x1 = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5]
jh_dis_y1 = [0.5354523227383863, 0.3594132029339853, 0.07823960880195599, 0.009779951100244499, 0.007334963325183374,
             0.007334963325183374, 0.0024449877750611247]
jh_dis_x2 = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5]
jh_dis_y2 = [0.49434290687554394, 0.39599651871192343, 0.07571801566579635, 0.02349869451697128, 0.006092254134029591,
             0.0026109660574412533, 0.0008703220191470844, 0.0008703220191470844]
jh_dis_x3 = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5]
jh_dis_y3 = [0.5486725663716814, 0.34513274336283184, 0.08185840707964602, 0.015486725663716814, 0.00663716814159292,
             0.0022123893805309734]
jh_dis_x4 = [0.5, 1.5, 2.5, 3.5]
jh_dis_y4 = [0.5614035087719298, 0.3684210526315789, 0.05263157894736842, 0.017543859649122806]
jh_dis_x5 = [0.5, 1.5]
jh_dis_y5 = [0.6666666666666666, 0.3333333333333333]

nb_dis_x1 = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5]
nb_dis_y1 = [0.5654596100278552, 0.3500464252553389, 0.06638811513463325, 0.012999071494893221, 0.002785515320334262,
             0.0009285051067780873, 0.0009285051067780873, 0.00046425255338904364]
nb_dis_x2 = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 9.5, 11.5]
nb_dis_y2 = [0.5523748438713162, 0.355534550855754, 0.06923674172096006, 0.016574958646997266, 0.003814603517537049,
             0.001451574789859231, 0.0005401208520406441, 0.0002363028727677818, 6.751510650508052e-05,
             0.00010127265975762077, 6.751510650508052e-05]
nb_dis_x3 = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 10.5, 11.5, 12.5]
nb_dis_y3 = [0.549376495780325, 0.3502330268295755, 0.07186043582315153, 0.02009069152286182, 0.0059201410757022295,
             0.0014485451568207583, 0.0005668220178863837, 0.00025192089683839276, 6.298022420959819e-05,
             6.298022420959819e-05, 6.298022420959819e-05, 6.298022420959819e-05]
nb_dis_x4 = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 9.5]
nb_dis_y4 = [0.5571095571095571, 0.3569347319347319, 0.06905594405594405, 0.01252913752913753, 0.002331002331002331,
             0.0008741258741258741, 0.0008741258741258741, 0.0002913752913752914]
nb_dis_x5 = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5]
nb_dis_y5 = [0.4975773387998509, 0.38874394334699963, 0.0827431979127842, 0.021244875139768915, 0.00633619083115915,
             0.002609019754006709, 0.0003727171077152441, 0.0003727171077152441]

fig, axes = plt.subplots(1, 2)

axes[0].plot(jh_dis_x1, jh_dis_y1)
axes[0].plot(jh_dis_x2, jh_dis_y2)
axes[0].plot(jh_dis_x3, jh_dis_y3)
axes[0].plot(jh_dis_x4, jh_dis_y4)
axes[0].plot(jh_dis_x5, jh_dis_y5)

axes[1].plot(nb_dis_x1, nb_dis_y1)
axes[1].plot(nb_dis_x2, nb_dis_y2)
axes[1].plot(nb_dis_x3, nb_dis_y3)
axes[1].plot(nb_dis_x4, nb_dis_y4)
axes[1].plot(nb_dis_x5, nb_dis_y5)

axes[0].set_xscale('log')
axes[0].set_yscale('log')
axes[1].set_xscale('log')
axes[1].set_yscale('log')


def cal():
    for i in range(1, 4):
        data = pd.read_csv(f'../data/level/过滤/3类/jinhua_level{i}_1.csv')
        dis_all = data['d(km)']
        userid = data['UserID']
        trip_x, trip_y, dis_x, dis_y = trips_d(userid, dis_all)
        print(dis_x, dis_y)


def fig():
    color = [(185 / 255, 94 / 255, 19 / 255),
             (254 / 255, 217 / 255, 78 / 255),
             (254 / 255, 130 / 255, 21 / 255),
             (64 / 255, 184 / 255, 204 / 255),
             (61 / 255, 118 / 255, 127 / 255)
             ]
    nb_x1 = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5]
    nb_y1 = [
        0.5656068069861173, 0.35064935064935066, 0.06448723690103, 0.013882669055082848, 0.003134796238244514,
        0.0013434841021047917, 0.0008956560680698612]
    nb_x2 = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5, 11.5]
    nb_y2 = [
        0.5454229784278831, 0.3672902469725248, 0.06827553279222189, 0.014410347671339903, 0.0031251356395676894,
        0.001085116541516559, 0.00021702330830331178, 4.3404661660662356e-05, 4.3404661660662356e-05,
        8.680932332132471e-05]
    nb_x3 = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5]
    nb_y3 = [
        0.546757457846952, 0.36219195849546043, 0.06945525291828794, 0.01556420233463035, 0.004669260700389105,
        0.0007133592736705577, 0.0005836575875486381, 6.485084306095979e-05]
    fig2 = plt.figure(figsize=(8, 6))
    ax2 = fig2.add_subplot(1, 1, 1)
    ax2.plot(nb_x1, nb_y1, label='1', color=color[0], linewidth=2)
    ax2.plot(nb_x2, nb_y2, label='2', color=color[2], linewidth=2)
    ax2.plot(nb_x3, nb_y3, label='3', color=color[4], linewidth=2)
    ax2.legend()
    ax2.set_xscale('log')
    ax2.set_yscale('log')
    ax2.set_xlabel(r'$\rm log_{10}\langle$d$\rangle$($\rm km$)', fontsize=18)
    ax2.set_ylabel(r'$\rm log_{10}P$($\rm d$)', fontsize=18)
    plt.tick_params(labelsize=14)

    fig2.savefig('../figure/3类/travel_distance_ningbo.pdf', bbox_inches='tight')
    fig2.show()

    jh_x1 = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5]
    jh_y1 = [0.5068493150684932, 0.3801369863013699, 0.08561643835616438, 0.010273972602739725, 0.00684931506849315,
             0.010273972602739725]
    jh_x2 = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5]
    jh_y2 = [0.4926829268292683, 0.41341463414634144, 0.07439024390243902, 0.014634146341463415, 0.003658536585365854,
             0.0012195121951219512]
    jh_x3 = [0.5, 1.5, 2.5, 3.5, 4.5]
    jh_y3 = [0.5459459459459459, 0.3675675675675676, 0.07567567567567568, 0.008108108108108109, 0.002702702702702703]
    fig2 = plt.figure(figsize=(8, 6))
    ax2 = fig2.add_subplot(1, 1, 1)
    ax2.plot(jh_x1, jh_y1, label='1', color=color[0], linewidth=2)
    ax2.plot(jh_x2, jh_y2, label='2', color=color[2], linewidth=2)
    ax2.plot(jh_x3, jh_y3, label='3', color=color[4], linewidth=2)
    ax2.legend()
    ax2.set_xscale('log')
    ax2.set_yscale('log')
    ax2.set_xlabel(r'$\rm log_{10}\langle$d$\rangle$($\rm km$)', fontsize=18)
    ax2.set_ylabel(r'$\rm log_{10}P$($\rm d$)', fontsize=18)
    plt.tick_params(labelsize=14)
    plt.legend()

    fig2.savefig('../figure/3类/travel_distance_jinhua.pdf', bbox_inches='tight')
    fig2.show()


if __name__ == '__main__':
    # cal()
    fig()