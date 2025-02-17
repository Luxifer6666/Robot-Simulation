% INSTITUTO POLITÉCNICO NACIONAL
% UNIDAD PROFESIONAL INTERDISCIPLINARIA EN INGENIERÍA Y TECNOLOGÍAS AVANZADAS
% SERVICIO SOCIAL - EDUARDO CRUZ OMAÑA - 2025

clc; clear; close all;

% Longitud de los eslabones
L1 = 2;
L2 = 1.5;

% Posiciones de las bases de las cuatro patas (invertidas hacia abajo)
bases = [
    2.5,  1.5, 0;  % Delantera derecha
   -2.5,  1.5, 0;  % Delantera izquierda
    2.5, -1.5, 0;  % Trasera derecha
   -2.5, -1.5, 0   % Trasera izquierda
];

% Configurar la figura
figure;
axis([-4 4 -4 4 -4 1]);
xlabel('X'); ylabel('Y'); zlabel('Z');
title('Cuadrúpedo Robótico Animado');
grid on;
hold on;
view(3);

% Dibujar un cuadrado conectando las bases
plot3([bases(:,1); bases(1,1)], [bases(:,2); bases(1,2)], [bases(:,3); bases(1,3)], 'r--', 'LineWidth', 2);

% Definir movimientos en secuencia
movimientos = {
    [0, 115], [0, -45], [0, 0], [1, 0, 0, 0];
    [0, 115], [0, -45], [0, 0], [0, 1, 0, 0];
    [0, 115], [0, -45], [0, 0], [0, 0, 1, 0];
    [0, 115], [0, -45], [0, 0], [0, 0, 0, 1];
    [115, 125], [-45, -55], [0, 0], [1, 1, 1, 1]
};
frames_por_movimiento = 50;

% Inicializar las líneas para las patas
lines = gobjects(4,2);
for i = 1:4
    lines(i,1) = plot3([0 0], [0 0], [0 0], 'b', 'LineWidth', 4);
    lines(i,2) = plot3([0 0], [0 0], [0 0], 'g', 'LineWidth', 4);
end

% Animación
theta_vals = cell(4,3);
for i = 1:4
    theta_vals{i,1} = linspace(deg2rad(movimientos{1,1}(1)), deg2rad(movimientos{1,1}(2)), frames_por_movimiento);
    theta_vals{i,2} = linspace(deg2rad(movimientos{1,2}(1)), deg2rad(movimientos{1,2}(2)), frames_por_movimiento);
    theta_vals{i,3} = linspace(deg2rad(movimientos{1,3}(1)), deg2rad(movimientos{1,3}(2)), frames_por_movimiento);
end

for frame = 1:frames_por_movimiento
    for i = 1:4
        theta1 = theta_vals{i,1}(frame);
        theta2 = theta_vals{i,2}(frame);
        theta_base = theta_vals{i,3}(frame);
        base_x = bases(i,1);
        base_y = bases(i,2);
        base_z = bases(i,3);
        
        % Calcular posiciones
        x1 = base_x + L1 * cos(theta1);
        z1 = base_z - L1 * sin(theta1);
        x2 = x1 + L2 * cos(theta1 + theta2);
        z2 = z1 - L2 * sin(theta1 + theta2);
        
        % Actualizar las líneas
        set(lines(i,1), 'XData', [base_x x1], 'YData', [base_y base_y], 'ZData', [base_z z1]);
        set(lines(i,2), 'XData', [x1 x2], 'YData', [base_y base_y], 'ZData', [z1 z2]);
    end
    pause(0.05);
end
