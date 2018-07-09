import pandas as pd

# 加载数据集
df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases'
                 '/breast-cancer-wisconsin/wdbc.data', header=None)

from sklearn.preprocessing import LabelEncoder

X = df.loc[:, 2:].values
y = df.loc[:, 1].values
le = LabelEncoder()
y = le.fit_transform(y)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, stratify=y, random_state=1)

# 在流水线中集成数据转换及评估操作
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline

pipe_lr = make_pipeline(StandardScaler(), PCA(n_components=2), LogisticRegression(random_state=1))

pipe_lr.fit(X_train, y_train)
y_pred = pipe_lr.predict(X_test)
# print('Test Accuracy: %.3f' % pipe_lr.score(X_test, y_test))

# k折交叉验证
import numpy as np
# from sklearn.model_selection import StratifiedKFold
#
# kfold = StratifiedKFold(n_splits=10, random_state=1).split(X_train, y_train)
#
# scores = []
# for k, (train, test) in enumerate(kfold):
#     pipe_lr.fit(X_train[train], y_train[train])
#     score = pipe_lr.score(X_train[test], y_train[test])
#     scores.append(score)
#     print('Fold: %2d, Class dist.: %s, Acc: %.3f' % (k + 1, np.bincount(y_train[train]), score))
#
# print('\nCV accuracy: %.3f +/- %.3f' % (np.mean(scores), np.std(scores)))


from sklearn.model_selection import cross_val_score

scores = cross_val_score(estimator=pipe_lr,
                         X=X_train,
                         y=y_train,
                         cv=10,
                         n_jobs=1)
print('CV accuracy scores: %s' % scores)
print('CV accuracy: %.3f +/- %.3f' % (np.mean(scores), np.std(scores)))

