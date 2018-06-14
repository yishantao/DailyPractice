import numpy as np
from scipy import interpolate


def func(x, y):
    return (x + y) * np.exp(-5.0 * (x ** 2 + y ** 2))


# X-Y轴分为15*15的网格
y, x = np.mgrid[-1:1:15j, -1:1:15j]
fvals = func(x, y)  # 计算每个网格点上的函数值

# 二维插值
newfunc = interpolate.interp2d(x, y, fvals, kind='cubic')

# 计算100*100的网格上的插值
xnew = np.linspace(-1, 1, 100)
ynew = np.linspace(-1, 1, 100)
fnew = newfunc(xnew, ynew)
