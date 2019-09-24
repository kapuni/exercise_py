# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 21:13:33 2019

@author: kapuni
"""

import pandas
data = pandas.DataFrame(
        data={
                'name':['KEN', 'John', 'JIMI'],
                'age': [21, 22, 23]
            }
        )

data.to_csv(
        'D:/python/works/data_analysis/data.csv',
        index=False
        )