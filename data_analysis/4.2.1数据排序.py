# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 22:09:03 2019

@author: kapuni
"""

import pandas
data = pandas.read_csv(
        "D:/python/works/data/4.2.1.csv",
        engine='python', encoding='utf8'
        )
sortData = data.sort_values(
        by=['年龄', '性别'],
        ascending=[True, False]
        )