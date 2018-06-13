import numpy as np
from scipy import linalg

m, n = 500, 50
A = np.random.rand(m, m)
B = np.random.rand(m, n)
X1 = linalg.solve(A, B)
X2 = np.dot(linalg.inv(A), B)
print(np.allclose(X1, X2))

a = np.array([[2, 3, -5], [1, -2, 1], [3, 1, 3]])
b = np.array([3, 0, 7])
x = linalg.solve(a, b)
print(x)
