# -*- coding: utf-8 -*-

"""拉格朗日插值代码"""

import numpy as np
import pandas as pd

from scipy.interpolate import lagrange  # 导入拉格朗日插值函数


def ploy_interp_column(s, n, k=5):
    """
    自定义列向量插值函数
    :param s: 列向量
    :param n: 被插值的位置
    :param k: 取前后的数据个数，默认为5
    :return:
    """
    y = s[list(range(n - k, n)) + list(range(n + 1, n + 1 + k))]  # 取数
    y = y[y.notnull()]  # 剔除空值
    return lagrange(y.index, list(y))(n)  # 插值并返回插值结果


if __name__ == '__main__':
    data = pd.DataFrame({'A': [1, 2, 3, 3, 4, 6], 'B': [11, 22, 33, 44, 55, 66]})
    data['A'][2] = np.nan
    print(data)
    # 逐个元素判断是否需要插值
    for i in data.columns:
        for j in range(len(data)):
            if (data[i].isnull())[j]:  # 如果为空即插值。
                data[i][j] = ploy_interp_column(data[i], j)
    print(data)
