#!/usr/bin/env python
# coding: utf-8

# ## 对房价分层

# In[4]:


# 关于文档的一个数据分类
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# import csv
import math
from pandas import Series, DataFrame
from matplotlib.ticker import MultipleLocator
import pylab as pl  # 画图用
import seaborn as sns


# In[ ]:


##########迭代函数 ###
# def cumulative(data,I):#排序后的数据，I值用来区分颜色
#     X = []#归一化后的x轴
#     Y = []#叠加后的y值
#     Y1 = []#对叠加后的y值进行归一化
#     x = np.arange(1,len(data)+1)#列表的长度，依次为1,2,3,4，。。。。
#     y = data###排序后的值
#     if len(y)==1:#如果截得只剩一个数了，就给y前面加个零，x的个数加1,这样再一次归一化
#         x = np.arange(1,len(data)+2)
#         y.insert(0,0)#在第0个位置加上0
#
#     sum1 = 0
#     for i in y:
#         sum1 = sum1+i
#         Y.append(sum1)#对y值进行叠加
#     #print(Y)
#     for m in x:
#         X.append((m - min(x)) / (max(x) - min(x)))#对x轴进行归一化
#     #print(X)
#     for n in Y:
#         Y1.append((n - min(Y)) / (max(Y) - min(Y)))#对y轴进行归一化
#     #print(Y1)
#     k = round((Y1[len(Y1)-1] - Y1[len(Y1)-2])/(X[len(X)-1] - X[len(X)-2]),2)#斜率
#     b = round((Y1[len(Y1)-1] - k*X[len(X)-1]),2)#截距
#     threshold_index = -b/k#和x轴的交点
#     for index in range(len(X)):
#         if X[index] >= threshold_index:
#             threshold = y[index]#要截取的值
#             break
#     xx = [X[-1],threshold_index]#两点确定一条直线
#
#     plt.plot(X,Y1,color=cm1[I])#曲线
#     plt.plot(xx,[k*xxx+b for xxx in xx],color=cm2[I],linewidth=2)#截断的那条线
#     plt.xlim(0,1)
#     plt.ylim(0,1)
#     return(k,b,threshold_index,threshold,len(y[:index]),len(y[index:]),y[:index])#斜率，截距,与x轴交点,截取的y值，剩下的值
#

# In[5]:


##########迭代函数 ###另一种归一化方式（用的是这个）
def cumulative(data, I):  # 排序后的数据，I值用来区分颜色
    X = []  # 归一化后的x轴
    Y = []  # 叠加后的y值
    Y1 = []  # 对叠加后的y值进行归一化
    x = np.arange(1, len(data) + 1)  # 列表的长度，依次为1,2,3,4，。。。。
    y = data  ###排序后的值
    if len(y) == 0:  # 如果没有数据了，但是截断的地方不是0，那就构造一个y=x的数
        x = [0, 1]
        y = [0, 1]
    #     if len(y)==1:#如果截得只剩一个数了，那就在归一化后都给前面加个0，构造y=x的线，但这样就截不到最后一个值了
    #         x.insert(0,0)
    #         y.insert(0,0)#在第0个位置加上0
    mx = max(x)
    sum1 = 0
    for i in y:
        sum1 = sum1 + i
        Y.append(sum1)  # 对y值进行叠加
    # print(Y)
    mY = max(Y)
    for m in x:
        X.append(m / mx)  # 对x轴进行归一化
    # print(X)
    for n in Y:
        Y1.append(n / mY)  # 对y轴进行归一化
    # print(Y1)
    if len(y) == 1:  # 如果截得只剩一个数了，那就在归一化后都给前面加个0，构造y=x的线
        X.insert(0, 0)
        Y1.insert(0, 0)  # 在第0个位置加上0
    k = round((Y1[len(Y1) - 1] - Y1[len(Y1) - 2]) / (X[len(X) - 1] - X[len(X) - 2]), 2)  # 斜率
    b = round((Y1[len(Y1) - 1] - k * X[len(X) - 1]), 2)  # 截距
    threshold_index = -b / k  # 和x轴的交点
    for index in range(len(X)):
        if X[index] >= threshold_index:
            threshold = y[index]  # 要截取的值
            break
    xx = [X[-1], threshold_index]  # 两点确定一条直线
    X.insert(0, 0)
    Y1.insert(0, 0)
    plt.plot(X, Y1, color=cm1[I])  # 曲线
    plt.plot(xx, [k * xxx + b for xxx in xx], color=cm2[I], linewidth=2, label='Threshold' + ' ' + str(I))  # 截断的那条线
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    font = {'size': 14}
    plt.legend(prop=font)
    return (k, b, threshold_index, threshold, len(y[:index]), len(y[index:]), y[:index])  # 斜率，截距,与x轴交点,截取的y值，剩下的值


# In[ ]:


# 主函数
# cm1 = list(sns.color_palette("Blues_r",10))###蓝色
# cm2 = list(sns.color_palette("Reds_r", 10))
# x = np.arange(1,len(data1)+1)
# y = data1
# threshold_sumunion = max(y)#每次截取的最小y值
# Threshold_sumunion = []#所有截取的y值
#
# plt.figure(figsize=(14,12))
# index = 1###标志是否停止
# i=0
# threshold_index = -1#与x轴的交点
# while(threshold_index!=0):
#     if i==0:
#         dataT=data1#第一次进来，默认不切
#     i+=1
#     data2 = sorted(dataT)#进行排序
#     plt.subplot(2,2,1)
#     plt.tick_params(labelsize=16) #刻度字体大小13
#     plt.xlabel('mean_price',fontsize=16)
#     plt.ylabel('mean_price_add',fontsize=16)
#     result = cumulative(data2,i)
#     print(result)
#     threshold_index = result[2]
#     threshold_sumunion = result[3]
#     Threshold_sumunion.append(threshold_sumunion)
#     dataT = result[5]#截去后剩余的值
# print(Threshold_sumunion)
# plt.savefig('D:/Python_code/北京上海骑行特征/shanghai/500房价分层.pdf', bbox_inches='tight')


# In[6]:


# 北京数据
data = pd.read_csv("../data/房价/ningbo平均房价.csv")
# aa = data.groupby("id")
data = data.dropna()
data1 = data['总价']
print(data1)
# In[7]:


# 北京主函数
cm1 = list(sns.color_palette("Blues_r", 10))  ###蓝色
cm2 = list(sns.color_palette("Reds_r", 10))
x = np.arange(1, len(data1) + 1)
y = data1
threshold_sumunion = max(y)  # 每次截取的最小y值
Threshold_sumunion = []  # 所有截取的y值

fig = plt.figure(figsize=(14, 12))
index = 1  ###标志是否停止
i = 0
threshold_index = -1  # 与x轴的交点
# while(threshold_index!=0):
a = 4
while (a > 0):
    if i == 0:
        dataT = data1  # 第一次进来，默认不切
    i += 1
    data2 = sorted(dataT)  # 进行排序
    ax1 = plt.subplot(221)
    plt.tick_params(labelsize=16)  # 刻度字体大小13
    plt.xlabel('fraction of locations', fontsize=16)
    plt.ylabel('fraction of total $\\langle$house price$\\rangle$', fontsize=16)
    result = cumulative(data2, i)
    print(result[:6])
    threshold_index = result[2]
    threshold_sumunion = result[3]
    Threshold_sumunion.append(threshold_sumunion)
    dataT = result[6]  # 截去后剩余的值
    a = a - 1

print(Threshold_sumunion)
# plt.savefig('../figure/fig1 宁波洛伦兹曲线.pdf', bbox_inches='tight')
plt.show()

# In[8]:


# 上海数据
# data = pd.read_csv("上海可用人口表.csv")
# data1 = data['total_average']
#
#
# # In[9]:
#
#
# #上海主函数
# cm1 = list(sns.color_palette("Blues_r",10))###蓝色
# cm2 = list(sns.color_palette("Reds_r", 10))
# x = np.arange(1,len(data1)+1)
# y = data1
# threshold_sumunion = max(y)#每次截取的最小y值
# Threshold_sumunion = []#所有截取的y值
#
# fig = plt.figure(figsize=(14,12))
# index = 1###标志是否停止
# i=0
# threshold_index = -1#与x轴的交点
# #while(threshold_index!=0):
# a = 4
# while(a>0):
#     if i==0:
#         dataT=data1#第一次进来，默认不切
#     i+=1
#     data2 = sorted(dataT)#进行排序
#     ax1 = plt.subplot(221)
#     plt.tick_params(labelsize=16) #刻度字体大小13
#     plt.xlabel('fraction of locations',fontsize=16)
#     plt.ylabel('fraction of total $\\langle$house price$\\rangle$',fontsize=16)
#     result = cumulative(data2,i)
#     print(result[:6])
#     threshold_index = result[2]
#     threshold_sumunion = result[3]
#     Threshold_sumunion.append(threshold_sumunion)
#     dataT = result[6]#截去后剩余的值
#     a = a-1
# print(Threshold_sumunion)
# plt.savefig('D:/Python_code/北京上海骑行特征/文章中的图/fig1 上海洛伦兹曲线.pdf', bbox_inches='tight')


# In[ ]:
