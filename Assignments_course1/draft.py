# import numpy as np
# import math
# from matplotlib import pyplot as plt

# # Differential equation
# # diff = y'= (-x + math.sqrt(x**2 + 4*y))/2


# def diff(x, y):
#     return (-x + math.sqrt(x**2 + 4*y))/2


# x = np.linspace(2, 10, 30)
# y = np.linspace(-1, 5, 30)

# # use x,y
# for j in x:
#     for k in y:
#         slope = diff(j, k)
#         domain = np.linspace(j-0.07, j+0.07, 2)

#         def fun(x1, y1):
#             z = slope*(domain-x1)+y1
#             return z
#         plt.plot(domain, fun(j, k), solid_capstyle='projecting',
#                  solid_joinstyle='bevel')

# plt.title("Slope field y'")
# plt.grid(True)
# plt.show()
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import math

# function that returns dy/dt


def model(y, t):
    dydt = y*math.sin(t*y)
    return dydt


# initial condition
# y0 = 5

# time points
t = np.linspace(0, 2)

# solve ODEs
y0 = 3
y1 = odeint(model, y0, t)
y0 = 6
y2 = odeint(model, y0, t)
y0 = 900
y3 = odeint(model, y0, t)
y0 = 0
y4 = odeint(model, y0, t)
y0 = -2.01
y5 = odeint(model, y0, t)
y0 = -6
y6 = odeint(model, y0, t)
y0 = -9
y7 = odeint(model, y0, t)
# y0 = 0.02
# y8 = odeint(model, y0, t)
# y0 = 0.04
# y9 = odeint(model, y0, t)
# y0 = 0.06
# y10 = odeint(model, y0, t)
# y0 = 0.08
# y11 = odeint(model, y0, t)

# plot results
plt.plot(t, y1, 'r-', linewidth=1)
plt.plot(t, y2, 'r-', linewidth=1)
plt.plot(t, y3, 'r-', linewidth=1)
plt.plot(t, y4, 'r-', linewidth=1)
plt.plot(t, y5, 'r-', linewidth=1)
plt.plot(t, y6, 'r-', linewidth=1)
plt.plot(t, y7, 'r-', linewidth=1)
# plt.plot(t, y8, 'r-', linewidth=1)
# plt.plot(t, y9, 'r-', linewidth=1)
# plt.plot(t, y10, 'r-', linewidth=1)
# plt.plot(t, y11, 'r-', linewidth=1)
plt.xlabel('time')
plt.ylabel('y(t)')
plt.legend()
plt.show()
