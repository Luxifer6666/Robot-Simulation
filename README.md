# INSTITUTO POLITÉCNICO NACIONAL  
# UNIDAD PROFESIONAL INTERDISCIPLINARIA EN INGENIERÍA Y TECNOLOGÍAS AVANZADAS  
# SERVICIO SOCIAL - EDUARDO CRUZ OMAÑA - 2025  

Este documento explica los códigos de distintas simulaciones de brazos robóticos en 3D, comenzando con modelos simples y aumentando la complejidad hasta llegar a un robot cuadrúpedo.  
Las simulaciones se desarrollaron en Python utilizando Visual Studio Code y, posteriormente, se adaptaron a MATLAB.  

Los robots se representan de manera simplificada mediante líneas para facilitar la comprensión del funcionamiento general de la cinemática robótica. En particular, se aborda la cinemática directa (o forward kinematics), que consiste en calcular la posición y orientación del extremo de un robot a partir de los valores de sus ángulos articulares.  

---

## 🔹 **Brazo 1**  
Este código simula un brazo robótico de dos eslabones con una base rotatoria en 3D. Se calcula la cinemática directa del sistema, determinando la posición final de cada eslabón en el espacio tridimensional según ángulos de entrada.  

<div align="center">
  <img src="https://github.com/user-attachments/assets/16c40605-b86a-4902-9d95-06ecfb39fb94" alt="Figure_1p" width="45%">
  <img src="https://github.com/user-attachments/assets/7b8bc2cf-31ee-4dc3-88cd-4053cc527bb2" alt="Figure_1m" width="43%">
</div>

---

## 🔹 **Brazo 2**  
En esta variante, el primer eslabón se mueve en el eje Y, mientras que el segundo se mueve en el eje X.  

<div align="center">
  <img src="https://github.com/user-attachments/assets/1e14c67c-3c3d-40ab-9b0e-9dd5e89f0df3" alt="Figure_2p" width="45%">
  <img src="https://github.com/user-attachments/assets/e9510ace-b9da-4785-b8ed-d46951b57fa9" alt="Figure_2m" width="45%">
</div>

---

## 🔹 **Brazo 3**  
Se agrega un tercer eslabón fijo en la base, extendiendo la simulación.  

<div align="center">
  <img src="https://github.com/user-attachments/assets/3af5c1ef-87de-461d-8675-81ea6867cc65" alt="Figure_3p" width="45%">
  <img src="https://github.com/user-attachments/assets/0126a0e8-a351-46e1-a6bd-3fa0934b5b64" alt="Figure_3m" width="45%">
</div>

---

## 🔹 **Brazo 4**  
Introduce animación al movimiento del brazo robótico.  

<div align="center">
  <img src="https://github.com/user-attachments/assets/48498484-8fa0-4f1c-955a-6ddc83e468af" alt="Figure_4p" width="45%">
  <img src="https://github.com/user-attachments/assets/49eb3afb-9b77-47d3-9df3-5ee838ae1eda" alt="Figure_4m" width="45%">
</div>

---

## 🔹 **Brazo 5**  
Similar al Brazo 2, pero con animación.  

<div align="center">
  <img src="https://github.com/user-attachments/assets/0b69cf20-6a18-4d28-927d-7a256389c40d" alt="Figure_5p" width="45%">
  <img src="https://github.com/user-attachments/assets/a977a24d-c7b0-413f-adb1-6b08d8f1b577" alt="Figure_5m" width="45%">
</div>

---

## 🔹 **Cuadrúpedo 1**  
Este código modela un robot cuadrúpedo, simulando el movimiento de sus patas mediante cinemática directa.  

<div align="center">
  <img src="https://github.com/user-attachments/assets/ad8ec949-c615-46b7-9b91-879e7ee342a6" alt="Figure_6p" width="45%">
  <img src="https://github.com/user-attachments/assets/7a69099c-4eb1-4fe7-93e6-23ab0098b0e2" alt="Figure_6m" width="45%">
</div>
