# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 10:20:57 2019

@author: kapuni
"""

import pandas


data = pandas.read_csv(
        'D:/PDABook/第四章/4.4.3 随机抽样/随机抽样.csv',
        engine='python', encoding='utf-8'
        )

sData = data.sample(n=3)
pData = data.sample(frac=0.2)
rData = data.sample(n=3, replace=True)
