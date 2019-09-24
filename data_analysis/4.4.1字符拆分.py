# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 21:47:24 2019

@author: kapuni
"""

import pandas 
data = pandas.read_csv(
        'D:/PDABook/第四章/4.4.1 字段拆分/字段拆分.csv',
        engine='python'
        )
data['tel'] = data['tel'].astype(str)
bands = data['tel'].str.slice(0, 3)

areas = data['tel'].str.slice(3, 7)

nums = data['tel'].str.slice(7, 11)

data['bands'] = bands
data['areas'] = areas
data['num'] = nums