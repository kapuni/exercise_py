# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 09:51:59 2019

@author: kapuni
"""

import pandas
from datetime import datetime

data = pandas.read_csv(
        'D:/PDABook/第四章/4.4.2 记录抽取/记录抽取.csv',
        engine='python', encoding='utf-8'
        )

fData = data[data.title.str.contains('台电', na=False)]
sData = data[data.title.isnull()]
bData = data[data.comments > 10000]
tData = data[data.comments.between(1000, 10000)]
iData = data[~data.title.str.contains('台电', na=False)]

data['ptime'] = pandas.to_datetime(
        data.ptime,
        format='%Y-%m-%d'
        )


#定义时间点1，2015.11
dt1 = datetime(
        year=2015,
        month=1,
        day=1
        )
#定义时间点2，2015.12.31
dt2 = datetime(
        year=2015,
        month=12,
        day=31
        )
dData = data[(data.ptime >= dt1) & (data.ptime <= dt2)]

