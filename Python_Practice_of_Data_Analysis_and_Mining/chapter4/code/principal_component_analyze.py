# -*- coding: utf-8 -*-
# 主成分分析 降维
import pandas as pd
from sklearn.decomposition import PCA

# 参数初始化
inputfile = '../data/principal_component.xls'
outputfile = '../data/dimention_reducted.xls'  # 降维后的数据

data = pd.read_excel(inputfile, header=None)  # 读入数据
# pca = PCA()
# pca.fit(data)
# print(pca.components_)  # 返回模型的各个特征向量
# print('*' * 30)
# print(pca.explained_variance_ratio_)  # 返回各个成分各自的方差百分比

pca = PCA(4)
pca.fit(data)
low_d = pca.transform(data)  # 用它来降低维度
pd.DataFrame(low_d).to_excel(outputfile)
pca.inverse_transform(low_d)  # 必要时可以用inverse_transform()函数来复原数据
print(low_d)
