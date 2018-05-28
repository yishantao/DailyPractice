# -*- coding:utf-8 -*-

"""This module is used for cross validation"""

from xgboost import XGBClassifier
# 加载LibSVM格式数据模块
from sklearn.datasets import load_svmlight_file
# from sklearn.model_selection import KFold
from sklearn.model_selection import StratifiedKFold
# 对给定参数的单个模型评估
from sklearn.model_selection import cross_val_score

# read in data
my_workpath = './data/'
x_train, y_train = load_svmlight_file(my_workpath + 'agaricus.txt.train')
x_test, y_test = load_svmlight_file(my_workpath + 'agaricus.txt.test')
# print(x_train.shape)

# 设置boosting迭代计算次数
num_round = 2
bst = XGBClassifier(max_depth=2, learning_rate=0.1, n_estimators=num_round, silent=True, objective='binary:logistic')

# 交叉验证，速度比较慢
# stratified k-fold cross validation evaluation of xgboost model
# kfold = KFold(n_splits=10, random_state=7)
kfold = StratifiedKFold(n_splits=10, random_state=7)
results = cross_val_score(bst, x_train, y_train, cv=kfold)
print(results)
print('CV Accuracy: %.2f%% (%.2f%%)' % (results.mean() * 100, results.std() * 100))
