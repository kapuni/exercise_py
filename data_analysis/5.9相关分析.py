# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 09:21:29 2019

@author: kapuni
"""

import pandas
data = pandas.read_csv(
        'D:/PDABook/第五章/5.9 相关分析/相关分析.csv',
        engine='python', encoding='utf-8'
        )

r = data['人口'].corr(data['文盲率'])
#print(r)

corrMatrix = data[[
        '超市购物率', '网上购物率', '文盲率', '人口'
        ]].corr()