import numpy as np

A = np.array([[4410000 * 4410000, 4410000, 1],
              [4830000 * 4830000, 4830000, 1],
              [5250000 * 5250000, 5250000, 1]])

B = np.array([[1165978],
              [1329190],
              [1501474]])

casicero = 1e-15

A = np.array(A, dtype=float)

AB = np.concatenate((A, B), axis=1)
AB0 = np.copy(AB)

tamano = np.shape(AB)
n = tamano[0]
m = tamano[1]

for i in range(0, n - 1, 1):
    columna = abs(AB[i:, i])
    dondemax = np.argmax(columna)

    if (dondemax != 0):
        temporal = np.copy(AB[i, :])
        AB[i, :] = AB[dondemax + i, :]
        AB[dondemax + i, :] = temporal

AB1 = np.copy(AB)

for i in range(0, n - 1, 1):
    pivote = AB[i, i]
    adelante = i + 1
    for k in range(adelante, n, 1):
        factor = AB[k, i] / pivote
        AB[k, :] = AB[k, :] - AB[i, :] * factor
AB2 = np.copy(AB)

ultfila = n - 1
ultcolumna = m - 1
for i in range(ultfila, 0 - 1, -1):
    pivote = AB[i, i]
    atras = i - 1
    for k in range(atras, 0 - 1, -1):
        factor = AB[k, i] / pivote
        AB[k, :] = AB[k, :] - AB[i, :] * factor
    AB[i, :] = AB[i, :] / AB[i, i]
X = np.copy(AB[:, ultcolumna])
X = np.transpose([X])

print('Matriz aumentada:')
print(AB0)
print('Pivoteo parcial por filas')
print(AB1)
print('eliminacion hacia adelante')
print(AB2)
print('eliminación hacia atrás')
print(AB)
print('solución de X: ')
print(X)

valor = 5000000
ValorTotal = valor**2 * X[0] + valor * X[1] + X[2]
print('El valor total es ')
print(ValorTotal)

import numpy as np
import matplotlib.pyplot as pt

# INGRESO
A = np.array([[4410000 * 4410000 * 4410000, 4410000 * 4410000, 4410000, 1],
              [4830000 * 4830000 * 4830000, 4830000 * 4830000, 4830000, 1],
              [5250000 * 5250000 * 5250000, 5250000 * 5250000, 5250000, 1],
              [5670000 * 5670000 * 5670000, 5670000 * 5670000, 5670000, 1]])

B = np.array([[1165978],
              [1329190],
              [1501474],
              [1682830]])


A = np.array(A, dtype=float)

AB = np.concatenate((A, B), axis=1)
AB0 = np.copy(AB)

tamano = np.shape(AB)
n = tamano[0]
m = tamano[1]

for i in range(0, n - 1, 1):
    columna = abs(AB[i:, i])
    dondemax = np.argmax(columna)

    if (dondemax != 0):
        temporal = np.copy(AB[i, :])
        AB[i, :] = AB[dondemax + i, :]
        AB[dondemax + i, :] = temporal

AB1 = np.copy(AB)

for i in range(0, n - 1, 1):
    pivote = AB[i, i]
    adelante = i + 1
    for k in range(adelante, n, 1):
        factor = AB[k, i] / pivote
        AB[k, :] = AB[k, :] - AB[i, :] * factor
AB2 = np.copy(AB)

ultfila = n - 1
ultcolumna = m - 1
for i in range(ultfila, 0 - 1, -1):
    pivote = AB[i, i]
    atras = i - 1
    for k in range(atras, 0 - 1, -1):
        factor = AB[k, i] / pivote
        AB[k, :] = AB[k, :] - AB[i, :] * factor

    AB[i, :] = AB[i, :] / AB[i, i]
X = np.copy(AB[:, ultcolumna])
X = np.transpose([X])

print('Matriz aumentada:')
print(AB0)
print('Pivoteo parcial por filas')
print(AB1)
print('eliminacion hacia adelante')
print(AB2)
print('eliminación hacia atrás')
print(AB)
print('solución de X: ')
print(X)

valor = 5000000
ValorTotal = valor**3 * X[0] + valor**2 * X[1] + valor * X[2] + X[3]
print('El valor total es ')
print(ValorTotal)

x = [4410000, 4830000, 5000000, 5250000, 5670000]
y = [1165978, 1329190, 1397831, 1501474, 1682830]

pt.plot(x, y, 'o')
pt.plot(x, y, 'm:')
pt.show()