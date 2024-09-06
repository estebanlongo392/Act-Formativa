import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt

# Datos del problema
x_vals = np.array([0, 1, 2, 3])
y_vals = np.array([1, 2, 33, 244])

# Construcción del trazador cúbico
cs = CubicSpline(x_vals, y_vals)

# Imprimimos los coeficientes del trazador cúbico en cada intervalo
for i in range(len(cs.c[0])):
    print(f"Polinomio en el intervalo [{x_vals[i]}, {x_vals[i+1]}]: {cs.c[3,i]}*(x - {x_vals[i]})^3 + {cs.c[2,i]}*(x - {x_vals[i]})^2 + {cs.c[1,i]}*(x - {x_vals[i]}) + {cs.c[0,i]}")

# Estimación del valor para x = 2.7
cs_at_2_7 = cs(2.7)
print(f"Valor del trazador cúbico en x = 2.7: {cs_at_2_7}")

# Graficamos el trazador cúbico
x_fine = np.linspace(0, 3, 100)  # Generamos valores de x más detallados para una curva suave
y_fine = cs(x_fine)

plt.plot(x_vals, y_vals, 'o', label='Datos')
plt.plot(x_fine, y_fine, label='Trazador cúbico')
plt.scatter(2.7, cs_at_2_7, color='red', label=f'Estimación en x=2.7: {cs_at_2_7:.2f}')

plt.title('Trazador Cúbico')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()
