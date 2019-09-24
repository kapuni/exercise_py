# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 19:28:20 2019

@author: kapuni
"""

import pandas
import numpy as np
from sklearn.linear_model import LinearRegression

data = pandas.read_csv(
        'D:/PDABook/第五章/5.10.2 简单线性回归分析/线性回归.csv',
        engine='python', encoding='utf-8'
        )
#定义自变量
c = data['广告费用(万元)']
#用numpy转换维数   1D --> 2D
x = np.array(c).reshape(-1,1)
#定义因变量
d = data['销售额(万元)']
y = np.array(d).reshape(-1,1)
#计算相关系数
corr = data['广告费用(万元)'].corr(data['销售额(万元)'])
#data.plot('广告费用(万元)', '销售额(万元)', kind='scatter')

lrModel = LinearRegression()
#需要使用reshape数组
lrModel.fit(x,y)

#R2检验拟合程度
print(lrModel.score(x, y))

#输入广告费用 预测销售额
pX = pandas.DataFrame({
        '广告费用(万元)':[20]
        })
print(lrModel.predict(pX))
