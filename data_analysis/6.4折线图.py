# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 10:14:55 2019

@author: kapuni
"""

import pandas
import matplotlib
from matplotlib import pyplot as plt


data = pandas.read_csv(
        'D:/PDABook/第六章/6.4 折线图/折线图.csv',
        engine='python', encoding='utf-8'
        )
#日期格式转换
data['reg_date'] = pandas.to_datetime(
        data['reg_date']
        )
#按照注册天数分组。按照id列进行计数统计
ga = data.groupby(
        by=['reg_date'], as_index=False
        )['id'].agg('count')
#对数据框的列重命名
ga.columns = ['注册日期', '注册用户数']
 
mainColor = (91/255,155/255,213/255,1)
#设置字体
font = matplotlib.font_manager.FontProperties(
        fname='D:/PDABook/SourceHanSansCN-Light.otf', size=10
        )
labelFont = matplotlib.font_manager.FontProperties(
        fname='D:/PDABook/SourceHanSansCN-Light.otf', size=15
        )
#y轴范围
plt.ylim(0,500)
#设置标题
plt.title('注册用户数',color=mainColor, fontproperties=labelFont)
#设置想x，y轴的标签
plt.xlabel('注册日期',color=mainColor, fontproperties=labelFont)
plt.ylabel('注册用户数',color=mainColor, fontproperties=labelFont)

#设置x。y坐标轴样式
plt.xticks(color=mainColor, fontproperties=labelFont)
plt.yticks(color=mainColor, fontproperties=labelFont)

plt.plot(ga['注册日期'], ga['注册用户数'], '-',lw=2, c=mainColor)
