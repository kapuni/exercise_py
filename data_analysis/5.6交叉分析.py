# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 17:56:45 2019

@author: kapuni
"""

import pandas
data = pandas.read_csv(
        'D:/PDABook/第五章/5.6 交叉分析/交叉分析.csv',
        engine='python', encoding='utf-8'
        )


bins = [
        0, 20, 30, 40, 100
        ]
ageLabels = [
        '20岁以下', '21岁到30岁', '31岁到40', '41岁以上'
        ]
data['年龄分层'] = pandas.cut(
        data.年龄,
        bins,
        labels=ageLabels
        )

ptResult = data.pivot_table(
        values = '用户ID',
        index = '年龄分层',  #行
        columns = '性别',    #列
        aggfunc ='count'
        )