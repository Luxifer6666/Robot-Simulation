% INSTITUTO POLITÉCNICO NACIONAL
% UNIDAD PROFESIONAL INTERDISCIPLINARIA EN INGENIERÍA Y TECNOLOGÍAS AVANZADAS
% SERVICIO SOCIAL - EDUARDO CRUZ OMAÑA - 2025

clc; clear; close all;

% Longitud de los eslabones
L1 = 2;
L2 = 1.5;

% Ángulos en radianes (modifica estos valores según sea necesario)
theta1 = deg2rad(90); % Movimiento en Y
theta2 = deg2rad(90); % Movimiento en X
theta_base = deg2rad(0); % Rotación de la base

% Obtener posiciones
[pos1, pos2] = actualizar_posiciones(L1, L2, theta1, theta2, theta_base);

% Graficar
figure;
plot3([0, 0], [0, pos1(2)], [0, pos1(3)], 'b', 'LineWidth', 4); hold on;
plot3([0, pos2(1)], [pos1(2), pos2(2)], [pos1(3), pos2(3)], 'g', 'LineWidth', 4);

% Configuración del gráfico
xlabel('X'); ylabel('Y'); zlabel('Z');
title('Brazo Robótico en 3D (Eslabón 1 en Y, Eslabón 2 en X y base en eje Z)');
axis([-3 3 -3 3 -3 3]); grid on;
view(3);

% Función para actualizar posiciones
function [pos1, pos2] = actualizar_posiciones(L1, L2, theta1, theta2, theta_base)
    % Cálculo de la posición del primer eslabón (en Y)
    y1 = L1 * cos(theta1);
    z1 = L1 * sin(theta1);
    
    % Posición del segundo eslabón en su propio sistema de referencia
    x2_local = L2 * cos(theta2);
    z2_local = z1 + L2 * sin(theta2);
    
    % Aplicar la rotación de la base en Y al segundo eslabón
    x2 = x2_local * cos(theta_base);
    y2 = y1;
    z2 = x2_local * sin(theta_base) + z2_local;
    
    pos1 = [0, y1, z1];
    pos2 = [x2, y2, z2];
end