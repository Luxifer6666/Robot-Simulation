% INSTITUTO POLITÉCNICO NACIONAL
% UNIDAD PROFESIONAL INTERDISCIPLINARIA EN INGENIERÍA Y TECNOLOGÍAS AVANZADAS
% SERVICIO SOCIAL - EDUARDO CRUZ OMAÑA - 2025

clc; clear; close all;

% Longitud de los eslabones
L1 = 2;
L2 = 1.5;

% Ángulos en radianes (modifica estos valores según sea necesario)
theta1 = deg2rad(90); % Ángulo del primer eslabón
theta2 = deg2rad(90);  % Ángulo del segundo eslabón
theta_base = deg2rad(180); % Ángulo de la base

% Obtener posiciones
[pos1, pos2] = actualizar_posiciones(L1, L2, theta1, theta2, theta_base);

% Graficar
figure;
plot3([0, pos1(1)], [0, pos1(2)], [0, pos1(3)], 'b', 'LineWidth', 4); hold on;
plot3([pos1(1), pos2(1)], [pos1(2), pos2(2)], [pos1(3), pos2(3)], 'g', 'LineWidth', 4);

% Configuración del gráfico
xlabel('X'); ylabel('Y'); zlabel('Z');
title('Brazo Robótico en 3D (Eslabón 1 en Y, Eslabón 2 en Y y base en eje Z)');
axis([-3 3 -3 3 -3 3]); grid on;
view(3);

% Función para actualizar posiciones
function [pos1, pos2] = actualizar_posiciones(L1, L2, theta1, theta2, theta_base)
    % Posición del primer eslabón en su propio plano (sin rotar la base todavía)
    x1_local = L1 * cos(theta1);
    z1_local = L1 * sin(theta1);
    
    % Rotación de la base en torno al eje Y
    x1 = x1_local * cos(theta_base);
    y1 = x1_local * sin(theta_base);
    z1 = z1_local;
    
    % Posición del segundo eslabón respecto al primero
    x2_local = x1_local + L2 * cos(theta1 + theta2);
    z2_local = z1_local + L2 * sin(theta1 + theta2);
    
    % Aplicamos la misma rotación de la base al segundo eslabón
    x2 = x2_local * cos(theta_base);
    y2 = x2_local * sin(theta_base);
    z2 = z2_local;
    
    pos1 = [x1, y1, z1];
    pos2 = [x2, y2, z2];
end
