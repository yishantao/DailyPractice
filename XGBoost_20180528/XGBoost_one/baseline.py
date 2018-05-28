# -*- coding:utf-8 -*-

"""This module is used to construct XGBoost"""

# 导入必要的工具包
import xgboost as xgb

# 计算分类正确率
from sklearn.metrics import accuracy_score

# read in data,训练集和测试集
my_workpath = './data/'
dtrain = xgb.DMatrix(my_workpath + 'agaricus.txt.train')
dtest = xgb.DMatrix(my_workpath + 'agaricus.txt.test')

# 查看数据情况
# print(dtrain.num_col())
# print(dtrain.num_row())
# print(dtest.num_row())

# specify parameters via map
param = {'max_depth': 2, 'eta': 1, 'silent': 0, 'objective': 'binary:logistic'}

# 设置boosting迭代计算次数
num_round = 2
import time

start_time = time.clock()
bst = xgb.train(param, dtrain, num_round)
end_time = time.clock()
print(end_time - start_time)

# make prediction
train_preds = bst.predict(dtrain)
train_predictions = [round(value) for value in train_preds]
y_train = dtrain.get_label()
train_accuracy = accuracy_score(y_train, train_predictions)
print('Thain Accuary:%.2f%%' % (train_accuracy * 100.0))

# make prediction
preds = bst.predict(dtest)
predictions = [round(value) for value in preds]
y_test = dtest.get_label()
test_accuracy = accuracy_score(y_test, predictions)
print('Thain Accuary:%.2f%%' % (test_accuracy * 100.0))

# from matplotlib import pyplot
# import graphviz
# xgb.plot_tree(bst, num_trees=0, rankdir='LR')
# pyplot.show()
