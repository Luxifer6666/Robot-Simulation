# INSTITUTO POLITÉCNICO NACIONAL
# UNIDAD PROFESIONAL INTERDISCIPLINARIA EN INGENIERÍA Y TECNOLOGÍAS AVANZADAS
# SERVICIO SOCIAL - EDUARDO CRUZ OMAÑA - 2025

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Longitud de los eslabones
L0, L1, L2 = 1, 2, 1.5  # L0 es el eslabón de la base, que no se mueve

# Función para actualizar las posiciones de los eslabones
def actualizar_posiciones(theta_base, theta1, theta2):
    # Cálculo de la posición del eslabón 0 (base giratoria)
    x0 = L0 * np.cos(theta_base)
    z0 = L0 * np.sin(theta_base)

    # Cálculo de la posición del primer eslabón (movimiento en el plano XZ)
    x1 = x0 + L1 * np.cos(theta_base + theta1)
    z1 = z0 + L1 * np.sin(theta_base + theta1)

    # Cálculo de la posición del segundo eslabón
    x2 = x1 + L2 * np.cos(theta_base + theta1 + theta2)
    z2 = z1 + L2 * np.sin(theta_base + theta1 + theta2)

    return (x0, z0), (x1, z1), (x2, z2)

# Configurar el gráfico 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Establecer límites de los ejes para una buena visualización
ax.set_xlim([-5, 5])
ax.set_ylim([-5, 5])
ax.set_zlim([-5, 5])

# Etiquetas
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Título
ax.set_title('Brazo Robótico en 3D (Eslabón 1 en Y, Eslabón 2 en Y y Eslabón 3 en Y)')

# Variables de ángulos que puedes modificar
theta_base = np.radians(0)  # Ángulo del primer eslabón
theta1 = np.radians(90)     # Ángulo del segundo eslabón
theta2 = np.radians(90)    # Ángulo del tercer eslabón

# Obtener las posiciones de los eslabones
(x0, z0), (x1, z1), (x2, z2) = actualizar_posiciones(theta_base, theta1, theta2)

# Graficar los eslabones
ax.plot([0, x0], [0, 0], [0, z0], color='purple', linewidth=4)  # Eslabón 0 (base)
ax.plot([x0, x1], [0, 0], [z0, z1], color='blue', linewidth=4)  # Primer eslabón
ax.plot([x1, x2], [0, 0], [z1, z2], color='green', linewidth=4)  # Segundo eslabón

# Mostrar la gráfica
plt.show()

