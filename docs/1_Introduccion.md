---
marp        : true
auto-scaling:
    - true
    - fittingHeader
    - math
    - code
paginate        : true
theme           : hegel
title           : Robótica
author          : Raúl Lara Cabrera
description     : Presentación de la asignatura Robótica
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
<div class="author">Alberto Díaz, Raúl Lara</div>
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
<!--
   _class: transition
-->

# Evolución de los robots

---

![bg left:33%](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4a/Mechanical_Pinochio.gif/361px-Mechanical_Pinochio.gif)

# Autómatas

Son máquinas relativamente autónomas, o mecanismos de control diseñados para seguir automáticamente una secuencia de operaciones, o responder a instrucciones predeterminadas.

Se tienen registros desde el antiguo Egipto hasta nuestros días (animatrónics).

---

<video controls width=100% src="https://upload.wikimedia.org/wikipedia/commons/1/1a/Cima_automaton.ogv" poster="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Cima_automaton.ogv/1280px--Cima_automaton.ogv.jpg"></video>

---

![bg right:50%](https://upload.wikimedia.org/wikipedia/commons/8/83/Ajedrecista_segundo2.JPG)
# Principios del siglo XX

En 1912, **Leonardo Torres y Quevedo** construye la primera máquina autónoma capaz de jugar al ajedrez: *El Ajedrecista*.

Intenta hacer mate en un escenario reducido de final de partida.

Capaz de detectar movimientos incorrectos del oponente señalándolos con una bombilla.

---

<video controls width=100% src="https://drive.upm.es/s/V5temgyKuoHbvq9/download"></video>

---

![bg left:40%](https://upload.wikimedia.org/wikipedia/commons/thumb/9/9b/FANUC_6-axis_welding_robots.jpg/1280px-FANUC_6-axis_welding_robots.jpg)

# Robots industriales

Empiezan a desarrollarse en los 1930.

Articulados a imagen y semejanza de brazos humanos.

Inicialmente replicando el movimiento del operador.

Entran en juego la automatización y el **control numérico**.

---

<video controls width=100% src="https://drive.upm.es/s/QdVyi48T8sYgj81/download"></video>

---

![bg right:33%](https://www.ntticc.or.jp/uploads/assets/000/c7d5b.179.large.jpg)
# Década de los 70: autonomía y control

La industria armamentística se convierte en la punta de lanza de la robótica, creando munición autónoma 'fire-and-forget'.

Se crea el primer robot capaz de caminar como un humano: **WABOT-1**. Incluía síntesis de voz, manipulación de objetos y entendía órdenes habladas en japonés.

---

<video controls width=100% src="https://drive.upm.es/s/pJvoVnJPhYhRS6l/download"></video>

---

![bg left:30%](https://robots.ieee.org/robots/aibo/aibo-thumb@2x.jpg)
# 80s/90s: humanoides, sistemas inteligentes y robótica de consumo

La tendencia de humanizar a los robots se dispara en esta época.

Honda desarrolla dos versiones de su robot humanoide inteligente: P2 y P3.

Sony presenta su mascota robot, **AIBO**, capaz de seguir una pelota gracias a su módulo de visión por computador. Este robot está dotado de inteligencia artificial para reconocer órdenes, establecer una relación empática con el propietario, recordar caras, etc.

---

<video controls width=100% src="https://drive.upm.es/s/Q3ehKj81lDdz0vh/download"></video>

---

![bg right:33%](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6b/Roomba3g.jpg/1200px-Roomba3g.jpg)
# Siglo XXI: de la humanidad a la utilidad

Ya no importa tanto el aspecto humano del robot, sino su utilidad.

La robótica entra de lleno en los hogares: aspiradoras, drones, impresoras 3D, robots de acompañamiento, etc.

El **vehículo autónomo** entra en escena, dando lugar a los primeros modelos comerciales.

Los robots están plenamente establecidos en el tejido productivo de la sociedad.

---

<video controls width=100% src="https://drive.upm.es/s/TNv3HvtF6X2PoV2/download"></video>

---

<!--
   _class: transition
-->

# Clasificaciones y definiciones

---

![bg height:700](../img/t1/taxonomia2.png)

---

![bg height:700](../img/t1/taxonomia.png)

---

# Sensor

Objeto capaz de variar una propiedad ante magnitudes físicas o químicas, llamadas variables de instrumentación, y transformarlas con un transductor en variables eléctricas.

Características deseables:

- es sensible a la propiedad medida
- es insensible a cualquier otra propiedad que se pueda encontrar en el entorno
- no influye en la propiedad medida

**Sensibilidad**: ratio entre la señal de salida y la propiedad medida.

**Resolución**: cambio más pequeño que puede ser detectado en la cantidad que está siento medida.

---

# Actuador

Componente de una máquina que se encarga de mover o controlar un mecanismo o sistema.

Un actuador requiere de una señal de control, normalmente de baja energía, y una fuente de energía:

- Hidráulico
- Neumático
- Eléctrico
- Magnético
- Mecánico

---

# Control

Es el sistema que gestiona el funcionamiento del robot.

Interpreta las señales percibidas por los sensores y hace funcionar los actuadores en consecuencia.

<center>

![Bucle de control cerrado](https://upload.wikimedia.org/wikipedia/commons/thumb/2/24/Feedback_loop_with_descriptions.svg/1024px-Feedback_loop_with_descriptions.svg.png)

</center>

El bucle de control es **esencial** para la automatización industrial

---

# Grados de libertad

Los grados de libertad son el número mínimo de velocidades generalizadas independientes necesarias para definir el estado cinemático de un mecanismo o sistema mecánico.

El número de grados de libertad coincide con el número de ecuaciones necesarias para describir el movimiento.

¿Cuántos grados de libertad tiene...

- ...una locomotora sobre una vía recta?
- ...un brazo humano?
- ...un avión en vuelo?
- ...un barco navegando?

---

# Valle inquietante

<div class="columns">

<div>

Conocido por su voz inglesa **uncanny valley**, es una hipótesis en el campo de la robótica y animación 3D​ que afirma que cuando las réplicas antropomórficas se acercan en exceso a la apariencia y comportamiento de un ser humano real, causan una respuesta de rechazo entre los observadores humanos.

</div>

<div>

![width:600px](https://upload.wikimedia.org/wikipedia/commons/1/14/Valle_inexplicable2.gif)

</div>

</div>

---

<video controls width=100% src="https://drive.upm.es/s/82CBp6Iu0rNQeMM/download"></video>

---

---
