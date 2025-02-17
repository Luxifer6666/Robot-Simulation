# INSTITUTO POLITÉCNICO NACIONAL
# UNIDAD PROFESIONAL INTERDISCIPLINARIA EN INGENIERÍA Y TECNOLOGÍAS AVANZADAS
# SERVICIO SOCIAL - EDUARDO CRUZ OMAÑA - 2025

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Longitud de los eslabones
L1, L2 = 2, 1.5

# Función para actualizar las posiciones de los eslabones con rotación correcta de la base
def actualizar_posiciones(theta1, theta2, theta_base):
    # Posición del primer eslabón en su propio plano (sin rotar la base todavía)
    x1_local = L1 * np.cos(theta1)
    z1_local = L1 * np.sin(theta1)

    # Rotación de la base en torno al eje Y
    x1 = x1_local * np.cos(theta_base)
    y1 = x1_local * np.sin(theta_base)
    z1 = z1_local  # Se mantiene en el mismo eje Z

    # Posición del segundo eslabón respecto al primero
    x2_local = x1_local + L2 * np.cos(theta1 + theta2)
    z2_local = z1_local + L2 * np.sin(theta1 + theta2)

    # Aplicamos la misma rotación de la base al segundo eslabón
    x2 = x2_local * np.cos(theta_base)
    y2 = x2_local * np.sin(theta_base)
    z2 = z2_local

    return (x1, y1, z1), (x2, y2, z2)

# Configurar el gráfico 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Establecer límites de los ejes para una buena visualización
ax.set_xlim([-3, 3])
ax.set_ylim([-3, 3])
ax.set_zlim([-3, 3])

# Etiquetas
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Título
ax.set_title('Brazo Robótico en 3D (Eslabón 1 en Y, Eslabón 2 en Y y base en eje Z)')

# Variables de ángulos que puedes modificar
theta1 = np.radians(90)   # Ángulo del primer eslabón (modifica este valor)
theta2 = np.radians(90)   # Ángulo del segundo eslabón (modifica este valor)
theta_base = np.radians(180)  # Ángulo de la base (modifica este valor)

# Obtener las posiciones de los eslabones
(x1, y1, z1), (x2, y2, z2) = actualizar_posiciones(theta1, theta2, theta_base)

# Graficar los eslabones
ax.plot([0, x1], [0, y1], [0, z1], color='blue', linewidth=4)  # Primer eslabón
ax.plot([x1, x2], [y1, y2], [z1, z2], color='green', linewidth=4)  # Segundo eslabón

# Mostrar la gráfica
plt.show()
