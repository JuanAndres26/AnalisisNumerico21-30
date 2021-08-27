import numpy as np
import matplotlib.pyplot as plt
def fx(x):
    return x - np.cos(x)

def gx(x):
    return np.cos(x)


tolerancia = 10**-5
x1 = 0
error = np.abs(gx(x1) - x1)
i = 0

while (error > tolerancia and i<=200):
    print(i, " xi = ", float('{:.5f}'.format(x1)),"f(x) = ", float('{:.5f}'.format(fx(x1))), " g(x1) = ", float('{:.5f}'.format(gx(x1))), " error = ", float('{:.5f}'.format(error)))
    if i > 0 :
        error = np.abs(gx(x1)-x1)
    x1 = gx(x1)
    i = i + 1
    
print("El valor de x, tal que f(x) = 0 es : ",  float('{:.5f}'.format(x1)),"numero de iteraciones ", i)

x = np.linspace(0, 1, 100)
plt.title("Metodo punto fijo")
plt.plot(x,fx(x), label = "f(x)")

plt.grid()
plt.show()