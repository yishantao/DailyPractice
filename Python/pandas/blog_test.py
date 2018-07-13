import pandas as pd

data = pd.DataFrame(
    {'name': ['zhangsan', 'zhangsan', 'lisi', 'lisi'], 'category': ['one', 'two', 'one', 'two'],
     'number': [1, 2, 3, 4], 'count': [6, 9, 2, 9]})
print(data[~data['number'].isin([2])])
