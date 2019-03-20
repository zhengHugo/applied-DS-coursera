import numpy as np
import math
from matplotlib import pyplot as plt

# Differential equation
# diff = y'= (-x + math.sqrt(x**2 + 4*y))/2


def diff(x, y):
    return (-x + math.sqrt(x**2 + 4*y))/2


x = np.linspace(2, 10, 30)
y = np.linspace(-1, 5, 30)

# use x,y
for j in x:
    for k in y:
        slope = diff(j, k)
        domain = np.linspace(j-0.07, j+0.07, 2)

        def fun(x1, y1):
            z = slope*(domain-x1)+y1
            return z
        plt.plot(domain, fun(j, k), solid_capstyle='projecting',
                 solid_joinstyle='bevel')

plt.title("Slope field y'")
plt.grid(True)
plt.show()
