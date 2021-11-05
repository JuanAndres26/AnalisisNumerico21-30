from scipy import integrate, interpolate

x = (0.1, 0.2, 0.3, 0.4, 0.5)
y = (1.8, 2.6, 3.0, 2.8, 1.9)

simpson_result = integrate.simpson(y, x)
print("Area bajo la curva(simpson):", simpson_result)
ec_lagrange_interpolation = interpolate.lagrange(x, y)
res_lagrange = integrate.simpson(ec_lagrange_interpolation(x), x)
print('-------------------------------------------')
print('|     POLINOMIO INTERPOLADO(LAGRANGE)     |')
print('-------------------------------------------')
print(ec_lagrange_interpolation)
print('-------------------------------------------')
print("Area bajo la curva(simpson) con la interpolacion lagrange:", res_lagrange)
error = simpson_result - res_lagrange
print("Error Truncamiento:", error)
