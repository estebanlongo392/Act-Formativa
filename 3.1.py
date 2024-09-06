import numpy as np
import sympy as sp

# Datos del problema
x_vals = np.array([0, 1, 2, 3])
y_vals = np.array([1, 2, 33, 244])

# Definimos la variable simbólica para x
x = sp.Symbol('x')

# Función para calcular el polinomio de Lagrange
def lagrange_polynomial(x_vals, y_vals):
    n = len(x_vals)
    P = 0
    for i in range(n):
        L_i = 1
        for j in range(n):
            if i != j:
                L_i *= (x - x_vals[j]) / (x_vals[i] - x_vals[j])
        P += y_vals[i] * L_i
    return sp.simplify(P)

# Calculamos el polinomio de Lagrange
P = lagrange_polynomial(x_vals, y_vals)
print(f"Polinomio de Lagrange: {P}")

# Evaluamos el polinomio en x = 2.7
P_at_2_7 = P.subs(x, 2.7)
print(f"Valor de P(2.7): {P_at_2_7}")
