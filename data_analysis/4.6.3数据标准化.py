# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 21:49:37 2019

@author: kapuni
"""

import pandas
data = pandas.read_csv(
        'D:/PDABook/第四章/4.6.3 数据标准化/标准化.csv',
        engine='python', encoding='utf-8'
        )
# 0-1 标准化
data['消费标准化'] = round(
        (
                data.消费 - data.消费.min()
                )/(
                        data.消费.max() - data.消费.min())
        ,2       #保留小数位 2
        )