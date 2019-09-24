# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 10:38:44 2019

@author: kapuni
"""

import pandas
data = pandas.read_csv(
        'D:/PDABook/第四章/4.5.2 字段合并/字段合并.csv',
        engine='python', encoding='utf-8'
        )

data = data.astype(str)

tel = data['band'] + data['area'] + data['num']
data['tel'] = tel