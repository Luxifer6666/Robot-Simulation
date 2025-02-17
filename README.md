# INSTITUTO POLITÉCNICO NACIONAL
# UNIDAD PROFESIONAL INTERDISCIPLINARIA EN INGENIERÍA Y TECNOLOGÍAS AVANZADAS
# SERVICIO SOCIAL - EDUARDO CRUZ OMAÑA - 2025


Esta documento explica los códigos de distintas simulaciones de brazos robóticos en 3D, comenzando con modelos simples y aumentando la complejidad hasta llegar a un robot cuadrúpedo. 
Las simulaciones se desarrollaron en Python utilizando Visual Studio Code y, posteriormente, se adaptaron a MATLAB.

Los robots se representan de manera simplificada mediante líneas para facilitar la comprensión del funcionamiento general de la cinemática robótica. En particular, se aborda 
la cinemática directa (o forward kinematics), que consiste en calcular la posición y orientación del extremo de un robot a partir de los valores de sus ángulos articulares.



> Brazo 1: Este código simula un brazo robótico de dos eslabones con una base rotatoria en 3D. Se calcula la cinemática directa del sistema, determinando la posición final de cada
> eslabón en el espacio tridimensional según ángulos de entrada. Se emplean transformaciones de coordenadas para representar el movimiento correcto del brazo y su base. En Python se
> utiliza Matplotlib para la visualización y en MATLAB se implementa un sistema equivalente con gráficos 3D.
![Figure_1p](https://github.com/user-attachments/assets/b0f76702-6fc3-40bf-b89a-455d4e348a5b)
<img src="https://github.com/user-attachments/assets/9e46fadf-2599-480c-99fc-60a0d8ad4011" alt="Figure_1m" width="400">



> Brazo 2: En esta variante, el primer eslabón se mueve en el eje Y, mientras que el segundo se mueve en el eje X. La base también puede girar en torno al eje Y, permitiendo
> diferentes configuraciones de movimiento. Se utilizan funciones trigonométricas para calcular las coordenadas de cada eslabón. La implementación en MATLAB y Python sigue la misma
> lógica pero adaptada a sus respectivos entornos de programación.


> Brazo 3: Se agrega un tercer eslabón fijo en la base, extendiendo la simulación. La base giratoria afecta la posición de los eslabones siguientes, proporcionando un sistema más complejo.
> Se utilizan matrices de transformación para determinar la ubicación final de cada componente. Se representa en gráficos 3D tanto en Python como en MATLAB.


> Brazo 4: Introduce animación al movimiento del brazo robótico. Se define una secuencia de movimientos interpolando ángulos a lo largo del tiempo. En Python, se usa Matplotlib con
> FuncAnimation para generar la animación, mientras que en MATLAB se emplea una estructura iterativa con actualización de los gráficos en cada frame.


> Brazo 5: Similar al Brazo 2, pero con animación. Se simulan cambios progresivos en los ángulos de los eslabones para visualizar el desplazamiento del brazo en tiempo real.
> La implementación sigue el mismo patrón de interpolación y representación gráfica.


> Cuadrúpedo 1: Este código modela un robot cuadrúpedo, simulando el movimiento de sus patas mediante cinemática directa. Se definen bases fijas para cada pata y se calculan las
> posiciones de sus eslabones en el espacio tridimensional. Se interpolan ángulos para animar el movimiento secuencial de las patas, representando un patrón de marcha.
