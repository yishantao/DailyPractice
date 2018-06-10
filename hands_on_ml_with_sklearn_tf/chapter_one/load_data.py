import os
import numpy as np
import pandas as pd

from download_data import HOUSING_PATH


def load_housing_data(housing_path=HOUSING_PATH):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)


# 返回包含所有数据的DataFrame对象
housing = load_housing_data()
# 查看数据集前5行
print(housing.head())
# 查看数据的描述，包含总行数，每个属性的类型和非空值的数量
print(housing.info())
# 当发现数据某列是重复时，意味着它可能是一项表示类别的属性。可以使用value_count()方法查看该项中有那些类别。
print(housing["ocean_proximity"].value_counts())
# describe()方法展示数值属性的概括
print(housing.describe())
# 柱状图
# import matplotlib.pyplot as plt
#
# housing.hist(bins=50, figsize=(20, 15))
# plt.show()

housing["income_cat"] = np.ceil(housing["median_income"] / 1.5)
# 将所有大于5的分类归入到分类5
housing["income_cat"].where(housing["income_cat"] < 5, 5.0, inplace=True)

from sklearn.model_selection import StratifiedShuffleSplit

split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)

for train_index, test_index in split.split(housing, housing["income_cat"]):
    strat_train_set = housing.loc[train_index]
    strat_test_set = housing.loc[test_index]

# print(housing['income_cat'].value_counts() / len(housing))

# 删除income_cat属性，使数据回到初始状态
for set in (strat_train_set, strat_test_set):
    set.drop(["income_cat"], axis=1, inplace=True)