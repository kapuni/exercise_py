# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 10:26:26 2019

@author: kapuni
"""

import pandas
data1 = pandas.read_csv(
        'D:/PDABook/第四章/4.5.1 记录合并/台电.csv',
        engine='python', encoding='utf-8'
        )

data2 = pandas.read_csv(
        'D:/PDABook/第四章/4.5.1 记录合并/小米.csv',
        engine='python', encoding='utf-8'
        )

data3 = pandas.read_csv(
        'D:/PDABook/第四章/4.5.1 记录合并/苹果.csv',
        engine='python', encoding='utf-8'
        )

data = pandas.concat([data1, data2, data3])
cData = pandas.concat([
        data1[['id', 'comments']],
        data2[['comments', 'title']],
        data3[['id', 'title']]
        ])
