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
yMin = aggData['月流量（MB）'].min() * (1- gap)
yMax = aggData['月流量（MB）'].max() * (1+ gap)

# 设置x轴和y轴的坐标轴范围
plt.xlim(xMin, xMax)
plt.ylim(yMin, yMax)

plt.xticks(color=mainColor, fontproperties=font)
plt.yticks(color=mainColor, fontproperties=font)
plt.scatter(
         aggData['月消费（元）'],
         aggData['月流量（MB）'],
         s=50,marker = 'o', color=mainColor
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
#绘制均值线
plt.vlines(
        x=data['月消费（元）'].mean(),
        ymin=yMin, ymax=yMax,
        linewidth=1, color=mainColor
        )
plt.hlines(
        y=data['月流量（MB）'].mean(),
        xmin=xMin, xmax=xMax,
        linewidth=1, color=mainColor
        )

#标注四个象限的标记， 在不同的分辨率↓， 需要微调一下
plt.text(
        xMax - 0.5, yMax - 5,
        'I', color=fontColor, fontsize=20
        )
plt.text(
        xMin, yMax - 5,
        'II', color=fontColor, fontsize=20
        )
plt.text(
        xMin, yMin ,
        'III', color=fontColor, fontsize=20
        )
plt.text(
        xMax - 0.7, yMin,
        'IV', color=fontColor, fontsize=20
        )
#给每个点画标签， for循环遍历每一行
for i, r in aggData.iterrows():
    plt.text(
            r['月消费（元）'] + 0.25,
            r['月流量（MB）'] - 1,
            r['省份'], 
            color =fontColor,
            fontproperties=font
            )
