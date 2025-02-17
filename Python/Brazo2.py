# INSTITUTO POLITÉCNICO NACIONAL
# UNIDAD PROFESIONAL INTERDISCIPLINARIA EN INGENIERÍA Y TECNOLOGÍAS AVANZADAS
# SERVICIO SOCIAL - EDUARDO CRUZ OMAÑA - 2025

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Longitud de los eslabones
L1, L2 = 2, 1.5

# Función para actualizar las posiciones de los eslabones
def actualizar_posiciones(theta1, theta2, theta_base):
    """
    - El primer eslabón se mueve en el eje Y (vertical).
    - El segundo eslabón se mueve en el eje X.
    - La base puede rotar en torno al eje Y.
    """
    # Cálculo de la posición del primer eslabón (ahora en Y)
    y1 = L1 * np.cos(theta1)
    z1 = L1 * np.sin(theta1)

    # Posición del segundo eslabón en su propio sistema de referencia
    x2_local = L2 * np.cos(theta2)
    z2_local = z1 + L2 * np.sin(theta2)  # Se suma a z1 para continuidad

    # Aplicar la rotación de la base en Y al segundo eslabón
    x2 = x2_local * np.cos(theta_base)
    y2 = y1  # Mantiene la altura del primer eslabón
    z2 = x2_local * np.sin(theta_base) + z2_local  # Se rota en torno a Y
    
    return (0, y1, z1), (x2, y2, z2)  # El primer eslabón siempre inicia en (0,0,0)

# Configurar el gráfico 3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Establecer límites de los ejes
ax.set_xlim([-3, 3])
ax.set_ylim([-3, 3])
ax.set_zlim([-3, 3])

# Etiquetas de los ejes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Título
ax.set_title('Brazo Robótico en 3D (Eslabón 1 en Y, Eslabón 2 en X y base en eje Z)')

# Variables de ángulos
theta1 = np.radians(90)   # Movimiento en Y
theta2 = np.radians(90)   # Movimiento en X
theta_base = np.radians(0)  # Rotación de la base

# Obtener las posiciones de los eslabones
(x1, y1, z1), (x2, y2, z2) = actualizar_posiciones(theta1, theta2, theta_base)

# Graficar los eslabones
ax.plot([0, 0], [0, y1], [0, z1], color='blue', linewidth=4)  # Primer eslabón (Y)
ax.plot([0, x2], [y1, y2], [z1, z2], color='green', linewidth=4)  # Segundo eslabón (X)

# Mostrar la gráfica
plt.show()
