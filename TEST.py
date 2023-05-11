import numpy as np
from scipy.special import legendre
from numpy.polynomial.legendre import legfit
import matplotlib.pyplot as plt


def f(x):
    return np.sin(x)
n = 5
m = n + 1
x = np.linspace(-1, 1, m)
y = f(x)
a = legfit(x, y, n)

def approx(x):
    return sum(a[k] * legendre(k)(x) for k in range(n+1))

x_test = np.linspace(-1, 1, 101)
y_test = f(x_test)
y_approx = approx(x_test)

plt.plot(x_test, y_test, label='True Function')
plt.plot(x_test, y_approx, label='Legendre Approximation')
plt.legend()
plt.show()
