import numpy as np
import matplotlib.pyplot as plt

# Datos proporcionados
x = np.array([3.0, 4.5, 7.0, 9.0])
y = np.array([2.5, 1.0, 2.5, 0.5])

# Función para ajustar un polinomio cuadrático en cada intervalo
def quadratic_spline(x_data, y_data):
    coeffs = []
    for i in range(len(x_data) - 1):
        # Ajuste de un polinomio cuadrático en el intervalo [x_i, x_{i+1}]
        coeff = np.polyfit(x_data[i:i+2], y_data[i:i+2], 2)
        coeffs.append(coeff)
    return coeffs

# Obtener los coeficientes del trazador cuadrático
coeffs = quadratic_spline(x, y)

# Estimar el valor en x = 5
x_eval = 5
for i in range(len(x) - 1):
    if x[i] <= x_eval <= x[i+1]:
        # Usar el polinomio correspondiente al intervalo
        a, b, c = coeffs[i]
        y_eval = a * x_eval**2 + b * x_eval + c
        print(f"El valor estimado para x = {x_eval} es y = {y_eval:.4f}")

# Crear una gráfica para visualizar los resultados
x_vals = np.linspace(min(x), max(x), 100)
y_vals = np.piecewise(x_vals, 
                      [x_vals <= 4.5, (x_vals > 4.5) & (x_vals <= 7.0), x_vals > 7.0],
                      [lambda x: coeffs[0][0]*x**2 + coeffs[0][1]*x + coeffs[0][2],
                       lambda x: coeffs[1][0]*x**2 + coeffs[1][1]*x + coeffs[1][2],
                       lambda x: coeffs[2][0]*x**2 + coeffs[2][1]*x + coeffs[2][2]])

plt.plot(x, y, 'o', label='Datos', color='red')
plt.plot(x_vals, y_vals, label='Trazador cuadrático', color='blue')
plt.scatter(x_eval, y_eval, color='green', label=f'Estimación en x={x_eval}', zorder=5)
plt.title('Trazador cuadrático y estimación')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

