# -*- coding: utf-8 -*-
# @Time : 2023/7/10 15:36
# @Author : YangYu
# @Email: yangyu.cs@outlook.com
# @File : 10.平均房价&访问地点数.py
# @Software: PyCharm
from collections import Counter
from math import log
from math import radians, sin, asin, sqrt, cos
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
    bike_end = [no for no in bike_end if no < 100 and no > 1]
    return np.mean(bike_end)


def cal():
    jh1 = pd.read_csv('../data/level/去掉日行程小于2/jinhua_level1.csv')
    jh2 = pd.read_csv('../data/level/去掉日行程小于2/jinhua_level2.csv')
    jh3 = pd.read_csv('../data/level/去掉日行程小于2/jinhua_level3.csv')
    jh4 = pd.read_csv('../data/level/去掉日行程小于2/jinhua_level4.csv')
    # nb5 = pd.read_csv('../data/宁波_level5.csv')
    jh_price = pd.read_csv('../data/房价/金华有房价和用户的地点.csv')
    jh1["e_id"] = jh1["e_id"].astype(int)
    jh2["e_id"] = jh2["e_id"].astype(int)
    jh3["e_id"] = jh3["e_id"].astype(int)
    jh4["e_id"] = jh4["e_id"].astype(int)
    # nb5["e_id"] = nb5["e_id"].astype(int)
    # print(nb1)
    num_visitation = []
    ug = jh1.groupby("UserID")
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
        pp = jh_price[jh_price["id"] == p]
        # print(pp["total"].values[0], type(pp["total"].values[0]))
        if not np.isnan(pp["total"].values[0]):
            # print(pp, pp["total"])
            u1_price.append(pp["total"].values[0])
    # print(u1_price)
    print(round(np.mean(u1_price), 0))

    ug = jh2.groupby("UserID")
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
        pp = jh_price[jh_price["id"] == p]
        # print(pp["total"].values[0], type(pp["total"].values[0]))
        if not np.isnan(pp["total"].values[0]):
            # print(pp, pp["total"])
            u2_price.append(pp["total"].values[0])
    # print(u1_price)
    print(round(np.mean(u2_price), 0))

    ug = jh3.groupby("UserID")
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

    # print(u1_price)
    # print(round(np.mean(u3_price), 0))

    ug = jh4.groupby("UserID")
    u4_list = []
    u4_place = []
    u4_price = []
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
        pp = jh_price[jh_price["id"] == p]
        # print(pp["total"].values[0], type(pp["total"].values[0]))
        if not np.isnan(pp["total"].values[0]):
            # print(pp, pp["total"])
            u3_price.append(pp["total"].values[0])
    # num_visitation.append(np.mean(u4_list))
    # 计算流量熵
    # X4 = list(Counter(u4_place).values())
    # e4 = get_entropy(X4)
    # print(e4)
    # for p in set(u4_place):
    #     pp = nb_price[nb_price["id"] == p]
    #     # print(pp["total"].values[0], type(pp["total"].values[0]))
    #     if not np.isnan(pp["total"].values[0]):
    #         # print(pp, pp["total"])
    #         u4_price.append(pp["total"].values[0])
    # # print(u1_price)
    # print(round(np.mean(u4_price), 0))

    # ug = nb5.groupby("UserID")
    # u5_list = []
    # u5_place = []
    # u5_price = []
    # for u in ug:
    #     u_set = set()
    #     for row in u[1].values:
    #         u_set.add(row[-2])
    #         u_set.add(row[-1])
    #         u5_place.append(row[-2])
    #         u5_place.append(row[-1])
    #         u_place.append(row[-2])
    #         u_place.append(row[-1])
    #     u5_list.append(len(u_set))
    #     u_all.append(len(u_set))
    # num_visitation.append(np.mean(u5_list))
    # # 计算流量熵
    # X5 = list(Counter(u5_place).values())
    # e5 = get_entropy(X5)
    # print(e5)
    # for p in set(u5_place):
    #     pp = nb_price[nb_price["id"] == p]
    #     # print(pp["total"].values[0], type(pp["total"].values[0]))
    #     if not np.isnan(pp["total"].values[0]):
    #         # print(pp, pp["total"])
    #         u5_price.append(pp["total"].values[0])
    # # print(u1_price)
    # print(round(np.mean(u5_price), 0))
    u_price = []
    for p in set(u_place):
        pp = jh_price[jh_price["id"] == p]
        # print(pp["total"].values[0], type(pp["total"].values[0]))
        if not np.isnan(pp["total"].values[0]):
            # print(pp, pp["total"])
            u_price.append(pp["total"].values[0])
    print(round(np.mean(u_price), 0))

    num_avg = np.mean(u_all)
    # print(num_visitation)
    # print(num_avg)


def geodistance(lng1, lat1, lng2, lat2):
    lng1, lat1, lng2, lat2 = map(radians, [float(lng1), float(lat1), float(lng2), float(lat2)])
    # lng1, lat1, lng2, lat2 = map(radians, [lng1, lat1, lng2, lat2])
    dlon = lng2 - lng1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    dis = 2 * asin(sqrt(a)) * 6371 * 1000  # 地球平均半径，6371km
    dis = round(dis / 1000, 3)
    return dis


def fig_range():
    jh = [2.436027092274684,
          2.4756989021956097,
          3.7871006981172153]
    jh_avg = 2.8468502841677963

    # 宁波分3类

    nb = [3.789480379619059
        , 3.8859726070304372
        , 4.085395088869553]

    nb_avg = 3.9565931637112546

    fig1 = plt.figure()
    ax1 = fig1.add_subplot(1, 1, 1)
    ax1.plot([1, 2, 3], jh, color='orange', label='Jinghua', )
    ax1.plot([1, 2, 3], nb, color='#3e88ad', label='Ningbo')
    ax1.plot([1, 3], [jh_avg, jh_avg], alpha=0.6, linestyle='--', color='orange')
    ax1.plot([1, 3], [nb_avg, nb_avg], alpha=0.6, linestyle='--', color='#3e88ad')

    ax1.set_ylabel("Dispersion range(km)", fontsize=16)
    ax1.set_xticks([1, 2, 3])
    ax1.legend()
    ax1.set_xlabel("category", fontsize=16)
    fig1.savefig('../figure/3类/group_activity_range_income_level_3.pdf', bbox_inches='tight')
    fig1.show()


def fig_price():
    fig2 = plt.figure()
    ax2 = fig2.add_subplot(1, 1, 1)
    jh_price = [415.0, 333.0, 286.0, 310.0, 114.0]
    # jh_price_avg = 329
    jh_price_avg = int(np.mean(jh_price))
    # 金华三类用户的平均房价
    jh_price = [426.21126638053653, 329.6425347909653, 283.6886078286691]
    jh_price_avg = 338.2642412799231
    # 金华加权平均
    # jh_price = [551.7763486297913,
    #             300.0180509677043,
    #             314.898325168241]
    # jh_price_avg = 388.89757492191217
    nb_price = [int(294.05745856353593), int(278.44575936883626), int(277.0701902748414), int(281.1363855421687),
                int(284.7492537313433)]
    nb_price_avg = np.mean(nb_price)
    # 宁波三类用户的平均房价
    nb_price = [287.65134408602154,
                280.7831081081081,
                275.4627853881278, ]

    nb_price_avg = 280.96228070175437
    # 加权平均
    nb_price = [446.4984025688969,
                285.5307312413625,
                244.53873465571908]
    nb_price_avg = 325.52262282199285
    # TODO:重新画一遍
    # ax2.plot([1, 2, 3], nb_price, color='#0F50A2', label='Ningbo')
    ax2.plot([1, 2, 3], jh_price, color='orange', label='Jinhua')
    ax2.plot([1, 3], [jh_price_avg, jh_price_avg], alpha=0.6, linestyle='--', color='orange')
    ax2.plot([1, 2, 3], nb_price, color='#3e88ad', label='Ningbo')
    ax2.plot([1, 3], [nb_price_avg, nb_price_avg], alpha=0.6, linestyle='--', color='#3e88ad')

    ax2.set_xticks([1, 2, 3])
    ax2.tick_params(labelsize=12)
    ax2.set_xlabel("category", fontsize=16)
    ax2.set_ylabel("average price of group activity", fontsize=16)
    ax2.legend()
    fig2.savefig('../figure/3类/price_group_activity_income_2.pdf', bbox_inches='tight')
    fig2.show()


def fig_volume():
    fig = plt.figure(figsize=(8, 6))
    ax3 = fig.add_subplot(1, 1, 1)
    jh_volume = [0.7936739014862049, 0.8532234058008169, 0.8171988658188964, 0.8234951160680781,
                 0.8976915212270171]
    # 金华分3级用户的流量多样性
    jh_volume = [0.7979453539213233, 0.8562899559099179, 0.837291491175352]
    nb_volume = [0.7871032484728104, 0.8328762391463381, 0.8231463631998077, 0.7878441820366949,
                 0.7379026694552102]
    # 宁波3类用户的流量多样性
    nb_volume = [0.7754813162891413,
                 0.8067542667900709,
                 0.8043508357640883]
    nb_volume = [0.8048544502432969, 0.8358225068781159, 0.8146825120328643]
    ax3.plot([1, 2, 3], jh_volume, label='Jinhua', color='orange')
    ax3.plot([1, 2, 3], nb_volume, label='Ningbo', color='#3e88ad')

    ax3.legend()
    ax3.set_xlabel("category", fontsize=16)
    ax3.set_ylabel("Flow Diversity", fontsize=16)
    ax3.set_xticks([1, 2, 3])
    ax3.tick_params(labelsize=12)
    fig.savefig('../figure/3类/entropy_flow_2.pdf', bbox_inches='tight')
    fig.savefig('../figure/3类/entropy_flow_2.png', bbox_inches='tight')
    fig.show()


def cal_price_jh():
    path = '../data/level/过滤/金华1类用户的流量分布.csv'
    data = pd.read_csv(path)
    data = data[data['price'] != 0]
    price1 = data['price'].values.tolist()
    nums = data['nums'].values.tolist()
    temp_all = 0
    num_all = 0
    temp = 0
    for i in range(len(nums)):
        temp += nums[i] * price1[i]
    temp_all += temp
    temp /= sum(nums)
    print(temp)
    num_all += sum(nums)
    path = '../data/level/过滤/金华2类用户的流量分布.csv'
    data = pd.read_csv(path)
    data = data[data['price'] != 0]
    price2 = data['price'].values.tolist()
    temp = 0
    for i in range(len(nums)):
        temp += nums[i] * price2[i]
    temp_all += temp
    temp /= sum(nums)
    print(temp)
    num_all += sum(nums)

    path = '../data/level/过滤/金华3类用户的流量分布.csv'
    data = pd.read_csv(path)
    data = data[data['price'] != 0]
    price3 = data['price'].values.tolist()
    temp = 0
    for i in range(len(nums)):
        temp += nums[i] * price3[i]
    temp_all += temp
    temp /= sum(nums)
    num_all += sum(nums)
    print(temp)
    all_price = price1.copy()
    all_price.extend(price2)
    all_price.extend(price3)
    print(temp_all / num_all)
    # print(np.mean(price1), np.mean(price2), np.mean(price3))
    # print(np.mean(all_price))


def cal_price_nb():
    path = '../data/level/过滤/3类/宁波1类用户的流量分布.csv'
    data = pd.read_csv(path)
    data = data[data['price'] != 0]
    print(data)
    print(data.size)
    print(data[data['nums'] < 3].size)
    price1 = data['price'].values.tolist()
    nums = data['nums'].values.tolist()
    temp_all = 0
    num_all = 0
    temp = 0
    for i in range(len(nums)):
        temp += nums[i] * price1[i]
    temp_all += temp
    temp /= sum(nums)
    num_all += sum(nums)
    print(temp)
    path = '../data/level/过滤/3类/宁波2类用户的流量分布.csv'
    data = pd.read_csv(path)
    data = data[data['price'] != 0]
    price2 = data['price'].values.tolist()
    temp = 0
    for i in range(len(nums)):
        temp += nums[i] * price2[i]
    temp_all += temp

    temp /= sum(nums)
    num_all += sum(nums)

    print(temp)
    path = '../data/level/过滤/3类/宁波3类用户的流量分布.csv'
    data = pd.read_csv(path)
    data = data[data['price'] != 0]
    price3 = data['price'].values.tolist()
    temp = 0
    for i in range(len(nums)):
        temp += nums[i] * price3[i]
    temp_all += temp
    temp /= sum(nums)
    num_all += sum(nums)
    print(temp)
    all_price = price1.copy()
    all_price.extend(price2)
    all_price.extend(price3)
    # print(price1, price2, price3)
    # print(np.mean(price1), np.mean(price2), np.mean(price3))
    print(temp_all / num_all)


def gyration(endx, endy):
    r_end = []
    endx_mid = np.mean(endx)
    endy_mid = np.mean(endy)
    dis1 = 0
    for ix, jy in zip(endx, endy):
        dis1 = dis1 + geodistance(ix, jy, endx_mid, endy_mid)
    r_end.append(dis1 / len(endx))
    print(endx_mid, endy_mid)
    return r_end


def cal_range_jh():
    endx, endy = [], []
    for i in range(1, 4):
        data = pd.read_csv(f'../data/level/过滤/3类/jinhua_level{i}.csv')
        # userid = data['UserID'].values
        endx1, endy1 = data['EndLng'].values, data['EndLat'].values
        endx.extend(endx1)
        endy.extend(endy1)
        # print(endx1, endy1)
        # m = mean_gyration(userid, endx1, endy1)
        # print(m)
        r = gyration(endx1, endy1)
        print(r)
    r_all = gyration(endx, endy)
    print(r_all)


def cal_range_nb():
    endx, endy = [], []
    for i in range(1, 4):
        data = pd.read_csv(f'../data/level/过滤/3类/ningbo_level{i}.csv')
        # userid = data['UserID'].values
        endx1, endy1 = data['EndLng'].values, data['EndLat'].values
        endx.extend(endx1)
        endy.extend(endy1)
        # print(endx1, endy1)
        # m = mean_gyration(userid, endx1, endy1)
        # print(m)
        r = gyration(endx1, endy1)
        print(r)
    r_all = gyration(endx, endy)
    print(r_all)


# def cal_range():
#     data = pd.read_csv('../data/level/过滤/jinhua_level1_1.csv')
#     userID = data['UserID']
#     endx = data['EndLng']
#     endy = data['EndLat']
#     g1 = mean_gyration(userID, endx, endy)
#     data = pd.read_csv('../data/level/过滤/jinhua_level2_1.csv')
#     userID = data['UserID']
#     endx = data['EndLng']
#     endy = data['EndLat']
#     g2 = mean_gyration(userID, endx, endy)
#     data = pd.read_csv('../data/level/过滤/jinhua_level3_1.csv')
#     userID = data['UserID']
#     endx = data['EndLng']
#     endy = data['EndLat']
#     g3 = mean_gyration(userID, endx, endy)
#
#     data = pd.read_csv('../data/level/过滤/jinhua_level_1.csv')
#     userID = data['UserID']
#     endx = data['EndLng']
#     endy = data['EndLat']
#     g = mean_gyration(userID, endx, endy)
#     print(g1, g2, g3)
#     print(g)


# def cal_range_nb():
#     data = pd.read_csv('../data/level/过滤/3类/ningbo_level1.csv')
#     userID = data['UserID']
#     endx = data['EndLng']
#     endy = data['EndLat']
#     g1 = mean_gyration(userID, endx, endy)
#     data = pd.read_csv('../data/level/过滤/3类/ningbo_level2.csv')
#     userID = data['UserID']
#     endx = data['EndLng']
#     endy = data['EndLat']
#     g2 = mean_gyration(userID, endx, endy)
#     data = pd.read_csv('../data/level/过滤/3类/ningbo_level3.csv')
#     userID = data['UserID']
#     endx = data['EndLng']
#     endy = data['EndLat']
#     g3 = mean_gyration(userID, endx, endy)
#
#     data = pd.read_csv('../data/level/过滤/3类/宁波_level_all.csv')
#     userID = data['UserID']
#     endx = data['EndLng']
#     endy = data['EndLat']
#     g = mean_gyration(userID, endx, endy)
#     print(g1, g2, g3)
#     print(g)


def cal_volume():
    path = '../data/level/过滤/3类/宁波1类用户的流量分布.csv'
    data = pd.read_csv(path)
    nums = data['nums'].values.tolist()
    e1 = get_entropy(nums)
    path = '../data/level/过滤/3类/宁波2类用户的流量分布.csv'
    data = pd.read_csv(path)
    nums = data['nums'].values.tolist()
    e2 = get_entropy(nums)

    path = '../data/level/过滤/3类/宁波3类用户的流量分布.csv'
    data = pd.read_csv(path)
    nums = data['nums'].values.tolist()
    e3 = get_entropy(nums)
    print(e1, e2, e3)


def massdis():
    jhx1, jhy1 = 121.57634436185378, 29.86398740368574
    jhx2, jhy2 = 121.57348257068445, 29.86824741251168
    jhx3, jhy3 = 121.57460607154852, 29.871987430972606
    jhxc, jhyc = 121.548816000000002, 29.867888000000001
    jhd1 = geodistance(jhx1, jhy1, jhxc, jhyc)
    jhd2 = geodistance(jhx2, jhy2, jhxc, jhyc)
    jhd3 = geodistance(jhx3, jhy3, jhxc, jhyc)
    print(jhd1, jhd2, jhd3)
    nbx1, nby1 = 120.06805391442413, 29.309658845695104
    nbx2, nby2 = 120.07808726499402, 29.31304173750615
    nbx3, nby3 = 120.08926769099261, 29.314118677683226
    nbxc, nbyc = 120.05761, 29.30281
    nbd1 = geodistance(nbx1, nby1, nbxc, nbyc)
    nbd2 = geodistance(nbx2, nby2, nbxc, nbyc)
    nbd3 = geodistance(nbx3, nby3, nbxc, nbyc)
    print(nbd1,nbd2,nbd3)

if __name__ == '__main__':
    # cal_range_jh()
    # cal_range_nb()

    # massdis()
    # fig_range()
    # cal()
    # cal_range()
    # 新数据，金华分3级
    fig_volume()
    # plt.xticks(x)
    # plt.show()
    # plt.plot(x, jh_price)
    # plt.plot([1, 5], [jh_price_avg, jh_price_avg])
    # plt.xticks(x)
    # plt.show()

    # fig3.savefig('../figure/entropy of volume.pdf', bbox_inches='tight')
    # fig3.show()

    # cal_range_nb()
    # cal_range()
    # fig_range()

    # cal_volume()
    # fig_volume()

    # cal_price_jh()
    # cal_price_nb()
    # fig_price()
