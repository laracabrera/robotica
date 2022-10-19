<!--
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
-->
<!-- _class: titlepage -->
![bg left:33%](https://images.unsplash.com/photo-1562758778-e5638b5b6607?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=627&q=80)

<div class="title">Robótica</div>
<div class="subtitle">Grado en Ingeniería de Computadores</div>
<div class="author">Alberto Díaz, Raúl Lara</div>
<div class="date">Curso 2022/2023</div>
<div class="organization">Departamento de Sistemas Informáticos</div>

[![height:30](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-informational.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

---

# La asignatura

**Robótica** es una asignatura con enfoque muy práctico donde se introducen los fundamentos del campo de la robótica, centrándose en la construcción y programación de robots móviles autónomos.

Todo el material del curso estará relacionado directamente con los experimentos realizados en las prácticas; los estudiantes trabajarán en grupos construyendo y probando técnicas de sistemas robóticos cada vez más complejas para, con un poco de suerte, finalizar la asignatura con una competición de robots.

---

# Concepto de Robot y estado actual del campo

El término **robot** fue utilizado por primera vez por un dramaturgo checo alrededor de 1920, pero la fascinación de la humanidad por los constructos capaces de percibir el entorno y actuar sobre él ha existido desde siempre.

A día de hoy, disponemos de hardware potente muy asequible, lo que nos permite a prácticamente todos construir (casi) cualquier tipo de robot para múltiples aplicaciones: robots industriales, aspiradoras, drones de reparto, coches autónomos y un largo etcétera. Aunque se trata de un campo de investigación activo, los bloques fundamentales como el modelado, el control o la percepción, están muy bien asentados.

---

# Profesorado

**Alberto Díaz**
Despacho 4122
alberto.diaz@upm.es

**Raúl Lara**
Despacho 1230
raul.lara@upm.es

Horarios y reserva de tutorías en el Moodle de la asignatura.

---

# Contenido

1. Introducción
2. Percepción del entorno
  2.1. Sensores para la navegación
  2.2. Visión artificial
  2.3. Detección de obstáculos
3. Actuación sobre el entorno
4. Control y optimización
  4.1. Control borroso
  4.2. Computación evolutiva para optimización de controladores
5. Toma de decisiones
  5.1. Robot Operating System (ROS)
  5.2. Planificación de trayectorias y navegación
6. Aplicaciones

---

# Evaluación de la asignatura

Cuestionarios telemáticos:

* Uno por cada tema (6 en total)
* Peso del 5% cada uno (30% del total)

Prácticas **presenciales** en grupo:

* Práctica 1. Percepción del entorno (10%)
* Práctica 2. Actuación sobre el entorno (10%)
* Práctica 3. Control y optimización (10%)
* Práctica 4. Toma de decisiones (40%)

---

# Evaluación extraordinaria

Un **examen teórico** (30% de peso sobre la nota final) de tipo test consistente en cuestiones relacionadas con los temas de la asignatura.

La entrega de la **práctica** realizada durante el curso (70% de peso sobre la nota final), donde existe la posibilidad de que el estudiante sea convocado para la exposición de la misma.

El aprobado de ambas partes es **obligatorio** para obtener el aprobado en la asignatura.

# Instalación y uso de la imagen de docker

>**Warning!**
Usar en caso de no tener/querer instalar la extension *Dev Containers* de VSCode. Esto ha sido probado en una distribución de linux, en concreto una basada en Arch Linux, si quieres ayuda mas personalizada, pregunta a tu profesor de confianza.

### Instalación de Docker

Usando tu gestor de paquetes, ejecuta el siguiente comando:

`$ pacman -S docker`

En este caso el gestor de paquetes es `pacman` pero si estas usando una distro derivada de Ubuntu, posiblemente tu gestor sea `apt` (Linux es un mundo, buscate la vida, e instala docker)

### Iniciando el servicio de Docker

Una vez instalado **Docker** debes iniciar el servicio, para ello deberás ejecutar el siguiente comando:

`$ sudo systemctl start docker.service`

Esto iniciara el servicio **Docker** pero sin embargo, cuando reinicies la máquina, deberás volver a iniciarlo. Si no quieres tener que iniciar **Docker** cada vez que enciendes tu máquina, puedes ejecutar:

`$ sudo systemctl enable docker`.

### Usando la imagen de humble con ros2

Para descargar y usar la imagen de **ros2** en **humble hawksbill**, deberás ejecutar el siguiente comandazo:

`$ sudo docker run --rm -it -v /home/mario/dev/robotica:/opt/robotica osrf/ros:humble-desktop-full bash`

Este comando lo que hace es lo siguiente

- `--rm`: es lo que nos permite borrar el contenedor de docker una vez lo *matemos*, es decir, no borra la imagen, si no que borra el contenedor. Si no añadimos esta flag, una vez *matemos* al contenedor, este seguirá ocupando espacio.
- `-it`: simplemente es una abreviación de *interactive* y lo que hace es, una vez descargada la imagen, te mete en ella.
- `-v`: especificamos primero una ruta local en nuestra máquina la cual *uniremos* a una ruta del contenedor, de manera que el código que tengamos en nuestra ruta local, estará sincronizado con el contenedor.
- `bash`: poniendo bash al final, estamos diciendo que nos meta en una bash dentro del contenedor, de esta manera, ya podriamos empezar a ejecutar comandos desde el contenedor.