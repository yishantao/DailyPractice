import pandas as pd

data = pd.DataFrame({'A': ["美丽", "漂亮", "漂亮", "美丽"], 'B': [2, 6, 7, 8], 'C': [3, 5, 7, 9], 'D': [10, 15, 20, 25]})
data = data.groupby('A')
# for key, df in data:
#     print(key, df.shape)
print(data['B'])
print(data[['B', 'C']])

# import matplotlib.pyplot as plt
#
# plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
# plt.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号“-”显示为方块的问题
