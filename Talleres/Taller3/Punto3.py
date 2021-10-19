from __future__ import division, absolute_import, print_function
import functools
import warnings
import numpy.core.numeric as NX
import numpy as np
from numpy.core import finfo,dot
from numpy.core import overrides
from numpy.core.overrides import set_module
from numpy.lib.twodim_base import vander
from numpy.linalg import lstsq, inv

array_function_dispatch = functools.partial(
    overrides.array_function_dispatch, module='numpy')

@set_module('numpy')
class RankWarning(UserWarning):
    """
    Issued by `polyfit` when the Vandermonde matrix is rank deficient.
    For more information, a way to suppress the warning, and an example of
    `RankWarning` being issued, see `polyfit`.
    """
    pass

def polyfit(x, y, deg, rcond=None, full=False, w=None, cov=False):

    order = int(deg) + 1
    x = NX.asarray(x) + 0.0
    y = NX.asarray(y) + 0.0

    # check arguments.
    if deg < 0:
        raise ValueError("expected deg >= 0")
    if x.ndim != 1:
        raise TypeError("expected 1D vector for x")
    if x.size == 0:
        raise TypeError("expected non-empty vector for x")
    if y.ndim < 1 or y.ndim > 2:
        raise TypeError("expected 1D or 2D array for y")
    if x.shape[0] != y.shape[0]:
        raise TypeError("expected x and y to have same length")

    # set rcond
    if rcond is None:
        rcond = len(x)*finfo(x.dtype).eps

    # set up least squares equation for powers of x
    lhs = vander(x, order)
    rhs = y

    # apply weighting
    if w is not None:
        w = NX.asarray(w) + 0.0
        if w.ndim != 1:
            raise TypeError("expected a 1-d array for weights")
        if w.shape[0] != y.shape[0]:
            raise TypeError("expected w and y to have the same length")
        lhs *= w[:, NX.newaxis]
        if rhs.ndim == 2:
            rhs *= w[:, NX.newaxis]
        else:
            rhs *= w

    # scale lhs to improve condition number and solve
    scale = NX.sqrt((lhs*lhs).sum(axis=0))
    lhs /= scale
    c, resids, rank, s = lstsq(lhs, rhs, rcond)
    c = (c.T/scale).T  # broadcast scale coefficients

    # warn on rank reduction, which indicates an ill conditioned matrix
    if rank != order and not full:
        msg = "Polyfit may be poorly conditioned"
        warnings.warn(msg, RankWarning, stacklevel=4)

    if full:
        return c, resids, rank, s, rcond
    elif cov:
        Vbase = inv(dot(lhs.T, lhs))
        Vbase /= NX.outer(scale, scale)
        if cov == "unscaled":
            fac = 1
        else:
            if len(x) <= order:
                raise ValueError("the number of data points must exceed order "
                                 "to scale the covariance matrix")
            # note, this used to be: fac = resids / (len(x) - order - 2.0)
            # it was deciced that the "- 2" (originally justified by "Bayesian
            # uncertainty analysis") is not was the user expects
            # (see gh-11196 and gh-11197)
            fac = resids / (len(x) - order)
        if y.ndim == 1:
            return c, Vbase * fac
        else:
            return c, Vbase[:,:, NX.newaxis] * fac
    else:
        return c

x = np.array([6,8,10,12,14,16,18,20])
y = np.array([7,9,12,18,21,19,15,10])
print("Hora:   ", x)
print("Grados: ", y)
p1 = polyfit(x,y,1) #Linea roja
p2 = polyfit(x,y,2) #linea azul
p3 = polyfit(x,y,3) #linea rosada
p8 = polyfit(x,y,8) #Linea roja 2
print("\nPolinomio lineal")
print("y = ", p1[0], "x +", p2[1])
print("Polinomio cuadratico")
print("y = ", p2[0], "x^2 +", p2[1], "x", p2[2])
print("Polinomio cubico")
print("y = ", p3[0], "x^3 +", p3[1], "x^2", p3[2], "x +", p3[3])
print("Polinomio de grado ocho")
print("y = ", p8[0], "x^8", p8[1], "x^7 +", p8[2], "x^6", p8[3], "x^5", p8[4], "x^4 +", p8[5], "x^3", p8[6], "x^2 +", p8[7], "x", p8[8])
prediccion_lineal = []
prediccion_cuadratica = []
prediccion_cubica = []
prediccion_grado_ocho = []
error1 = []
error2 = []
error3 = []
i = 6

while i<20.5:
    pendi1=p1[0]
    corte_y1=p1[1]
    prediccion_lineal.append([i,((pendi1*i) + corte_y1)])
    prediccion_cuadratica.append([i, (p2[0]*i**2)+(p2[1]*i)+p2[2]])
    prediccion_cubica.append([i, p3[0]*i**3 + p3[1]*i**2 + p3[2]*i + p3[3]])
    prediccion_grado_ocho = ([i,p8[0]*i**8 + p8[1]*i**7 + p8[2]*i**6 + p8[3]*i**5 + p8[4]*i**4 + p8[5]*i**3 + p8[6]*i**2 + p8[7]*i + p8[8]])
    i = i + 0.5

def print_l(var):
    for i in var:
        print(i)

import matplotlib.pyplot as plt
plt.plot(x,y,'o')
xp = np.linspace(6,20,100)
plt.plot(xp,np.polyval(p1,xp),'r-')
plt.plot(xp,np.polyval(p2,xp),'b--')
plt.plot(xp,np.polyval(p3,xp),'m:')
plt.plot(xp,np.polyval(p8,xp),'r:')
plt.legend(["Puntos originales","Polinomio lineal", "Polinomio cuadratico","Polinomio cubico","Polinomio grado ocho"], loc ="lower right", prop={'size': 9})

print("\nPrediccion_lineal:")
print_l(prediccion_lineal)

print("\nPrediccion_cuadratica:")
print_l(prediccion_cuadratica)

print("\nPrediccion_cubica:")
print_l(prediccion_cubica)

i = 0
for t in prediccion_lineal:
    if t[0] == x[i]:
        error1.append(abs(y[i] - t[1]))
        i = i + 1

i = 0
for z in prediccion_cuadratica:
    if z[0] == x[i]:
        error2.append(abs(y[i] - z[1]))
        i = i + 1

i = 0
for w in prediccion_cubica:
    if w[0] == x[i]:
        error3.append(abs(y[i] - w[1]))
        i = i + 1
print("")
print("Error medio polinomio lineal:", sum(error1)/len(y))
print("Error minimo polinomio lineal:", min(error1))
print("Error maximo polinomio lineal:", max(error1))
jaccard = (1-(sum(error1)/sum(y)))*100
print("Indice de Jaccard polinomio lineal:", jaccard,"\n")

print("Error medio polinomio cuadratica:", sum(error2)/len(y))
print("Error minimo polinomio cuadratica:", min(error2))
print("Error maximo polinomio cuadratica:", max(error2))
jaccard2 = (1-(sum(error2)/sum(y)))*100
print("Indice de Jaccard polinomio cuadratica:", jaccard2,"\n")

print("Error medio polinomio cubica:", sum(error3)/len(y))
print("Error minimo polinomio cubica:", min(error3))
print("Error maximo polinomio cubica:", max(error3))
jaccard3 = (1-(sum(error3)/sum(y)))*100 
print("Indice de Jaccard polinomio cuadratica:", jaccard3, "\n")

plt.show()




