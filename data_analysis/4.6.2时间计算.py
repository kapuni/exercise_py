# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 11:13:37 2019

@author: kapuni
"""

import pandas
from datetime import datetime

data = pandas.read_csv(
        'D:/PDABook/第四章/4.6.2 时间计算/时间计算.csv',
        engine='python', encoding='utf-8'
        )
#时间列  字符串-->时间类型
data['时间'] = pandas.to_datetime(
        data.注册时间,
        format='%Y/%m/%d'
        )

data['注册天数'] = datetime.now() - data['时间']
data['注册天数'] = data['注册天数'].dt.days
