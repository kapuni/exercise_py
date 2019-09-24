# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 09:14:47 2019

@author: kapuni
"""

import pandas
data = pandas.read_csv(
        'D:/PDABook/第五章/5.8 矩阵分析/矩阵分析.csv',
        engine='python', encoding='utf-8'
        )

costAgg = data.groupby(
        by='省份', as_index=False
        )['月消费（元）'].agg('mean')

dataAgg = data.groupby(
        by = '省份', as_index=False
        )['月流量（MB）'].agg('mean')

aggData = costAgg.merge(dataAgg)