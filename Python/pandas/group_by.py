# -*- coding:utf-8 -*-
"""This module is used to test groupby"""

import numpy as np
import pandas as pd

data = pd.DataFrame(
    {'name': ['zhangsan', 'zhangsan', 'lisi', 'lisi', 'zhangsan'], 'category': ['one', 'two', 'one', 'two', 'one'],
     'number': [1, 2, 3, 4, 5], 'count': [6, 9, 2, 9, 3]})
# print(data)

# grouped = data['number'].groupby(data['name'])
# print(grouped)
# print(grouped.mean())

# years = np.array(['2017', '2018', '2017', '2018', '2018'])
# grouped = data['number'].groupby([years]).mean()
# print(grouped)

# print(data['number'].groupby('name').mean())
# print(data.groupby('name')['number'].mean())
# print(data.groupby('name').mean())

# print(data.groupby('name').size())
# for name, group in data.groupby('name'):
#     print(name)
#     print(group)

# for (name, category), group in data.groupby(['name', 'category']):
#     print(name, category)
#     print(group)

# print(dict(list(data.groupby('name')))['lisi'])


# print(dict(list(data.groupby([[1, 1, 2, 2]], axis=1)))[1])

# data.groupby('name')['number']
# data.groupby('name')[['number', 'count']]
#
# data['number'].groupby(data['name'])
# data[['number', 'count']].groupby(data['name'])

mapping = {'name': 'a', 'category': 'b', 'number': 'a', 'count': 'b'}


# print(data.groupby(mapping, axis=1).sum())

# map_series = pd.Series(mapping)
# print(data.groupby(map_series, axis=1).sum())

# data = pd.DataFrame(
#     {'name': ['zhangsan', 'zhangsan', 'lisi', 'lisi', 'zhangsan'], 'category': ['one', 'two', 'one', 'two', 'one'],
#      'number': [1, 2, 3, 4, 5], 'count': [6, 9, 2, 9, 3]}, index=['a', 'b', 'aa', 'bb', 'cc'])
# print(data.groupby(len).sum())

# data.groupby([[1, 2, 3, 2, 3], len])

def peak_to_peak(arr):
    return arr.max() - arr.min()

#
# print(data.groupby('name')['number'].agg(peak_to_peak))

# print(data.groupby('name')['number'].agg('mean'))
# print(data.groupby('name')['number'].agg(['mean', 'sum', peak_to_peak]))

# print(data.groupby('name')['number'].agg([('one', 'mean'), ('two', 'sum')]))
# print(data.groupby('name')['number', 'count'].agg([('one', 'mean'), ('two', 'sum')])['number'])

# print(data.groupby('name')['number', 'count'].agg({'number': [('one', 'min'), ('two', 'max')], 'count': 'sum'}))

# print(data.groupby('name', as_index=False)['number'].agg('mean'))
