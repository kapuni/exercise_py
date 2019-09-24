# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 16:59:20 2019

@author: kapuni
"""

import pandas
data = pandas.read_csv(
        'D:/PDABook/第五章/5.5 分布分析/分布分析.csv',
        engine='python', encoding='utf-8'
        )


bins = [
      0, 20, 30, 40, 100
      ]
ageLabels = [
        '20岁以下', '21岁到30岁', '31岁到40', '41岁以上'
        ]
data['年龄分层'] = pandas.cut(
        data.年龄,
        bins,
        labels=ageLabels
        )


#各年龄段计数
aggResult = data.groupby(
        by=['年龄分层']
        )['用户ID'].agg('count')

p = round(
        aggResult / aggResult.sum(),
        4   #保留4位小数
        ) * 100
print(p.map('{:,.2f}%'.format))

