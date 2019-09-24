# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 21:33:54 2019

@author: kapuni
"""

import pandas
data = pandas.read_csv(
        'D:/PDABook/第四章/4.3.1 数值转字符/数值转字符.csv',
        engine='python', encoding='utf-8'
        )
#print(data.dtypes)

data['电话号码'] = data.电话号码.astype(float)
print(data.电话号码.dtype)