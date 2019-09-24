# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 09:22:11 2019

@author: kapuni
"""

import pandas
data = pandas.read_csv(
        'D:/PDABook/第五章/5.3 分组分析/分组分析.csv',
        engine='python', encoding='utf-8'
        )

#性别分组  平均年龄
ga = data.groupby(
        by = ['gender'], 
        as_index=False   #设置索引列
        )['age'].agg('mean')


