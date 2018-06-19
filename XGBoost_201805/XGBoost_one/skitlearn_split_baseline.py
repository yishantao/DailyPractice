# -*- coding:utf-8 -*-

"""This module is used to divide training set and test set"""

from xgboost import XGBClassifier
# 加载LibSVM格式数据模块
from sklearn.datasets import load_svmlight_file
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from matplotlib import pyplot

# read in data
my_workpath = './data/'
x_train, y_train = load_svmlight_file(my_workpath + 'agaricus.txt.train')
x_test, y_test = load_svmlight_file(my_workpath + 'agaricus.txt.test')
# print(x_train.shape)

# split data into train and test sets,1/3的训练数据作为校验数据
seed = 7
test_size = 0.33
x_train_part, x_validate, y_train_part, y_validate = train_test_split(x_train, y_train, test_size=test_size,
                                                                      random_state=seed)
# print(x_train_part.shape)

# 设置boosting迭代计算次数
num_round = 2

# bst = XGBClassifier(**params)
bst = XGBClassifier(max_depth=2, learning_rate=1, n_estimators=num_round, silent=True, objective='binary:logistic')
bst.fit(x_train_part, y_train_part)

# 查看模型在校验集上的性能
validate_preds = bst.predict(x_validate)
validate_predictions = [round(value) for value in validate_preds]
train_accuracy = accuracy_score(y_validate, validate_predictions)
print('Validation Accuracy:%.2f%%' % (train_accuracy * 100.0))

# 查看模型在完整训练集上的分类性能
train_preds = bst.predict(x_train)
train_predictions = [round(value) for value in train_preds]
train_accuracy = accuracy_score(y_train, train_predictions)
print('Train Accuracy:%.2f%%' % (train_accuracy * 100.0))

# 模型训练好后，可以用训练好的模型对测试数据进行预测
# make prediction
preds = bst.predict(x_test)
predictions = [round(value) for value in preds]
test_accuracy = accuracy_score(y_test, predictions)
print('Test Accuracy:%.2f%%' % (test_accuracy * 100.0))
