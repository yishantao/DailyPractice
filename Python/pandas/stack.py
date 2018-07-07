# -*- coding:utf-8 -*-
"""This module is used to test stack"""

import numpy as np
import pandas as pd

data = pd.DataFrame({'category': ['one', 'two', 'one'], 'number': [1, 2, 3]})
# print(data)
# print('*' * 35)
# print(data.stack())

# results = data.stack()
# print(results.unstack())
# print(results.unstack(0))

s1 = pd.Series([0, 1, 2, 3], index=['a', 'b', 'c', 'd'])
s2 = pd.Series([4, 5, 6], index=['c', 'd', 'e'])
data = pd.concat([s1, s2], keys=['one', 'two'])
# print(data)
# print('*' * 35)
# print(data.unstack())
print(data.unstack().stack(dropna=False))
