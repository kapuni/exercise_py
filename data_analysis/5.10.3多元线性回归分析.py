# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 16:48:06 2019

@author: kapuni
"""

import pandas
import numpy as np
from sklearn.linear_model import LinearRegression

data = pandas.read_csv(
        'D:/PDABook/第五章/5.10.3 多重线性回归分析/线性回归.csv',
        engine='python', encoding='utf-8'
        )
#自变量
a = data[['广告费用(万元)', '客流量(万人次)']]
x = np.array(a).reshape(-1,2)
#因变量
b = data[['销售额(万元)']]
y = np.array(b).reshape(-1,1)
#计算相关系数
x1 = data['广告费用(万元)'].corr(data['销售额(万元)'])
data['客流量(万人次)'].corr(data['销售额(万元)'])

#data.plot('广告费用(万元)', '销售额(万元)', kind='scatter')

#data.plot('客流量(万人次)', '销售额(万元)', kind='scatter')

lrModel = LinearRegression()
lrModel.fit(x,y)

print(lrModel.coef_)
print(lrModel.score(x, y))

pX = pandas.DataFrame({
        '广告费用(万元)':[20],
        '客流量(万人次)':[5]
        })

print(lrModel.predict(pX))