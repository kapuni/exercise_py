# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 21:22:32 2019

@author: kapuni
"""


import pandas
data = pandas.read_csv(
        'D:/PDABook/第四章/4.2.3 缺失值处理/常见缺失值.csv',
        engine='python', encoding='utf-8'
        )
cData = data.dropna()