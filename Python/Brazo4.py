# INSTITUTO POLITÉCNICO NACIONAL
# UNIDAD PROFESIONAL INTERDISCIPLINARIA EN INGENIERÍA Y TECNOLOGÍAS AVANZADAS
# SERVICIO SOCIAL - EDUARDO CRUZ OMAÑA - 2025

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Longitud de los eslabones
L1, L2 = 2, 1.5

def actualizar_posiciones(theta1, theta2, theta_base):
    # Posición del primer eslabón en su propio plano (sin rotar la base todavía)
    x1_local = L1 * np.cos(theta1)
    z1_local = L1 * np.sin(theta1)
    
    # Rotación de la base en torno al eje Y
    x1 = x1_local * np.cos(theta_base)
    y1 = x1_local * np.sin(theta_base)
    z1 = z1_local

    # Posición del segundo eslabón respecto al primero
    x2_local = x1_local + L2 * np.cos(theta1 + theta2)
    z2_local = z1_local + L2 * np.sin(theta1 + theta2)
    
    # Aplicamos la misma rotación de la base al segundo eslabón
    x2 = x2_local * np.cos(theta_base)
    y2 = x2_local * np.sin(theta_base)
    z2 = z2_local

    return (x1, y1, z1), (x2, y2, z2)

# Configurar la figura
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim([-3, 3])
ax.set_ylim([-3, 3])
ax.set_zlim([-3, 3])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Brazo Robótico 1 Animado')

# Definir movimientos en secuencia
movimientos = [
    {'theta1': (0, 45), 'theta2': (0, 30), 'theta_base': (0, 90)},
    {'theta1': (45, 90), 'theta2': (30, -30), 'theta_base': (90, 0)},
    {'theta1': (90, 90), 'theta2': (-30, -30), 'theta_base': (0, 80)}
]

frames_por_movimiento = 50

theta1_vals, theta2_vals, theta_base_vals = [], [], []
for mov in movimientos:
    theta1_vals.extend(np.radians(np.linspace(mov['theta1'][0], mov['theta1'][1], frames_por_movimiento)))
    theta2_vals.extend(np.radians(np.linspace(mov['theta2'][0], mov['theta2'][1], frames_por_movimiento)))
    theta_base_vals.extend(np.radians(np.linspace(mov['theta_base'][0], mov['theta_base'][1], frames_por_movimiento)))

# Graficar los enlaces
line1, = ax.plot([], [], [], color='blue', linewidth=4)
line2, = ax.plot([], [], [], color='green', linewidth=4)

def init():
    line1.set_data([], [])
    line1.set_3d_properties([])
    line2.set_data([], [])
    line2.set_3d_properties([])
    return line1, line2

def update(frame):
    theta1 = theta1_vals[frame]
    theta2 = theta2_vals[frame]
    theta_base = theta_base_vals[frame]
    (x1, y1, z1), (x2, y2, z2) = actualizar_posiciones(theta1, theta2, theta_base)
    
    line1.set_data([0, x1], [0, y1])
    line1.set_3d_properties([0, z1])
    
    line2.set_data([x1, x2], [y1, y2])
    line2.set_3d_properties([z1, z2])
    
    return line1, line2

anim = FuncAnimation(fig, update, frames=len(theta1_vals), init_func=init, blit=False, interval=50)
plt.show()
