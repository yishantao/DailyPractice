# -*- coding:utf-8 -*-

"""This module is used for standardization"""

import pandas as pd

# data = pd.DataFrame({'A': [2, 4, 3, 7, 9], 'B': [5, 8, 2, 3, 7]})

# # Min-Max标准化
# from sklearn.preprocessing import MinMaxScaler
#
# # 初始化一个scaler对象
# scaler = MinMaxScaler()
# # 调用scaler的fit_transform方法，把要处理的列作为参数传进去
# print(data)
# # data['A'] = scaler.fit_transform(data[['A']])
# data = scaler.fit_transform(data[['A', 'B']])
# print(data)

# # Z-Score标准化
# from sklearn.preprocessing import scale
#
# data['A'] = scale(data['A'])
# data['B'] = scale(data['B'])
# # data = scale(data[['A', 'B']])
# print(data)

# # Normalizer归一化
# from sklearn.preprocessing import Normalizer
#
# scaler = Normalizer()
# data = scaler.fit_transform(data[['A', 'B']])
# print(data)

# data = pd.DataFrame({'A': [2, 4, 3, 7, 9], 'B': ['大学', '大专', '大专', '硕士', '博士'], 'C': ['男', '男', '女', '女', '男']})
# print(data)

# print(data['B'].drop_duplicates())

# 构建学历字典
# education_level_dict = {'博士': 4, '硕士': 3, '大学': 2, '大专': 1}
# # 调用Map方法进行虚拟变量的转换
# data['B'] = data['B'].map(education_level_dict)
# print(data)


# dummies = pd.get_dummies(
#     data,
#     columns=['C'],
#     prefix=['性别'],
#     prefix_sep='_',
#     dummy_na=False,
#     drop_first=False)
# print(dummies)

# import numpy as np
# from sklearn.preprocessing import Imputer
#
# data = pd.DataFrame({'A': [2, 4, 3, 7, 9], 'B': [11, np.nan, np.nan, 23, 88], 'C': [23, 34, 12, np.nan, 34]})
# print(data)
# print('*' * 35)
# imputer = Imputer(strategy='mean')
# data[['B', 'C']] = imputer.fit_transform(data[['B', 'C']])
# print(data)

# data = pd.DataFrame(
#     {'产品': ['A产品', 'A产品', 'A产品', 'A产品', 'A产品'], '销售额': [4.5, 3.4, 2.5, 2.1, 2.0], '忠诚度': [6.6, 7.0, 4.2, 7.7, 9.1]})

# print(data)

# # 使用VarianceThreshold类进行方差过滤
# from sklearn.feature_selection import VarianceThreshold
#
# # 要生成这个类的对象，就需要一个参数，就是最小方差的阈值，我们先设置为1，
# # 然后调用它的transform方法进行特征值的过滤
# variancethreshold = VarianceThreshold(threshold=0.8)
# variancethreshold.fit_transform(
#     data[['销售额', '忠诚度']]
# )
# # 使用get_support方法，可以得到选择特征列的序号，
# # 然后根据这个序号在原始数据中把对应的列名选择出来即可
# print(variancethreshold.get_support(indices=True))
#
# # 检验为什么“销售额”和“忠诚度”都被选中
# print(data[['销售额', '忠诚度']].std(ddof=0))
# print(variancethreshold.variances_)


data = pd.DataFrame(
    {'产品': ['A产品', 'A产品', 'A产品', 'A产品', 'A产品'], '销售额': [4.5, 3.4, 2.5, 2.1, 2.0], '忠诚度': [6.6, 7.0, 4.2, 7.7, 9.1],
     '投资人数': [22, 12, 4, 8, 13], '年收入': [50, 35, 23, 20, 17]})

# # SelectKBest类，通过回归的方法，以及要选择多少个特征值，
# # 新建一个 SelectKBest对象
# from sklearn.feature_selection import SelectKBest
# from sklearn.feature_selection import f_regression
#
# selectKBest = SelectKBest(
#     f_regression, k=2
# )
#
# # 接着，把自变量选择出来，然后调用fit_transform方法，
# # 把自变量和因变量传入，即可选出相关度最高的两个变量。
# feature = data[['销售额', '忠诚度', '投资人数']]
# bestFeature = selectKBest.fit_transform(
#     feature,
#     data['年收入']
# )
#
# # 我们想要知道这两个自变量的名字，使用get_support方法即可得到相应的列名
# print(feature.columns[selectKBest.get_support()])


# # 使用RFE类，在estimator中，
# # 把我们的基模型设置为线性回归模型LinearRegression,
# # 然后在把我们要选择的特征数设置为2，
# # 接着就可以使用这个rfe对象，把自变量和因变量传入fit_transform方法，
# # 即可得到我们需要的特征值
# from sklearn.feature_selection import RFE
# from sklearn.linear_model import LinearRegression
#
# feature = data[['销售额', '忠诚度', '投资人数']]
#
# rfe = RFE(
#     estimator=LinearRegression(),
#     n_features_to_select=2
# )
# sFeature = rfe.fit_transform(
#     feature,
#     data['年收入']
# )
#
# # 同理，我们要想知道这两个自变量的名字，
# # 使用get_support方法，即可得到对应的列名
# print(rfe.get_support())


# from sklearn.feature_selection import SelectFromModel
# from sklearn.linear_model import LinearRegression
#
# feature = data[['销售额', '忠诚度', '投资人数']]
# lrModel = LinearRegression()
# selectFromModel = SelectFromModel(lrModel)
# selectFromModel.fit_transform(
#     feature,
#     data['年收入']
# )
# print(selectFromModel.get_support())


# # 导入iris特征数据到data变量中
# import pandas
# from sklearn import datasets
# import matplotlib.pyplot as plt
# from sklearn.decomposition import PCA
# from mpl_toolkits.mplot3d import Axes3D
#
# iris = datasets.load_iris()
#
# data = iris.data
#
# # 分类变量到target变量中
# target = iris.target
#
# # 使用主成分分析，将四维数据压缩为三维
# pca_3 = PCA(n_components=3)
# data_pca_3 = pca_3.fit_transform(data)
#
# # 绘图
# colors = {0: 'r', 1: 'b', 2: 'k'}
# markers = {0: 'x', 1: 'D', 2: 'o'}
#
# # 弹出图形
# # %matplotlib qt
#
# # 三维数据
# fig = plt.figure(1, figsize=(8, 6))
# ax = Axes3D(fig, elev=-150, azim=110)
#
# data_pca_gb = pandas.DataFrame(
#     data_pca_3
# ).groupby(target)
#
# for g in data_pca_gb.groups:
#     ax.scatter(
#         data_pca_gb.get_group(g)[0],
#         data_pca_gb.get_group(g)[1],
#         data_pca_gb.get_group(g)[2],
#         c=colors[g],
#         marker=markers[g],
#         cmap=plt.cm.Paired
#     )
# plt.show()
