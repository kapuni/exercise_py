# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 21:29:26 2019

@author: kapuni
"""

import pandas
data = pandas.read_csv(
        'D:/PDABook/第四章/4.2.4 空格值处理/空格值.csv',
        engine='python', encoding='utf-8'
        )
data['name'] = data['name'].str.strip()