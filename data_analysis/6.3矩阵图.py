# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 19:38:17 2019

@author: kapuni
"""

import pandas 
import matplotlib
import matplotlib.pyplot as plt

data = pandas.read_csv(
        'D:/PDABook/第五章/5.8 矩阵分析/矩阵分析.csv',
        engine='python', encoding='utf-8'
        )

costAgg = data.groupby(
        by='省份', as_index=False
        )['月消费（元）'].agg('mean')

dataAgg = data.groupby(
        by = '省份', as_index=False
        )['月流量（MB）'].agg('mean')

aggData = costAgg.merge(dataAgg)
  
#选择字体  点
font = matplotlib.font_manager.FontProperties(
        fname = 'D:/PDABook/SourceHanSansCN-Light.otf', size=10
        )
#字体 轴
labelFont = matplotlib.font_manager.FontProperties(
        fname = 'D:/PDABook/SourceHanSansCN-Light.otf', size=15
        )

#蓝色 点yans
mainColor = (91/255, 155/255, 213/255, 1)
#灰色 文本颜色
fontColor = (110/255, 110/255,110/255,1)

fig = plt.figure()
#为了画面美观， 旁边预留1%的空白边缘，范围[最小值*（1-1￥）， 最大值*（1+1%）]
gap = 0.01

#x轴的范围值
xMin = aggData['月消费（元）'].min() * (1- gap)
xMax = aggData['月消费（元）'].max() * (1- gap)
#y的范围值
yMin = aggData['月流量（MB）'].min() * (1+ gap)
yMax = aggData['月流量（MB）'].max() * (1+ gap)

# 设置x轴和y轴的坐标轴范围
plt.xlim(xMin, xMax)
plt.xlim(yMin, yMax)

plt.xticks([])
plt.yticks([])
plt.scatter(
         aggData['月消费（元）'],
         aggData['月流量（MB）'],
         s=300, marker = 'o', color=fontColor
         )
plt.xlabel(
        '人均月消费（元）',
        color = fontColor,
        fontproperties=labelFont
        )
plt.ylabel(
        '月流量（MB）',
        color = fontColor,
        fontproperties=labelFont
        )
