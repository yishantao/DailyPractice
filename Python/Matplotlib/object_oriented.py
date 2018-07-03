# import matplotlib.pyplot as plt
#
# fig = plt.gcf()
# axes = plt.gca()
# print(fig, axes)

import pandas as pd

test = pd.Series([1, 2, 3], index=['A', 'B', 'C'])
data = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6], 'c': [7, 8, 9]}, index=['F', 'G', 'H'])
print(data.ix['F':'G', 'a':'b'])
print(data.query('a>2 and b>5'))
