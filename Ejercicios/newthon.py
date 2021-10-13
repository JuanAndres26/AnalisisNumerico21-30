import sympy as sp
from math import *
import matplotlib.pyplot as plt
import numpy as np

def plot():
    x = np.arange(0, 2, 0.01)
    y = -2.1323529411764715*x**3  -1.1029411764705859*x**2 +  8.235294117647056*x +  9.999999999999979
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('plot')
    plt.show()

#def f(x):
    #func=cos(x)-x**3
    #return func

#def df(x):
    #return -sin(x)-3*pow(x,2)
#Pag 58 del libro
#Implementar
def NewtonRaphson (x0, tol, n): #Validar covergencia
    x = sp.symbols('x') #Crea la variable x
    f= -6.39705882352941*x**2 - 2.20588235294117*x + 8.23529411764706 - 1
    df = sp.diff(f) #Calcula la derivada de f, df no puede ser 0
    f=sp.lambdify(x,f)
    df = sp.lambdify(x,df)
    for k in range(n):
        x1=x0-f(x0)/df(x0)
        if(abs(x1-x0)<=tol):
            print('x',k,'=',x1,end=' ')
            print('es una buena aproximacion de la raiz')
            return
        x0=x1
        print('x',k+1,'=',x1)

NewtonRaphson(0,10**(-16),100)
plot()

#cos(x)**2-x**2
#exp(x)-x-1 ; e**x-x-1
#x**3-2*x**2+(4/3)*x-(8/27)
#x**3-2*x-5
#(667.38/x)*(1-exp(-0.146843*x))-40 ; (667.38/x)*(1-e**(-0.146843*x))-40

#Hablar solo el metodo newton, newto rhapson y newthon relajado
#Buscar una raiz y luego la otra