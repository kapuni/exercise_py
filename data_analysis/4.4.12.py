# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 22:35:20 2019

@author: kapuni
"""

import pandas
data = pandas.read_csv(
        'D:/PDABook/第四章/4.4.1 字段拆分/时间属性.csv',
        engine='python', encoding='utf-8'
        )

data['时间'] = pandas.to_datetime(
        data.注册时间,
        format='%Y/%m/%d %H:%M:%S'
        )

data['时间.年'] = data['时间'].dt.year 
data['时间.月'] = data['时间'].dt.month 
data['时间.周'] = data['时间'].dt.weekday 
data['时间.日'] = data['时间'].dt.day 
data['时间.时'] = data['时间'].dt.hour 
data['时间.分'] = data['时间'].dt.minute 
data['时间.秒'] = data['时间'].dt.second 