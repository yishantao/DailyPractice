# -*- coding:utf-8 -*-

"""This module is used to bulid the model using a mixed XGBoost and skit-learn"""

from xgboost import XGBClassifier
# 加载LibSVM格式数据模块
from sklearn.datasets import load_svmlight_file
from sklearn.metrics import accuracy_score
from matplotlib import pyplot

# read in data
my_workpath = './data/'
x_train, y_train = load_svmlight_file(my_workpath + 'agaricus.txt.train')
x_test, y_test = load_svmlight_file(my_workpath + 'agaricus.txt.test')
# print(x_train.shape)
# print(x_test.shape)

# 设置boosting迭代计算次数
num_round = 2

# bst = XGBClassifier(**params)
bst = XGBClassifier(max_depth=2, learning_rate=1, n_estimators=num_round, silent=True, objective='binary:logistic')
bst.fit(x_train, y_train)

# 查看模型在训练集上的性能
train_preds = bst.predict(x_train)
train_predictions = [round(value) for value in train_preds]
train_accuracy = accuracy_score(y_train, train_predictions)
print('Train Accuracy:%.2f%%' % (train_accuracy * 100.0))

# make prediction
preds = bst.predict(x_test)
predictions = [round(value) for value in preds]
test_accuracy = accuracy_score(y_test, predictions)
print('Test Accuracy:%.2f%%' % (test_accuracy * 100.0))
