---
marp        : true
auto-scaling:
    - true
    - fittingHeader
    - math
    - code
paginate        : true
theme           : hegel
title           : Percepción del entorno
author          : Raúl Lara Cabrera
description     : Percepción del entorno. Curso 2022-2023. E.T.S.I. Sistemas Informáticos (UPM)
math: katex
---
<style>

   .cite-author {
      text-align        : right;
   }
   .cite-author:after {
      color             : orangered;
      font-size         : 125%;
      font-weight       : bold;
      font-family       : Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
      padding-right     : 130px;
   }
   .cite-author[data-text]:after {
      content           : " - "attr(data-text) " - ";
   }

   .cite-author p {
      padding-bottom : 40px
   }

</style>

<!-- _class: titlepage -->
![bg left:33%](https://images.unsplash.com/photo-1597424216843-6c9696c01dbe?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=778&q=80)

<div class="title">Percepción del entorno</div>
<div class="subtitle">Robótica</div>
<div class="author">Alberto Díaz y Raúl Lara</div>
<div class="date">Curso 2022/2023</div>
<div class="organization">Departamento de Sistemas Informáticos</div>

[![height:30](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-informational.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

---

# Percepción

Una de las tareas más importantes de un sistema autónomo es obtener conocimiento de su entorno.

Para ello se toman medidas usando varios **sensores** y extrayendo información útil a partir de esas medidas.

<center>

![h:300](https://upload.wikimedia.org/wikipedia/commons/1/1b/Anemometer.jpg) ![h:300](https://upload.wikimedia.org/wikipedia/commons/2/27/Light_sensor.png) ![h:300](https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Digital_Pressure_Sensor.jpg/1920px-Digital_Pressure_Sensor.jpg)

</center>

---

# Clasificación de los sensores

Vamos a clasificar los sensores en función de dos ejes/características:

Magnitud medida:

- **Propioceptivos**: miden valores internos del sistema, por ejemplo, la velocidad del motor o el voltaje de la batería.
- **Exteroceptivos**: adquieren información del entorno del robot, por ejemplo, mediciones de distancia, intensidad de la luz y amplitud del sonido.

Mecanismo de medición:

- **Pasivos**: miden la energía ambiental que entra en el sensor.
- **Activos**: emiten energía al entorno y miden la respuesta del entorno.

---

# Rendimiento de los sensores

**Rango dinámico**: se utiliza para medir la dispersión entre los límites inferior y superior de los valores de entrada al sensor, manteniendo el funcionamiento normal del mismo. Se mide en decibelios:

$$
DR_P=10\cdot\log\left [\frac{P_{MAX}}{P_{MIN}} \right], DR_V=20\cdot\log\left [\frac{P_{MAX}}{P_{MIN}} \right]
$$

**Resolución**: es la diferencia mínima entre dos valores de medida del sensor.

**Frecuencia** o **ancho de banda**: velocidad a la cual el sensor es capaz de proporcionar lecturas. Se mide en hertzios.

**Sensibilidad**: cambio que debe ocurrir en la medida para que el sensor cambie su salida.

---

# Rendimiento de los sensores

**Linealidad**: es una medida importante que determina el comportamiento de la señal de salida del sensor al variar la señal de entrada:

<center>

![h:350](../img/t3/linearity.jpg)
</center>

**Error**: se define como la diferencia entre las mediciones de salida del sensor y los valores reales que se miden.

---

# Sensores de posición

<!-- _class: cool-list -->

1. *Sensores de motores/ruedas*
1. *Sensores de dirección*
1. *Acelerómetros*
1. *Unidad de medida inercial*
1. *Ground beacons*