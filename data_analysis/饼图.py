# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 10:50:03 2019

@author: kapuni
"""
#上接5.4结构分析
import pandas
import matplotlib
from matplotlib import pyplot as plt

data = pandas.read_csv(
        'D:/PDABook/第五章/5.4 结构分析/结构分析.csv',
        engine='python', encoding='utf-8'
        )

#gender列 + label + 计数
ga = data.groupby(by=['gender'])['id'].agg('count')

# =============================================================================
# #总用户
# print(ga.sum())
# 
# #不同性别用户比例
# print(ga / ga.sum())
# 
# =============================================================================

#设置女性用户颜色
femaleColor = (91/255, 155/255, 213/255, 0.5)
#设置男性用户颜色
maleColor =(91/255, 155/255, 213/255, 1)

font = matplotlib.font_manager.FontProperties(
        fname='D:/PDABook/SourceHanSansCN-Light.otf', size=10
        )
#设置圆形的饼图
#百分号%是占用符号，用%%表示一个%
plt.axis('equal')
plt.pie(
        ga, 
        labels=['女', '男'],
        colors=[femaleColor, maleColor],
        autopct='%.1f%%',
        textprops={'fontproperties': font}
        )
