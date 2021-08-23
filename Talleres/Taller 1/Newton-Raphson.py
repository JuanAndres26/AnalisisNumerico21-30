import sympy as sp
import math
import numpy as np
import matplotlib.pyplot as plt


def error(err):
    xi, yi = zip(*err)
    plt.figure(1)
    plt.title("Relacion entre error")
    plt.xlabel("ei")
    plt.ylabel("ei+1")
    plt.plot(xi, yi)
    plt.show()


def NewtonRaphson(x0, tol, n) -> list:
    rt = []
    x = sp.symbols("x")  # Crea la variable x
    f = input("Digite")  # Donde f es una funcion continua
    # Validar covergencia
    df = sp.diff(f)  # Calcula la derivada de f, df no puede ser 0
    d2f = sp.diff(df)  # Calcula la segunda derivada de f
    f = sp.lambdify(x, f)
    df = sp.lambdify(x, df)
    if d2f == 0:
        print(
            "No se puede realizar el metodo de Newton Rhapson porque la funcion no es derivable al menos dos veces"
        )
        return
    if f(x0) == 0 and df(x0) == 0:
        print(
            "No se puede realizar el metodo de Newton Raphson porque la funcion no es cuadraticamente convergente en el valor inicial"
        )
        return
    error = f(x0)
    for k in range(n):
        # print(k)
        errorA = error  # Error anterior
        x1 = x0 - f(x0) / df(x0)
        error = abs(f(x1))  # Error
        if abs(x1 - x0) <= tol:
            print("x", k, "=", x1, end=" ")
            print("es una buena aproximacion de la raiz")
            return rt
        x0 = x1
        print("x", k + 1, "=", x1)
        if k > 0:
            rt.append((errorA, error))
    return rt


result = []
result = NewtonRaphson(n=100, tol=10e-32, x0=math.pi)
error(result)

#Funciones para ingresar en consolo
# cos(x)**2-x**2
# exp(x)-x-1
# x**3-2*x**2+(4/3)*x-(8/27)
# x**3-2*x-5
# (667.38/x)*(1-exp(-0.146843*x))-40
# 3*sin(x)**3-1-4*sin(x)*cos(x)


