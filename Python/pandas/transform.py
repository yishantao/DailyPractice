# -*- coding:utf-8 -*-
"""This module is used to test transform"""

import numpy as np
import pandas as pd

data = pd.DataFrame(
    {'name': ['zhangsan', 'zhangsan', 'lisi', 'lisi', 'zhangsan'], 'category': ['one', 'two', 'one', 'two', 'one'],
     'number': [1, 2, 3, 4, 5], 'count': [6, 9, 2, 9, 3]})

# grouped = data.groupby('name').mean().add_prefix('mean_')
# data = pd.merge(data, grouped, left_on='name', right_index=True)
# print(data)

# data = data.groupby('name').transform(np.mean)
# print(data)

# def demean(arr):
#     return arr - arr.mean()
#
# data = data.groupby('name').transform(demean)
# print(data)

# def top(df, column='number'):
#     return df[column].max()
#
#
# data = data.groupby('name', group_keys=False).apply(top, column='count')
# print(data)

data.ix[1:2, ['number', 'count']] = np.nan

fill_mean = lambda g: g.fillna(g.mean())
data = data.groupby('name').apply(fill_mean)
print(data)
