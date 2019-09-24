# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 18:09:23 2019

@author: kapuni
"""

import pandas
from datetime import datetime


data = pandas.read_csv(
        'D:/PDABook/第五章/5.7 RFM分析/RFM分析.csv',
        engine='python'
        )
#交易日期转为时间格式
data['DealDateTime'] = pandas.to_datetime(
        data.DealDateTime,
        format='%Y/%m/%d' 
        )
#消费时间
data['DateDiff'] = datetime.now() - data['DealDateTime']
#转为消费天数
data['DateDiff'] = data['DateDiff'].dt.days


#最小的最近消费距离
R_Agg = data.groupby(
        by = ['CustomerID'],
        as_index = False
        )['DateDiff'].agg('min')
#交易总次数  计数
F_Agg = data.groupby(
        by = ['CustomerID'],
        as_index = False
        )['OrderID'].agg('count')
#交易总额    求和
M_Agg = data.groupby(
        by = ['CustomerID'],
        as_index = False
        )['Sales'].agg('sum')


#3表关联为一
aggData = R_Agg.merge(F_Agg).merge(M_Agg)
aggData.columns = ['CustomerID', 'RecencyAgg', 'FrequencyAgg', 'MonetaryAgg']

bins = aggData.RecencyAgg.quantile(
        q=[0, 0.2, 0.4, 0.6, 0.8, 1],
        interpolation='nearest'
        )
bins[0] = 0
rLabels = [5,4,3,2,1]
R_S = pandas.cut(
        aggData.RecencyAgg,
        bins,
        labels=rLabels
        )

bins = aggData.FrequencyAgg.quantile(
        q=[0, 0.2, 0.4, 0.6, 0.8, 1],
        interpolation='nearest'
        )
bins[0] = 0
fLabels = [5,4,3,2,1]
F_S = pandas.cut(
        aggData.FrequencyAgg,
        bins,
        labels=fLabels
        )

bins = aggData.MonetaryAgg.quantile(
        q=[0, 0.2, 0.4, 0.6, 0.8, 1],
        interpolation='nearest'
        )
bins[0] = 0
mLabels = [5,4,3,2,1]
M_S = pandas.cut(
        aggData.MonetaryAgg,
        bins,
        labels=mLabels
        )

aggData['R_S'] = R_S
aggData['F_S'] = F_S
aggData['M_S'] = M_S

aggData['RFM'] = 100*R_S.astype(int) + 10*F_S.astype(int) + M_S.astype(int)

bins = aggData.RFM.quantile(
        q=[0, 0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875, 1],
        interpolation='nearest'
        )
bins[0]=0
rfmlabels = [1,2,3,4,5,6,7,8]
aggData['level'] = pandas.cut(
        aggData.RFM,
        bins,
        labels = rfmlabels
        )

c = aggData.groupby(
        by='level'
        )['CustomerID'].agg('count')
print(c)

