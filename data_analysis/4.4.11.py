# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 22:30:27 2019

@author: kapuni
"""

import pandas
data = pandas.read_csv(
        'D:/PDABook/第四章/4.4.1 字段拆分/分隔符.csv',
        engine='python', encoding='utf-8'
        )

newData = data['name'].str.split(' ', 1 , True)

newData.columns = ['bands', 'name']