---
marp        : true
auto-scaling:
    - true
    - fittingHeader
    - math
    - code
paginate        : true
theme           : hegel
title           : Introducción a la robótica
author          : Raúl Lara Cabrera
description     : Introducción de la asignatura Robótica. Curso 2022-2023. E.T.S.I. Sistemas Informáticos (UPM)
---
<style>

   .cite-author {
      text-align        : right;
   }
   .cite-author:after {
      color             : orangered;
      font-size         : 125%;
      /* font-style        : italic; */
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
![bg left:33%](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6e/Racknitz_-_The_Turk_3.jpg/1920px-Racknitz_-_The_Turk_3.jpg)

<div class="title">Introducción</div>
<div class="subtitle">Robótica</div>
<div class="author">Alberto Díaz y Raúl Lara</div>
<div class="date">Curso 2022/2023</div>
<div class="organization">Departamento de Sistemas Informáticos</div>

[![height:30](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-informational.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

---

<!--
   _class: transition
-->

# ¿Qué es un robot?

---

![bg](https://images.unsplash.com/photo-1570222094114-d054a817e56b?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1805&q=80)

---

![bg right:50%](https://upload.wikimedia.org/wikipedia/commons/0/0d/Laproscopic_Surgery_Robot.jpg)

## ¿Un robot tiene que ser una máquina autónoma?

---

![bg](https://images.unsplash.com/photo-1473968512647-3e447244af8f?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1740&q=80)

---

![bg left:50%](https://images.unsplash.com/photo-1568910748155-01ca989dbdd6?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1740&q=80)

## Vale, un robot puede ser total, parcial o no autónomo, pero de alguna manera realiza tareas físicas sobre el mundo real, ¿verdad?

---

![bg](https://upload.wikimedia.org/wikipedia/commons/0/0f/Razer_side-on_view.jpg)

---

![bg right:40%](https://upload.wikimedia.org/wikipedia/commons/thumb/5/5e/LG_CLOi%2C_IFA_2018%2C_Berlin_%28P1070245%29.jpg/1024px-LG_CLOi%2C_IFA_2018%2C_Berlin_%28P1070245%29.jpg)

## Entonces, ¿qué define a un robot?

---

# ¿Cuál es el elemento más diferenciador de un robot?

- Algunos dicen que el bloque de inteligencia artificial donde se toman las decisiones.
- Otros indican que el requisito de una IA no es esencial, ya que un proceso de toma de decisiones basado en if-else nos vale también para generar inteligencia.
- Que claro, si está tomando decisiones inteligentes, ¿cómo podemos no estar hablando de inteligencia artificial?
- Bueno, el proceso de decisión se puede considerar esencial, el tema de una inteligencia artificial no tanto.

---

# Componentes esenciales de un robot

Para el propósito de este curso podemos ponernos de acuerdo en que hay tres componentes esenciales:

- **Sensores**: para percibir tanto el entorno que rodea al robot como su propio estado.
- **Controladores**: para analizar el estado actual y tomar decisiones.
- **Actuadores**: para manipular y realizar acciones sobre el entorno.

---

# Sensores

**Percepción**: Los robots perciben el mundo que les rodea a través de sensores.

Podemos pensar en los sensores de un robot como el análogo de los sentidos humanos:

- Vista: Cámaras, radares LiDAR, ...
- Oído: microfonos
- Tacto: sensor de temperatura, presión, ...
- Gusto y olfato: sensores químicos

Hay sensores que no tienen análogo humano, como GPS (para identificar la posición exacta en el globo, barómetro para identificar la altitud a la que nos encontramos, o detector de campos magnéticos (un compás) para detectar la dirección.

---

# Controladores

**Toma de decisiones**: Basándonos en los datos de los sensores y, opcionalmente, del estado interno del robot, un robot tiene que tomar decisiones para realizar cualquier tarea.

Pueden ser decisiones tan simples como responder un sí o un no. Aunque también pueden ser extremadamente complejas como navegar por un entorno desconocido.

En la práctica, el proceso de toma de decisiones en robótica es complejo, y requiere responder muchas cuestiones para encontrar una respuesta en el árbol de decisión de todas las posibilidades.

Por el camino se pueden usar técnicas sofisticadas, como análisis de imágen o algoritmos de path planning.

---

# Actuadores

Los robots **actúan** sobre el entorno.

Las acciones sobre el entorno se pueden dar de muy diferentes formas para muchos propósitos diferentes:

- Ir de un punto a otro.
- Acelerar o frenar.
- Realizar nuevas medidas del entorno con sensores.
- Comunicarse con humanos u otros robots.
- Los motores y actuadores pueden hacer girar las ruedas, activar .articulaciones o rotar las hélices de un robot.
- Encender un escáner para tomar una medida.
- Emitir luces o sonidos.
- Enviar mensajitos para comunicarse.

---

# Robot

1. Máquina o ingenio electrónico programable que es capaz de manipular objetos y realizar diversas operaciones.
2. Robot que imita la figura y los movimientos de un ser animado.
3. Persona que actúa de manera mecánica o sin emociones.
4. Programa que explora automáticamente la red para encontrar información.

Según el diccionario Collins: "A robot is a machine which is programmed to move and perform certain tasks automatically."

---