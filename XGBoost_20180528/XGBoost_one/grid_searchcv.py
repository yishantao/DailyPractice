# -*- coding:utf-8 -*-

"""This module is used for grid search cv"""

from xgboost import XGBClassifier
# 加载LibSVM格式数据模块
from sklearn.datasets import load_svmlight_file

from sklearn.model_selection import GridSearchCV

from sklearn.metrics import accuracy_score

# read in data
my_workpath = './data/'
x_train, y_train = load_svmlight_file(my_workpath + 'agaricus.txt.train')
x_test, y_test = load_svmlight_file(my_workpath + 'agaricus.txt.test')
# print(x_train.shape)

# 构造模型
bst = XGBClassifier(max_depth=2, learning_rate=0.1, silent=True, objective='binary:logistic')

param_test = {
    'n_estimators': range(1, 51, 1)
}
clf = GridSearchCV(estimator=bst, param_grid=param_test, scoring='accuracy', cv=5)
clf.fit(x_train, y_train)
print(clf.best_params_, clf.best_score_)

# make prediction
preds = clf.predict(x_test)
predictions = [round(value) for value in preds]
test_accuracy = accuracy_score(y_test, predictions)
print('Test Accuracy:%.2f%%' % (test_accuracy * 100.0))
