---
marp        : true
auto-scaling:
    - true
    - fittingHeader
    - math
    - code
paginate        : true
theme           : hegel
title           : Webots
author          : Raúl Lara Cabrera
description     : Webots. Curso 2022-2023. E.T.S.I. Sistemas Informáticos (UPM)
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

<div class="title">El entorno de simulación Webots</div>
<div class="subtitle">Robótica</div>
<div class="author">Alberto Díaz y Raúl Lara</div>
<div class="date">Curso 2022/2023</div>
<div class="organization">Departamento de Sistemas Informáticos</div>

[![height:30](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-informational.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

---

# Instalación (GNU/Linux)

Añadiendo el repositorio para <i>Advanced Packaging Tool</i> (APT)

Instalando el paquete `.deb` directamente

Desde el tarball (archivo `.tar.bz2`)

Desde snap

Imagen de docker

Modo servidor
  - En caso de que se quiera tener cliente y servidor por separado

---

https://cyberbotics.com/doc/guide/the-3d-window#axis-aligned-handles

---

https://cyberbotics.com/doc/guide/the-scene-tree

---

# Jerarquía de archivos en un proyecto<!--_class: transition-->

---

# Estructura base de directorios

Un proyecto es un directorio con, al menos, un directorio denominado `world/`

- Contiene ficheros de descripción de mundo (`.wbt`) y archivos del proyecto
- **Deberá incluir al menos** un fichero con extensión `.wbt`
- Puede incluir un directorio `textures\` con las texturas a utilizar

Ahora bien, normalmente son necesarios más directorios; estos son:

- `controllers/`: Fuentes para el control de robots.
- `libraries/`: Posibles bibliotecas externas en el proyecto.
- `plugins/`: Plugins para alterar el comportamiento típico de la simulación
- `protos/`: Prototipos disponibles para todos los ficheros del proyecto.

---

# Ficheros asociados a un mundo

Cada mundo (e.g. `world.wbt`) lleva asociados los siguientes ficheros ocultos:

- `.world.wbproj`: Información sobre la UI del usuario (e.g. perspectiva).
- `.world.jpg`: Imagen de carga de 768x432 en simulaciones o animaciones.

Si no existen o se eliminan, se crean al guardar correctamente el mundo.

---

# El directorio `controllers/`

Contiene un **directorio por cada posible controlador** de la simulación:

- El `.wbt` contiene el nombre del controlador a iniciarse para cada robot.
- Ese nombre hace referencia al **directorio del controlador**
- Es un campo independiente de plataforma y lenguaje (sólo es una cadena)

Cuando Webots intenta inicializar un controlador sigue el siguiente proceso:

1. Busca en `controllers/` un directorio que coincida con el nombre indicado
1. Busca en el subdirectorio un fichero que coincida con el nombre indicado
1. Si hay varios, selecciona uno de ellos siguiendo el siguiente orden:
   ```bash
   [.exe] > .class > .jar > .bsg > .py > .m
   ```
1. Si no encuentra ninguno, lanzará un error y iniciará un controlador vacío

---

# A CLASIFICAR<!--_class: transition-->

---

# Controladores

Son programas que definen el comportamieto de un robot.

Se pueden escribir en los siguientes lenguajes de programación:

- C, C++ o Java: Necesitan ser compilados antes de usarse como controladores
- Python y MATLAB: Se ejecutan sin ser compilados (son interpretados)

https://cyberbotics.com/doc/guide/language-setup