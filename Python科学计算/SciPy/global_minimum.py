# -*- coding:utf-8 -*-

import numpy as np

from scipy import optimize


def func(x, p):
    a, k, theta = p
    return a * np.sin(2 * np.pi * k * x + theta)


def func_error(p, y, x):
    return np.sum((y - func(x, p)) ** 2)


x = np.linspace(0, 2 * np.pi, 100)
a, k, theta = 10, 0.34, np.pi / 6
y = func(x, [a, k, theta])

result = optimize.basinhopping(func_error, (1, 1, 1), niter=10, minimizer_kwargs={'method': 'L-BFGS-B', 'args': (y, x)})
print(result.x)
