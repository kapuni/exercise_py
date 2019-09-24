# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 11:09:57 2019

@author: kapuni
"""

import pandas
data = pandas.read_csv(
        'D:/PDABook/第四章/4.6.1 简单计算/单价数量.csv',
        engine='python', encoding='utf-8'
        )
data['total'] = data.price * data.num