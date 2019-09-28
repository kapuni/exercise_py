# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 11:09:58 2019

@author: kapuni
"""

import pandas
import matplotlib
from matplotlib import pyplot as plt


data = pandas.read_csv(
        'D:/PDABook/第六章/6.6 柱形图/柱形图.csv',
        engine='python', encoding='utf-8'
        )

#统计每个手机=品牌的用户消费总额
result = data.groupby(
        by=['手机品牌'], as_index=False
        )['月消费（元）'].sum()

plt.figure()
mainColor = (91/255,155/255,213/255,1)
font = matplotlib.font_manager.FontProperties(
        fname='D:/PDABook/SourceHanSansCN-Light.otf', size=10
        )

index = [1,2,3,4,5,6,7,8]
sgb = result.sort_values(
        by='月消费（元）',
        ascending=False)

plt.bar(index, sgb['月消费（元）'], color=mainColor)
#x的刻度
plt.xticks(index, result.手机品牌, fontproperties=font)

#数据排序
