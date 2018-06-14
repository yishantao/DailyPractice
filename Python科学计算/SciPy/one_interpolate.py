import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

x = np.linspace(0, 10, 11)
y = np.sin(x)
xnew = np.linspace(0, 10, 101)
plt.plot(x, y, 'ro')
for kind in ['nearest', 'zero', 'slinear', 'quadratic']:
    f = interpolate.interp1d(x, y, kind=kind)
    ynew = f(xnew)
    plt.plot(xnew, ynew, label=str(kind))
plt.legend(loc='lower right')
plt.show()
