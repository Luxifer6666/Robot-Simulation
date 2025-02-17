% INSTITUTO POLITÉCNICO NACIONAL
% UNIDAD PROFESIONAL INTERDISCIPLINARIA EN INGENIERÍA Y TECNOLOGÍAS AVANZADAS
% SERVICIO SOCIAL - EDUARDO CRUZ OMAÑA - 2025

clc; clear; close all;

% Longitud de los eslabones
L1 = 2;
L2 = 1.5;

% Definir el número de frames
frames_por_movimiento = 50;

% Definir movimientos en secuencia
movimientos = [
    struct('theta1', [0, 45], 'theta2', [0, 30], 'theta_base', [0, 90]);
    struct('theta1', [45, 90], 'theta2', [30, -30], 'theta_base', [90, 0]);
    struct('theta1', [90, 90], 'theta2', [-30, -30], 'theta_base', [0, 80])
];

% Preparar valores de ángulos
theta1_vals = [];
theta2_vals = [];
theta_base_vals = [];

for i = 1:length(movimientos)
    theta1_vals = [theta1_vals, linspace(deg2rad(movimientos(i).theta1(1)), deg2rad(movimientos(i).theta1(2)), frames_por_movimiento)];
    theta2_vals = [theta2_vals, linspace(deg2rad(movimientos(i).theta2(1)), deg2rad(movimientos(i).theta2(2)), frames_por_movimiento)];
    theta_base_vals = [theta_base_vals, linspace(deg2rad(movimientos(i).theta_base(1)), deg2rad(movimientos(i).theta_base(2)), frames_por_movimiento)];
end

% Configurar la figura
figure;
axis([-3 3 -3 3 -3 3]);
xlabel('X'); ylabel('Y'); zlabel('Z');
title('Brazo Robótico 1 Animado');
grid on;
hold on;
view(3);

% Crear líneas para animación
line1 = plot3([0, 0], [0, 0], [0, 0], 'b', 'LineWidth', 4);
line2 = plot3([0, 0], [0, 0], [0, 0], 'g', 'LineWidth', 4);

for frame = 1:length(theta1_vals)
    theta1 = theta1_vals(frame);
    theta2 = theta2_vals(frame);
    theta_base = theta_base_vals(frame);
    
    [pos1, pos2] = actualizar_posiciones(L1, L2, theta1, theta2, theta_base);
    
    set(line1, 'XData', [0, pos1(1)], 'YData', [0, pos1(2)], 'ZData', [0, pos1(3)]);
    set(line2, 'XData', [pos1(1), pos2(1)], 'YData', [pos1(2), pos2(2)], 'ZData', [pos1(3), pos2(3)]);
    
    pause(0.05);
end

% Función para actualizar posiciones
function [pos1, pos2] = actualizar_posiciones(L1, L2, theta1, theta2, theta_base)
    x1_local = L1 * cos(theta1);
    z1_local = L1 * sin(theta1);
    
    x1 = x1_local * cos(theta_base);
    y1 = x1_local * sin(theta_base);
    z1 = z1_local;
    
    x2_local = x1_local + L2 * cos(theta1 + theta2);
    z2_local = z1_local + L2 * sin(theta1 + theta2);
    
    x2 = x2_local * cos(theta_base);
    y2 = x2_local * sin(theta_base);
    z2 = z2_local;
    
    pos1 = [x1, y1, z1];
    pos2 = [x2, y2, z2];
end
