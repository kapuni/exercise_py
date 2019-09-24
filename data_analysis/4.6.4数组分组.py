# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 22:03:26 2019

@author: kapuni
"""

import pandas
data = pandas.read_csv(
        'D:/PDABook/第四章/4.6.4 数据分组/数据分组.csv',
        engine='python', encoding='utf-8'
        )
print(data.cost.min())
print(data.cost.max())

bins = [
        0, 20, 40, 60, 80, 100, 120
        ]

#设置标签格式
customLabels = [
        
       '0到20', '20到40','40到60',
        '60到80', '80到100', '100到120'
        ]
data['cut'] = pandas.cut(
        data.cost,
        bins,
        right = False, #左区间闭 右开
        labels= customLabels

        )