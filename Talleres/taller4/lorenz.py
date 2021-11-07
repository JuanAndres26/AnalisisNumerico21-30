import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import Axes3D

x, y, z = sp.symbols('x,y,z')

def f(x,y,z):
    return a * x + y * z, b * (y - z), -x * y + c * y - z


state0 = [1.0, 1.0, 1.0]


def taylor(f, q, w, e, h, t, k):
    p=0
    u = np.zeros([t, 2])
    D = []
    for j in range(1, k + 1):
        D = D + [derive(f, j)]

    for i in range(t):
        g = f.subs(x, a).subs(y, b).subs(z, c)
        v = b + h*g
        for j in range(1, k + 1):
            l = D[j - 1].subs(x, a).subs(y, b).subs(z, c)
            p = float(p + h ** (j + 1) / sp.factorial(j + 1)*l)

            w = p
            q = q + h
            u[i, 0] = q
            u[i, 1] = w
            u[i, 2] = e
            return u

t = np.arange(0.0, 40.0, 0.01)

c = 28.0
b = 10.0
a = 8.0 / 3.0
h = 0.5
t = 100
q = 1.0
w = 1.0
e = 1.0
k = 3

states = taylor(f, q, w, e, h, t, k)

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot(states[:, 0], states[:, 1], states[:, 2])
plt.show()