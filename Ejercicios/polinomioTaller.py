# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 11:30:17 2021

@author: casta
"""
import matplotlib.pyplot as plt
import numpy as np


def funcion(p3,x):
    return p3[0]*x**3 + p3[1]*x**2 + p3[2]*x + p3[3]
def fx(x):
    return -6.39705882352941*x**2 - 2.20588235294117*x + 8.23529411764706
def y(x, p3):
    return x + funcion(p3,0.9049723952296584) - 0.9049723952296584

xf = [0, 1, 2]
yf = [10, 15, 5]
p = np.polyfit(xf,yf,3)
print("Funcion polinomio grado 3: ",p[0],"x^3 + ", p[1],"x^2 + ", p[2], "x + ",p[3])
print("0 evaluado en el polinomio: ", funcion(p,0))
print("1 evaluado en el polinomio: ", funcion(p,1))
print("2 evaluado en el polinomio: ", funcion(p,2))

xp = np.arange(-3, 3, 0.01)
plt.plot(xp, y(xp, p),'m-')
plt.plot(xf,yf,'o')
plt.plot(xp,funcion(p, xp),'r--')
plt.show()
