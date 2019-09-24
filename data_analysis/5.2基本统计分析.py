# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 09:11:46 2019

@author: kapuni
"""

import pandas
data = pandas.read_csv(
        'D:/PDABook/第五章/5.2 基本统计分析/描述性统计分析.csv',
        engine='python', encoding='utf-8'
        )

#输出describe的参数
#print(data.sales.describe())

#sales列求和
#print(data.sales.count())

#排序在30%附近的值
q = data.sales.quantile(0.3, interpolation='nearest')
print(q)