# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 10:52:55 2019

@author: kapuni
"""

import pandas
items = pandas.read_csv(
        'D:/PDABook/第四章/4.5.3 字段匹配/商品名称.csv',
        engine='python', encoding='utf-8'
        )
prices = pandas.read_csv(
        'D:/PDABook/第四章/4.5.3 字段匹配/商品价格.csv',
        engine='python', encoding='utf-8'
        )

#内连接 交集列
itemPrices1 = pandas.merge(
        items,
        prices,
        left_on='id',
        right_on='id'
        )

#左连接 左列为主
itemPrices2 = pandas.merge(
        items,
        prices,
        left_on='id',
        right_on='id',
        how='left'
        )

#左右连接 右列为主
itemPrices3 = pandas.merge(
        items,
        prices,
        left_on='id',
        right_on='id',
        how='right'
        )

#外连接 并集合
itemPrices4 = pandas.merge(
        items,
        prices,
        left_on='id',
        right_on='id',
        how='outer'
        )