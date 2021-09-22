import numpy as np
import math

def intercambioRenglones(v, i, j):
    if len(v.shape) == 1:
        v[i], v[j] = v[j], v[i]
    else:
        v[[i, j], :] = v[[j, i], :]

#Eliminacion de Gauss con renglon pivote escalado
def gauss(a, b, tol):
    n = len(b)

    #Definiendo los factores escalables
    s = np.zeros(n)
    for i in range(n):
        s[i] = max(np.abs(a[i, :]))

    for k in range(0, n - 1):

        #Intercambio de renglones, si se necesita
        p = np.argmax(np.abs(a[k:n, k]) / s[k:n]) + k
        if abs(a[p, k]) < tol: error.err('La matriz es singular')
        if p != k:
            intercambioRenglones(b, k, p)
            intercambioRenglones(s, k, p)
            intercambioRenglones(a, k, p)

        #Eliminacion
        for i in range(k + 1, n):
            if a[i, k] != 0.0:
                lam = a[i, k] / a[k, k]
                a[i, k + 1:n] = a[i, k + 1:n] - lam * a[k, k + 1:n]
                b[i] = b[i] - lam * b[k]
    if abs(a[n - 1, n - 1]) < tol: error.err('La matriz es singular')

    #Substitution en reversa
    b[n - 1] = b[n - 1] / a[n - 1, n - 1]
    for k in range(n - 2, -1, -1):
        b[k] = (b[k] - np.dot(a[k, k + 1:n], b[k + 1:n])) / a[k, k]
    return b

def newtonMultivariado(f, x, tol):
    #Calcular la matriz Jacobiana compuesta por las derivadas parciales de las fi respecto a las variables xj
    def jacobiano(f, x):
        h = 1.0e-4
        n = len(x)
        jac = np.zeros((n, n))
        f0 = f(x)
        #Calcular derivadas parciales por definicion
        for i in range(n):
            temp = x[i]
            x[i] = temp + h
            f1 = f(x)
            x[i] = temp
            jac[:, i] = (f1 - f0) / h
        return jac, f0
    print()
    for i in range(100):
        jac, f0 = jacobiano(f, x)
        #Resolver el sistema que esta dado por la matriz Jacobiana multiplicado por el vector y e igualado por menos el vector F
        y = gauss(jac, -f0, tol)
        print("Iteracion", i, "\t[x,y]:", x, "\t\tMagnitud: ",math.sqrt(np.dot(y, y)))
        #Reescribir la aproximacion inicial
        x = x + y
        #Si la magitud del vector y es menor que la tolerancia finaliza la funcion y retorna el vector x
        if math.sqrt(np.dot(y, y)) < tol:
            return x
    print('Acaba la funcion Newthon por exceder el numero de iteraciones dadas')

def f(x):
    f = np.zeros(len(x))
    #Circunferencia
    f[0] = x[0]**2 + x[1]**2 - 1
    #Recta
    f[1] = x[1] - x[0]
    return f
#Aproximacion inicial
x = np.array([1.0, 1.0])
tol=10E-8
x = newtonMultivariado(f,x,tol)
print('\nLa interseccion del problema dado utilizando el metodo de Newton Multivariado y la aproximacion incial (1,1) es:')
print(x)

