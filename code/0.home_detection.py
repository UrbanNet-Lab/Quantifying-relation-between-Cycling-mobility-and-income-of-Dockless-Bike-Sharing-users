# -*- coding: utf-8 -*-
# @Time : 2023/7/4 22:54
# @Author : YangYu
# @Email: yangyu.cs@outlook.com
# @File : userTrip.py
# @Software: PyCharm
from collections import Counter

import pandas as pd

"""
输入数据：订单对应的起始点栅格
输出，用户的职住地点
"""
df = pd.read_csv('../data/宁波_Home.csv')
home = df[df['is_home'] == 1]["id"].values
home_dict = dict()
for h in home:
    home_dict[h] = 1
# print(home_dict)
data = pd.read_csv('../data/宁波OD数据（500m栅格）.csv')
data['StartTime'] = pd.to_datetime(data['StartTime'])
data['EndTime'] = pd.to_datetime(data['EndTime'])
data['st'] = data['StartTime'].dt.hour
data['et'] = data['EndTime'].dt.hour
data['day'] = data['StartTime'].dt.day

ugroup = data.groupby('UserID')
u_dict = {}
aa = 0
bb = 0

for u in ugroup:
    trip = u[1]
    day_list = trip["day"].values
    if len(day_list) < 2:
        continue
    if len(day_list) <= len(set(day_list)):
        # print(day_list)
        continue

    # 目的地为22点后或5点前
    home1 = trip[(trip["et"] >= 22) | (trip["et"] <= 5)]["e_id"].values
    # 出发地为5点到9点之间
    home2 = trip[(trip["st"] >= 5) & (trip["st"] <= 9)]["s_id"].values
    # print(home1["end_id"].values)
    # print(home2["id"].values)
    homes = []
    if len(home1):
        homes.extend(home1)
    if len(home2):
        homes.extend(home2)
    work1 = trip[(trip["st"] >= 9) & (trip["st"] <= 22)]["s_id"].values
    work2 = trip[(trip["st"] >= 9) & (trip["st"] <= 22)]["e_id"].values
    works = []
    if len(work1):
        works.extend(work1)
    if len(work2):
        works.extend(work2)
    hc = list(Counter(homes).items())
    wc = list(Counter(works).items())
    if len(hc) == 0 or len(wc) == 0:
        aa += 1
        continue
    hc = sorted(hc, key=lambda x: x[1], reverse=True)
    wc = sorted(wc, key=lambda x: x[1], reverse=True)
    # if len(hc) > 5:
    #     print(hc)
    u_h = -1
    for _h in hc:
        if _h[0] in home_dict:
            u_h = _h[0]
            break
    u_w = -1
    for _w in wc:
        if _w[0] != u_h:
            u_w = _w[0]
            break
    u_dict[u[0]] = (u_h, u_w)
    # print(hc[0], wc[0])

# print(aa, bb)
# print(len(u_dict))
u_key, u_hw = zip(*u_dict.items())
u_home, u_work = zip(*u_hw)
uu = list(zip(u_key, u_home, u_work))
# print(uu)
udata = pd.DataFrame(uu)
udata.columns = ['userid', 'home', 'work']
# udata = udata.dropna()
udata['home'] = udata['home'].astype(int)
udata['work'] = udata['work'].astype(int)
# print(len(udata))
# udata.to_csv('宁波用户职住数据(过滤).csv', index=False)
# print(udata)
