import numpy as np
from scipy import linalg

a = np.array([[1, -2, 3], [2, -1, 1]])
b = np.array([5, 5])
x = linalg.lstsq(a, b)
print(x)
print(x[0])
