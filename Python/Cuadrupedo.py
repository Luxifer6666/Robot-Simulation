# INSTITUTO POLITÉCNICO NACIONAL
# UNIDAD PROFESIONAL INTERDISCIPLINARIA EN INGENIERÍA Y TECNOLOGÍAS AVANZADAS
# SERVICIO SOCIAL - EDUARDO CRUZ OMAÑA - 2025

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Longitud de los eslabones
L1, L2 = 2, 1.5

# Posiciones de las bases de las cuatro patas (invertidas hacia abajo)
bases = [
    (2.5, 1.5, 0),  # Delantera derecha
    (-2.5, 1.5, 0),  # Delantera izquierda
    (2.5, -1.5, 0),  # Trasera derecha
    (-2.5, -1.5, 0)  # Trasera izquierda
]

def actualizar_posiciones(theta1, theta2, theta_base, base_x, base_y, base_z):
    x1_local = L1 * np.cos(theta1)
    z1_local = -L1 * np.sin(theta1)  # Invertimos para que vaya hacia abajo
    
    x1 = x1_local * np.cos(theta_base) + base_x
    y1 = x1_local * np.sin(theta_base) + base_y
    z1 = z1_local + base_z

    x2_local = x1_local + L2 * np.cos(theta1 + theta2)
    z2_local = z1_local - L2 * np.sin(theta1 + theta2)
    
    x2 = x2_local * np.cos(theta_base) + base_x
    y2 = x2_local * np.sin(theta_base) + base_y
    z2 = z2_local + base_z

    return (x1, y1, z1), (x2, y2, z2)

# Configurar la figura
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.set_xlim([-4, 4])
ax.set_ylim([-4, 4])
ax.set_zlim([-4, 1])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Cuadrúpedo Robótico Animado')

# Dibujar un cuadrado conectando las bases
base_xs, base_ys, base_zs = zip(*bases)
base_xs += (base_xs[0],)
base_ys += (base_ys[0],)
base_zs += (base_zs[0],)
ax.plot(base_xs, base_ys, base_zs, 'r--', linewidth=2)

# Definir movimientos en secuencia   ------> ( Angulo en el que se encuentra ,  Angulo al que se dirige )
movimientos = [
    {'theta1': (0, 115), 'theta2': (0, -45), 'theta_base': (0, 0), 'patas': [0]}, # Izquierda delantera
    {'theta1': (0, 115), 'theta2': (0, -45), 'theta_base': (0, 0), 'patas': [1]}, # Izquierda trasera
    {'theta1': (0, 115), 'theta2': (0, -45), 'theta_base': (0, 0), 'patas': [2]}, # Derecha delantera
    {'theta1': (0, 115), 'theta2': (0, -45), 'theta_base': (0, 0), 'patas': [3]}, # Derecha trasera

    {'theta1': (115, 125), 'theta2': (-45, -55), 'theta_base': (0, 0), 'patas': [0, 1, 2, 3]}
]

frames_por_movimiento = 50

# Inicializamos valores de movimiento para cada pata
theta1_vals = [[] for _ in range(4)]
theta2_vals = [[] for _ in range(4)]
theta_base_vals = [[] for _ in range(4)]

for mov in movimientos:
    patas_mov = mov['patas']
    for i in range(4):
        if i in patas_mov:
            theta1_vals[i].extend(np.radians(np.linspace(mov['theta1'][0], mov['theta1'][1], frames_por_movimiento)))
            theta2_vals[i].extend(np.radians(np.linspace(mov['theta2'][0], mov['theta2'][1], frames_por_movimiento)))
            theta_base_vals[i].extend(np.radians(np.linspace(mov['theta_base'][0], mov['theta_base'][1], frames_por_movimiento)))
        else:
            theta1_vals[i].extend([theta1_vals[i][-1]] * frames_por_movimiento if theta1_vals[i] else [0] * frames_por_movimiento)
            theta2_vals[i].extend([theta2_vals[i][-1]] * frames_por_movimiento if theta2_vals[i] else [0] * frames_por_movimiento)
            theta_base_vals[i].extend([theta_base_vals[i][-1]] * frames_por_movimiento if theta_base_vals[i] else [0] * frames_por_movimiento)

# Graficar los enlaces para las cuatro patas
lines = []
for _ in range(4):
    line1, = ax.plot([], [], [], color='blue', linewidth=4)
    line2, = ax.plot([], [], [], color='green', linewidth=4)
    lines.append((line1, line2))

def init():
    for line1, line2 in lines:
        line1.set_data([], [])
        line1.set_3d_properties([])
        line2.set_data([], [])
        line2.set_3d_properties([])
    return sum(lines, ())

def update(frame):
    for i, (base_x, base_y, base_z) in enumerate(bases):
        theta1 = theta1_vals[i][frame]
        theta2 = theta2_vals[i][frame]
        theta_base = theta_base_vals[i][frame]
        (x1, y1, z1), (x2, y2, z2) = actualizar_posiciones(theta1, theta2, theta_base, base_x, base_y, base_z)
        
        line1, line2 = lines[i]
        line1.set_data([base_x, x1], [base_y, y1])
        line1.set_3d_properties([base_z, z1])
        
        line2.set_data([x1, x2], [y1, y2])
        line2.set_3d_properties([z1, z2])
    
    return sum(lines, ())

anim = FuncAnimation(fig, update, frames=len(theta1_vals[0]), init_func=init, blit=False, interval=50)
plt.show()
