# -*- coding:utf-8 -*-

"""This module is used to construct early_stop"""

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
num_round = 100

bst = XGBClassifier(max_depth=2, learning_rate=0.1, n_estimators=num_round, silent=True, objective='binary:logistic')
eval_set = [(x_validate, y_validate)]
bst.fit(x_train_part, y_train_part, early_stopping_rounds=10, eval_metric='error', eval_set=eval_set, verbose=True)

# 显示学习曲线，retrieve performance metrics
results = bst.evals_result()
# print(results)
epochs = len(results['validation_0']['error'])
x_axis = range(0, epochs)

# plot log loss
fig, ax = pyplot.subplots()
ax.plot(x_axis, results['validation_0']['error'], label='Test')
ax.legend()
pyplot.ylabel('Error')
pyplot.xlabel('Round')
pyplot.title('XGBoost Early Stop')
pyplot.show()

# 模型训练好后，可以用训练好的模型对测试数据进行预测
# make prediction
preds = bst.predict(x_test)
predictions = [round(value) for value in preds]
test_accuracy = accuracy_score(y_test, predictions)
print('Test Accuracy:%.2f%%' % (test_accuracy * 100.0))
