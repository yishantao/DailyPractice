import pandas as pd

data = pd.DataFrame({'a': [1, 2, 3], 'b': ['hello', 'world', 'china']})
# data['b'] = data['b'].map({'hello': 'A', 'world': 'b', 'china': 'c'})
# print(data)

# data['new'] = data['a'].apply(lambda x: 1 if x > 2 else 0)
# print(data)

# data['new'] = data.apply(lambda x: x['a'] * x['a'], axis=1)
# print(data)

# data = data.applymap(lambda x: x * 2 if isinstance(x, int) else x)
# print(data)

# data = pd.DataFrame({'a': [1, 2, 3, 5], 'b': ['hello', 'world', 'china', 'china']})
# data = data.groupby('b').mean()
# print(data)
