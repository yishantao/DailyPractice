import numpy as np
from scipy import linalg

A = np.array([[1, -0.3], [-0.1, 0.9]])
evalues, evectors = linalg.eig(A)
print(evalues)
print('*' * 30)
print(evectors)
