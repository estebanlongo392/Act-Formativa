import numpy as np
from scipy.interpolate import interp1d

# Datos del problema
x = np.array([3, 4.5, 7, 9])
y = np.array([2.5, 1, 2.5, 0.5])

# 1.1. Construir el trazador lineal
linear_interp = interp1d(x, y, kind='linear')

# 1.2. Estimar el valor en x = 5 usando el trazador lineal
x_val = 5
y_val_linear = linear_interp(x_val)

print(f"El valor estimado para x = 5 es y = {y_val_linear:.2f}")
