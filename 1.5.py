import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Datos proporcionados
x = np.array([3.0, 4.5, 7.0, 9.0])
y = np.array([2.5, 1.0, 2.5, 0.5])

# Construir el trazador cúbico
cs = CubicSpline(x, y, bc_type='natural')

# Estimar el valor en x = 5
x_eval = 5
y_eval = cs(x_eval)

print(f"El valor estimado para x = {x_eval} es y = {y_eval:.4f}")

# Crear una gráfica para visualizar los resultados
x_vals = np.linspace(min(x), max(x), 100)
y_vals = cs(x_vals)

plt.plot(x, y, 'o', label='Datos', color='red')
plt.plot(x_vals, y_vals, label='Trazador cúbico', color='blue')
plt.scatter(x_eval, y_eval, color='green', label=f'Estimación en x={x_eval}', zorder=5)
plt.title('Trazador cúbico y estimación')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
