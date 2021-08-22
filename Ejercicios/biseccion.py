from math import *
import matplotlib.pyplot as plt
import numpy as np

def plot():
    x = np.arange(0, pi, 0.01)
    y = x*np.cos(x**2)+1
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('plot')
    plt.show()

def funcion(x):
    return x**3 - 2*x - 5

def alg_biseccion(l_inferior,l_superior,tolerancia):
    x0=l_inferior
    x1=l_superior
    c_iteraciones=0
    if(funcion(l_inferior)*funcion(l_superior)>0):
        print('No podemos garantizar que exista una raiz porque evaluando ambos limites en la funcion tienen el mismo signo')

    while(abs(x1-x0)>tolerancia):
        x0=x1
        x1=(l_inferior+l_superior)/2
        if(funcion(l_inferior)*funcion(x1)<0): #El cambio de signo se da en el intervalo [l_inferior,x1]
            l_superior=x1 #Ahora el nuevo limite superior es el punto medio
        if (funcion(x1) * funcion(l_superior) < 0): #El cambio de signo se da en el intervalo [x1,l_superior]
            l_inferior = x1 #Ahora el nuevo limite inferior es el punto medio
        print('Intervalo = [',l_inferior,',',l_superior,']')
        c_iteraciones += 1

    print('Despues de',c_iteraciones,'iteraciones la raiz aproximada es',x1,'con un error de',abs(funcion(x1)))

alg_biseccion(0,50,10**(-8))


#x**3-2*x**2+(4/3)*x-(8/27)