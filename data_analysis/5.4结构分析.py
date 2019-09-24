# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 16:51:03 2019

@author: kapuni
"""

import pandas
data = pandas.read_csv(
        'D:/PDABook/第五章/5.4 结构分析/结构分析.csv',
        engine='python', encoding='utf-8'
        )

#gender列 + label + 计数
ga = data.groupby(by=['gender'])['id'].agg('count')

#总用户
print(ga.sum())

#不同性别用户比例
print(ga / ga.sum())












