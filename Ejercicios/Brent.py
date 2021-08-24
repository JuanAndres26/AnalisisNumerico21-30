from scipy.optimize import root_scalar
import matplotlib.pyplot as plt
import numpy as np

#cos(x)**2-x**2

def f(x):
    return np.cos(x)**2-x**2

x = np.arange(-3, 3, 0.1)
y = f(x)
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.title('plot')
plt.show()

sol = root_scalar(f, method="brentq", bracket=(0, 3))
print("Metodo de brent")
print("-Raiz : ", sol.root)      
print("-Interacciones = ", sol.iterations)
print("-Evaluacion = ", sol.function_calls)



