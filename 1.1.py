import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Datos del problema
x = np.array([3, 4.5, 7, 9])
y = np.array([2.5, 1, 2.5, 0.5])

# 1.1. Construir el trazador lineal
linear_interp = interp1d(x, y, kind='linear')

# Gráfica del trazador lineal
x_plot = np.linspace(3, 9, 100)  # Puntos para graficar la línea

plt.figure(figsize=(8, 5))
plt.plot(x, y, 'o', label='Datos originales')
plt.plot(x_plot, linear_interp(x_plot), label='Trazador Lineal', color='orange')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Trazador Lineal')
plt.legend()
plt.grid(True)
plt.show()
