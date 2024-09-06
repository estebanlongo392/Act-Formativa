import numpy as np
import matplotlib.pyplot as plt

# Definimos la función f(x) = sin(2 * pi * x)
def f(x):
    return np.sin(2 * np.pi * x)

# Nodos equidistantes
nodos = np.array([0, 1/3, 2/3, 1])

# Valores de f(x) en los nodos
valores_f = f(nodos)

# Polinomios cuadráticos por tramos
def polinomio_cuadratico(x, x0, x1, f0, f1, f_deriv):
    # Polinomio de la forma a*(x-x0)^2 + b*(x-x0) + c
    # Se construye a partir de f(x0), f(x1) y la derivada en x0 (f'(x0))
    c = f0
    b = f_deriv
    a = (f1 - f0 - b*(x1 - x0)) / ((x1 - x0)**2)
    return a*(x - x0)**2 + b*(x - x0) + c

# Derivada aproximada de f(x) = sin(2pi * x)
def derivada_f(x):
    return 2 * np.pi * np.cos(2 * np.pi * x)

# Trazador cuadrático en cada subintervalo
x_grafica = np.linspace(0, 1, 1000)
y_trazador = np.zeros_like(x_grafica)

# Calcular el trazador cuadrático en cada intervalo
for i in range(len(nodos) - 1):
    x0 = nodos[i]
    x1 = nodos[i + 1]
    f0 = valores_f[i]
    f1 = valores_f[i + 1]
    f_deriv = derivada_f(x0)
    
    # Aplicamos el polinomio cuadrático para cada subintervalo
    indices = np.where((x_grafica >= x0) & (x_grafica <= x1))
    y_trazador[indices] = polinomio_cuadratico(x_grafica[indices], x0, x1, f0, f1, f_deriv)

# Gráfica
y_funcion_original = f(x_grafica)

plt.plot(x_grafica, y_funcion_original, label=r'$f(x) = \sin(2\pi x)$', color='blue')
plt.plot(x_grafica, y_trazador, label='Trazador Cuadrático', linestyle='--', color='red')

# Mostrar los nodos en la gráfica
plt.scatter(nodos, valores_f, color='green', label='Nodos', zorder=5)

# Detalles de la gráfica
plt.title('Aproximación con Trazador Cuadrático')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)

# Mostrar los nodos
for i, nodo in enumerate(nodos):
    plt.text(nodo, valores_f[i], f'({nodo:.2f}, {valores_f[i]:.2f})', fontsize=9, ha='right')

plt.show()

# Imprimir nodos y valores de f(x) en consola
print("Nodos: ", nodos)
print("Valores de f(x) en los nodos: ", valores_f)
