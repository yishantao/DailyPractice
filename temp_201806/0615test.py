import numpy as np
import pandas as pd

# data1 = pd.DataFrame({'a': [np.nan, 1, 2, 3], 'b': [np.nan, np.nan, 5, 6]})
data2 = pd.DataFrame({'a': [5, 6, 7, 8], 'b': [10, 11, 12, 13]}, index=['h', 'i', 'j', 'k'])
print(data2)
print(data2.loc['h', ['a','b']])
