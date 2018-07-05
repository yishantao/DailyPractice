# -*- coding:utf-8 -*-
"""This module is used to test pivot table"""

import numpy as np
import pandas as pd

data = pd.DataFrame(
    {'name': ['zhangsan', 'zhangsan', 'lisi', 'lisi', 'zhangsan'], 'category': ['one', 'two', 'one', 'two', 'one'],
     'number': [1, 2, 3, 4, 5], 'count': [6, 9, 2, 9, 3]})

# data = data.pivot_table(index=['name', 'category'])
# print(data)

# data = data.pivot_table(values=['count'], index=['name', 'category'], columns='number', aggfunc=len)
# print(data)

# data = data.pivot_table(values=['count'], index=['name', 'category'], columns='number', aggfunc=len, fill_value=0)
# print(data)

data = pd.DataFrame({'sample': [1, 2, 3, 4, 5], 'Gender': ['Female', 'Male', 'Female', 'Male', 'Male'],
                     'Hand': ['Left', 'Left', 'Left', 'right', 'right']})
print(pd.crosstab(data.Gender, data.Hand, margins=True))
