# -*- coding: utf-8 -*-
# @Time : 2023/7/7 23:04
# @Author : YangYu
# @Email: yangyu.cs@outlook.com
# @File : 5.OD数据提取.py
# @Software: PyCharm
import threading
import time

import pandas as pd

# data = pd.read_csv("../data/金华OD数据（200m栅格）.csv")
# data = data.dropna()
# data["e_id"] = data["e_id"].astype(int)
# data["s_id"] = data["s_id"].astype(int)
# e_id = data["e_id"].unique()
# s_id = data["s_id"].unique()
# set1 = set(e_id)
# set2 = set(s_id)
# set3 = set1.union(set2)
# print(len(set3))
# id_set=set(e_id)
# id_set.union(s_id)
# print(len(id_set))
# id_set.add()

# sets = set()
# a = [1, 1, 2, 3]
# b = [1, 4, 5]
# set1 = set(a)
# set2 = set(b)
# set3 = set1.union(set2)
# print(set3)
import requests


def get_home_list():
    data = pd.read_csv('../data/宁波OD数据（500m栅格）.csv')
    data = data.dropna()
    # data.to_csv('../data/金华OD数据（200m栅格）.csv')
    data['StartTime'] = pd.to_datetime(data['StartTime'])
    data['EndTime'] = pd.to_datetime(data['EndTime'])
    data["s_id"] = data["s_id"].astype(int)
    data["e_id"] = data["e_id"].astype(int)
    data['st'] = data['StartTime'].dt.hour
    data['et'] = data['EndTime'].dt.hour

    # ugroup = data.groupby('UserID')
    u_dict = {}

    HOME = []

    home1 = data[(data["et"] >= 22) | (data["et"] <= 5)]["e_id"].values
    set1 = set(home1)
    home2 = data[(data["st"] >= 5) & (data["st"] <= 9)]["s_id"].values
    set2 = set(home2)
    set3 = list(set1.union(set2))
    # 这个用来找居住地的坐标
    data2 = pd.read_csv("../data/宁波人口和房价.csv")
    id = data2["id"].values
    # print(len(id))
    left, top, right, bottom = data2["left"].values, data2["top"].values, data2["right"].values, data2["bottom"].values
    dict1 = dict(zip(id, zip(left, top, right, bottom)))
    l, t, r, b = [], [], [], []
    for i in set3:
        l.append(dict1[i][0])
        t.append(dict1[i][1])
        r.append(dict1[i][2])
        b.append(dict1[i][3])
    is_home = [0] * len(set3)
    check = [0] * len(set3)
    HOME = pd.DataFrame()
    HOME['id'] = set3
    HOME['left'] = l
    HOME['top'] = t
    HOME['right'] = r
    HOME['bottom'] = b
    HOME['is_home'] = is_home
    HOME['check'] = check
    HOME.to_csv('../data/宁波_Home.csv', index=False)


def isExist(key, location, th, url):
    parameters = {'key': key, 'polygon': location, 'type': 120000}
    url = url
    s = requests.session()
    s.keep_alive = False
    exist = False
    try:
        response = requests.get(url, parameters)
        # print(response)
        result = response.json()

        if int(result["status"]) == 0:
            # 查找失败
            if int(result['infocode']) == 10021:
                time.sleep(100)
            print("线程" + str(th) + ",key:" + key + ',code:' + str(result['info']))
            # 返回-1
            exist = -1
        else:
            if result["count"] != '0':
                # print(result["count"])
                exist = True

    except (requests.ConnectionError, IndexError, UnicodeEncodeError, TimeoutError) as e:
        print("线程" + str(th) + ":" + str(e.args))
    except requests.HTTPError as f:
        print("线程" + str(th) + ":" + 'The server couldn\'t fulfill the request.')
    return exist


def getPOI1(start, end, key, exist, left, top, right, bottom, th, finish):
    url1 = 'https://restapi.amap.com/v5/place/polygon'
    print("线程:" + str(th) + "开始工作！")
    i = 0

    for l, t, r, b in zip(left[start:end], top[start:end], right[start:end], bottom[start:end]):
        # if COUNT >= 12000:
        #     j += 1
        # COUNT += 1
        # if i % 10 == 0:
        #     time.sleep(100)
        if finish[start + i]:
            i += 1
            continue
        location = str(l) + ',' + str(t) + ',' + str(r) + ',' + str(b)
        isexist = isExist(key, location, th, url1)
        if isexist != -1:
            finish[start + i] = 1
            if isexist:
                exist[start + i] = 1
            else:
                exist[start + i] = 0
        else:
            finish[start + i] = 0
        i += 1
    print("线程:" + str(th) + "结束！")


def getPOI2(start, end, key, exist, left, top, right, bottom, th, finish):
    url2 = 'https://restapi.amap.com/v3/place/polygon'
    print("线程:" + str(th) + "开始工作！")
    i = 0
    for l, t, r, b in zip(left[start:end], top[start:end], right[start:end], bottom[start:end]):

        # if COUNT >= 12000:
        #     j += 1
        # COUNT += 1
        if finish[start + i] == 1:
            # print("已经计算过了")
            i += 1
            continue
        location = str(l) + ',' + str(t) + ',' + str(r) + ',' + str(b)
        isexist = isExist(key, location, th, url2)
        if isexist != -1:
            finish[start + i] = 1
            if isexist:
                exist[start + i] = 1
            else:
                exist[start + i] = 0
        else:
            # -1表示说没有查到这个地方
            finish[start + i] = 0
        i += 1
    print("线程:" + str(th) + "结束！")


KEYS1 = ['610778207f510cff2099281f895ba778', '86692accaacaa8599267482e1a5fb759',
         '62de2775629d3aa7c4600192b3abdad0', '659f11afaef363ad0773ec7c8cfdc48c']
KEYS2 = ['e36ead85996afabc3a72ca2cd0e54885', 'bc96eaa92f08d55154bbd94fb28f9160',
         '63997281423c92cb181fa6decebfb7f9', 'a764af152b75be6ef9b9da932ca8464a',
         '48554b553a5e36960da2a872f832e6ea', 'e841b79d391c5e814cdc167ad6e013be']

KEYS3 = ['ba10b54da58595cd1c99787411b39c93', '659f11afaef363ad0773ec7c8cfdc48c', 'cabf7e1d47522e4a9df2aa24b5ea869a',
         'd0ad8476667415fd3e19d267f9f826d9', '7c709f5f428d1c0a3bf30a839b8c7800', '2a5f1364ed0f6b6ef6b3e118cefc535f'
         ]
KEY4 = ['9075b65302ebf4fc560d02c9841d40bc', '755df9e01b80e5ad5811594f2315a52b', 'f038307b817cee7aa8c097db47aaeba3']
KEYS = KEYS2


def check_home():
    data = pd.read_csv('../data/宁波_Home.csv')
    # print(data.dtypes)
    id = data["id"]
    left = data["left"]
    top = data["top"]
    right = data["right"]
    bottom = data["bottom"]
    is_home = data["is_home"].copy()
    check = data["check"].copy()
    # 1200-2400
    print(is_home[100:200])
    st = 0
    thread1 = threading.Thread(target=getPOI1,
                               args=(st, st + 100, KEYS[0], is_home, left, top, right, bottom, 1, check))
    thread2 = threading.Thread(target=getPOI1,
                               args=(st + 100, st + 200, KEYS1[2], is_home, left, top, right, bottom, 2, check))
    thread3 = threading.Thread(target=getPOI1,
                               args=(st + 200, st + 300, KEYS[1], is_home, left, top, right, bottom, 3, check))
    thread4 = threading.Thread(target=getPOI2,
                               args=(st + 300, st + 400, KEYS[1], is_home, left, top, right, bottom, 4, check))
    thread5 = threading.Thread(target=getPOI1,
                               args=(st + 400, st + 500, KEYS[2], is_home, left, top, right, bottom, 5, check))
    thread6 = threading.Thread(target=getPOI2,
                               args=(st + 500, st + 600, KEYS[2], is_home, left, top, right, bottom, 6, check))
    thread7 = threading.Thread(target=getPOI1,
                               args=(st + 600, st + 700, KEYS[3], is_home, left, top, right, bottom, 7, check))
    thread8 = threading.Thread(target=getPOI2,
                               args=(st + 700, st + 800, KEY4[1], is_home, left, top, right, bottom, 8, check))
    thread9 = threading.Thread(target=getPOI1,
                               args=(st + 800, st + 900, KEYS1[2], is_home, left, top, right, bottom, 9, check))
    thread10 = threading.Thread(target=getPOI2,
                                args=(st + 900, st + 1000, KEYS1[2], is_home, left, top, right, bottom, 10, check))
    thread11 = threading.Thread(target=getPOI1,
                                args=(st + 1000, st + 1100, KEYS1[2], is_home, left, top, right, bottom, 11, check))
    # thread12 = threading.Thread(target=getPOI2,
    #                             args=(2300, 2400, KEYS[5], is_home, left, top, right, bottom, 12, check))
    # 2400-2900
    # thread13 = threading.Thread(target=getPOI1,
    #                             args=(2400, 2500, KEYS[0], is_home, left, top, right, bottom, 13, check))
    # thread14 = threading.Thread(target=getPOI2,
    #                             args=(2500, 2600, KEYS[0], is_home, left, top, right, bottom, 14, check))
    # thread15 = threading.Thread(target=getPOI1,
    #                             args=(2600, 2700, KEYS[1], is_home, left, top, right, bottom, 15, check))
    # thread16 = threading.Thread(target=getPOI2,
    #                             args=(2700, 2800, KEYS[1], is_home, left, top, right, bottom, 16, check))
    # thread17 = threading.Thread(target=getPOI2,
    #                             args=(2800, 2900, KEYS[2], is_home, left, top, right, bottom, 16, check))
    # thread1.start()
    # thread2.start()
    # thread3.start()
    # thread4.start()
    # thread5.start()
    # thread6.start()
    # thread7.start()
    thread8.start()
    thread9.start()
    thread10.start()
    thread11.start()
    # thread12.start()
    # thread13.start()
    # thread14.start()
    # thread15.start()
    # thread16.start()
    # thread17.start()
    print("主线程继续执行其他操作")
    #
    # # 等待线程执行完毕
    # thread1.join()
    # thread2.join()
    # thread3.join()
    # thread4.join()
    # thread5.join()
    # thread6.join()
    # thread7.join()
    thread8.join()
    thread9.join()
    thread10.join()
    thread11.join()
    # thread12.join()
    # thread13.join()
    # thread14.join()
    # thread15.join()
    # thread16.join()
    # thread17.join()
    print("结束！")
    print(is_home[100:200])
    data["is_home"] = is_home
    data["check"] = check
    data.to_csv('../data/宁波_HOME.csv', index=False)


if __name__ == '__main__':
    # get_home_list()
    check_home()
    # data = pd.read_csv('../data/金华_Home_ALL.csv')
    # print(data.groupby("is_home").size())
