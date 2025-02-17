% INSTITUTO POLITÉCNICO NACIONAL
% UNIDAD PROFESIONAL INTERDISCIPLINARIA EN INGENIERÍA Y TECNOLOGÍAS AVANZADAS
% SERVICIO SOCIAL - EDUARDO CRUZ OMAÑA - 2025

clc; clear; close all;

% Longitud de los eslabones
L0 = 1;
L1 = 2;
L2 = 1.5; % L0 es el eslabón de la base, que no se mueve

% Ángulos en radianes (modifica estos valores según sea necesario)
theta_base = deg2rad(0);
theta1 = deg2rad(90);
theta2 = deg2rad(90);

% Obtener posiciones
[pos0, pos1, pos2] = actualizar_posiciones(L0, L1, L2, theta_base, theta1, theta2);

% Graficar
figure;
plot3([0, pos0(1)], [0, 0], [0, pos0(2)], 'm', 'LineWidth', 4); hold on;
plot3([pos0(1), pos1(1)], [0, 0], [pos0(2), pos1(2)], 'b', 'LineWidth', 4);
plot3([pos1(1), pos2(1)], [0, 0], [pos1(2), pos2(2)], 'g', 'LineWidth', 4);

% Configuración del gráfico
xlabel('X'); ylabel('Y'); zlabel('Z');
title('Brazo Robótico en 3D (Eslabón 1 en Y, Eslabón 2 en Y y Eslabón 3 en Y)');
axis([-5 5 -5 5 -5 5]); grid on;
view(3);

% Función para actualizar posiciones
function [pos0, pos1, pos2] = actualizar_posiciones(L0, L1, L2, theta_base, theta1, theta2)
    % Cálculo de la posición del eslabón 0 (base giratoria)
    x0 = L0 * cos(theta_base);
    z0 = L0 * sin(theta_base);
    
    % Cálculo de la posición del primer eslabón (movimiento en el plano XZ)
    x1 = x0 + L1 * cos(theta_base + theta1);
    z1 = z0 + L1 * sin(theta_base + theta1);
    
    % Cálculo de la posición del segundo eslabón
    x2 = x1 + L2 * cos(theta_base + theta1 + theta2);
    z2 = z1 + L2 * sin(theta_base + theta1 + theta2);
    
    pos0 = [x0, z0];
    pos1 = [x1, z1];
    pos2 = [x2, z2];
end
