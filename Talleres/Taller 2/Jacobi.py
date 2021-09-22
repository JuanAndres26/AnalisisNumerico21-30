import numpy as np

#si una matriz es diagonalmente dominante, entonces es convergente
#Para la primera fila 2 > |0| + |-1|
#Para la segunda fila 2 > |B| + |-1|
#Para la tercera fila A > |-1| + |1|
#Por lo tanto Beta = 0 y Alpha > 2 para garantizar convergencia

A = np.array ([[2.0,0,-1.0],[0,2.0,-1.0],[-1.0,1.0,3.0]])
B = np.array ([1.0,2.0,1.0])

Vinicial = np.array ([1.0,2.0,3.0])
tol = 1*10**(-8)


#definir tamaño de la matriz

tam = np.shape (A)
n = tam [0]
m = tam [1]
Vseg = np.zeros (n,dtype=float)
difer = np.ones (n,dtype=float)
error = tol*2
it = 0
while not (error <= tol or it > 10):
    for i in range (0,n,1):
        new = B [i]
        for j in range (0,m,1):
            if (i!=j):
                new = new - A[i,j] * Vinicial[j]
        new = new/A[i,i]    
        difer[i] = np.abs(new-Vinicial[i])    
        Vseg[i] = new
    error = np.max (difer)
    Vinicial = np.copy(Vseg)
    it = it + 1
    print ("Iteracion n: ",it)    
    print (Vseg)
    print (difer)
    print (error)

