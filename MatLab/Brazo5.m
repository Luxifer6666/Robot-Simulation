% INSTITUTO POLITÉCNICO NACIONAL
% UNIDAD PROFESIONAL INTERDISCIPLINARIA EN INGENIERÍA Y TECNOLOGÍAS AVANZADAS
% SERVICIO SOCIAL - EDUARDO CRUZ OMAÑA - 2025

clc; clear; close all;

% Longitud de los eslabones
L1 = 2;
L2 = 1.5;

% Configuración de la figura
figure;
ax = axes('XLim', [-3, 3], 'YLim', [-3, 3], 'ZLim', [-3, 7]);
hold on;
grid on;
xlabel('X'); ylabel('Y'); zlabel('Z');
title('Brazo Robótico 2 Animado');
view(3);

% Crear líneas para animación
line1 = line('XData', [], 'YData', [], 'ZData', [], 'LineWidth', 4, 'Color', 'b');
line2 = line('XData', [], 'YData', [], 'ZData', [], 'LineWidth', 4, 'Color', 'g');

% Definir movimientos en secuencia
movimientos = {
    struct('theta1', [0, 45], 'theta2', [0, 30], 'theta_base', [0, 90]),
    struct('theta1', [45, 90], 'theta2', [30, 90], 'theta_base', [90, 90])
};

frames_por_movimiento = 50;
theta1_vals = [];
theta2_vals = [];
theta_base_vals = [];

for i = 1:length(movimientos)
    mov = movimientos{i};
    theta1_vals = [theta1_vals, linspace(deg2rad(mov.theta1(1)), deg2rad(mov.theta1(2)), frames_por_movimiento)];
    theta2_vals = [theta2_vals, linspace(deg2rad(mov.theta2(1)), deg2rad(mov.theta2(2)), frames_por_movimiento)];
    theta_base_vals = [theta_base_vals, linspace(deg2rad(mov.theta_base(1)), deg2rad(mov.theta_base(2)), frames_por_movimiento)];
end

% Función para actualizar las posiciones de los eslabones
function [x1, y1, z1, x2, y2, z2] = actualizar_posiciones(theta1, theta2, theta_base, L1, L2)
    y1 = L1 * cos(theta1);
    z1 = L1 * sin(theta1);
    x2_local = L2 * cos(theta2);
    z2_local = z1 + L2 * sin(theta2);
    x2 = x2_local * cos(theta_base);
    y2 = y1;
    z2 = x2_local * sin(theta_base) + z2_local;
    x1 = 0;
end

% Animación
for frame = 1:length(theta1_vals)
    theta1 = theta1_vals(frame);
    theta2 = theta2_vals(frame);
    theta_base = theta_base_vals(frame);
    [x1, y1, z1, x2, y2, z2] = actualizar_posiciones(theta1, theta2, theta_base, L1, L2);
    
    set(line1, 'XData', [0, x1], 'YData', [0, y1], 'ZData', [0, z1]);
    set(line2, 'XData', [0, x2], 'YData', [y1, y2], 'ZData', [z1, z2]);
    
    pause(0.05);
end
