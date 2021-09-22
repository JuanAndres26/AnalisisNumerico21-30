# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 17:39:50 2021

@author: casta
"""

import numpy as np
import math
 
def Cholesky_Decomposicion(matrix, n):
 
    lower = [[0 for x in range(n + 1)]
                for y in range(n + 1)]
 
    # Descomposicion de la matriz a triangular inferior
    try:
        for i in range(n):
            for j in range(i + 1):
                sum1 = 0;
     
                # sumatoria para diagonales
                if (j == i):
                    for k in range(j):
                        sum1 += pow(lower[j][k], 2);
                    lower[j][j] = int(math.sqrt(matrix[j][j] - sum1))
                else:
                     
                    # Evaluacion L(i, j)
                    # utilizando L(j, j)
                    for k in range(j):
                        sum1 += (lower[i][k] *lower[j][k]);
                    if(lower[j][j] > 0):
                        lower[i][j] = int((matrix[i][j] - sum1) /
                                                   lower[j][j])
    # Se saca la matriz triangular inferior y su transposición 
        print("Triangular inferior \t\ Transposicion ")
        for i in range(n):
             
            # Triangular inferior
            for j in range(n):
                print(lower[i][j], end = "\t")
            print("", end = "\t");
             
            # Transposicion de la matriz triangular inferior
        for i in range(n):
            for j in range(n):
                print(lower[j][i], end = "\t")
            print("");
        return lower
    except:
        print("No se cumplen las condiciones de ser una matriz Herminitiana y definida positiva para la descomposicion de Cholesky")
 
   

np.random.seed(2)

def Master_Sequential (A, n): # Juzgar si la expresión maestra secuencial de orden k de A no es cero y si no es cero satisface la condición de descomposición LU
    for i in range(0,n):
        Master = np.zeros([i+1,i+1])
        for row in range(0,i+1):
            for a in range(0,i+1):
                Master[row][a]=A[row][a]
        if np.linalg.det(Master)==0:
            done=False
            return done
def LU_decomposition(A):
    n=len(A[0])
    L = np.zeros([n,n])
    U = np.zeros([n, n])
    for i in range(n):
        L[i][i]=1
        if i==0:
            U[0][0] = A[0][0]
            for j in range(1,n):
                U[0][j]=A[0][j]
                L[j][0]=  '{:.4f}'.format(A[j][0]/U[0][0])
        else:
                for j in range(i, n):#U
                    temp=0
                    for k in range(0, i):
                        temp = temp+L[i][k] * U[k][j]
                    U[i][j]=A[i][j]-temp
                for j in range(i+1, n):#L
                    temp = 0
                    for k in range(0, i ):
                        temp = temp + L[j][k] * U[k][i]
                    L[j][i] = '{:.4f}'.format((A[j][i] - temp)/U[i][i])
    return L,U

A = [[1,-8,-2], [1,1,5], [3,-1,1]] # matriz inicial
n = 3;
if Master_Sequential(A,n) != False:
    L,U=LU_decomposition(A)
    B = np.array([1, 4, -2])
    Y = np.linalg.solve(L,B)#primer paso
    X = np.linalg.solve(U,Y)#segundo Paso
    print("Matriz L : \n",L,'\n', "Matriz U : \n",U)
    print("La solucion del sistema es =",[ "{:0.4f}".format(v) for v in X ])
else:
    print ('La subforma principal de orden k-ésima de A no es toda distinta de cero y no satisface la condición de descomposición LU')
matrix = [[1,-8,-2], [1,1,5], [3,-1,1]]
L = Cholesky_Decomposicion(matrix, n);
print("\n", L)
