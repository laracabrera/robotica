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
author          :
    - Alberto Díaz Álvarez <alberto.diaz@upm.es>
    - Raul Lara Cabrera <raul.lara@upm.es>
description     : Robot Operating System (ROS)
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
![bg left:33%](https://www.ros.org/imgs/humble.png)

<div class="title"><i>Robot Operating System</i> (ROS)</div>
<div class="subtitle">Robótica</div>
<div class="author">Alberto Díaz y Raúl Lara</div>
<div class="date">Curso 2022/2023</div>
<div class="organization">Departamento de Sistemas Informáticos</div>

[![height:30](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-informational.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

---
# ¿Qué es <i>Robot Operating System</i> (ROS)?

Pues, aunque se denomine <i>Robot Operating System</i>:
- Ni es un sistema operativo, ni es exclusivo para robots

Es un **framework** y un **middleware** para desarrollar aplicaciones distribuidas
- **Framework**: Establece las prácticas y conceptos con los que trabajar
- **Middleware**: Sirve de intermediario de comunicación entre componentes
- Es <i>Open Software</i>, licenciado bajo la [BSD 3-Clause](https://choosealicense.com/licenses/bsd-3-clause/)

Incluye además un sistema de gestión de paquetes para desarrollar y desplegar software con facilidad
- En C++ y Python

---

# ¿Para qué? Podemos programarlos desde cero

Claro que sí, pero una vez tenemos el hardware:

- Hay que desarrollar drivers para cada uno de los sensores y actuadores
- Hay que desarrollar el framework de comunicaciones
  - Que soporte, además los diferentes protocolos de diferentes hardwares

- Escribir también el código asociado a la percepción
- Si es móvil, también los algoritmos de navegación y path planning
- Ojo, no olvidemos tampoco el mecanismo para sacar los <i>logs</i>
- Ah, y la gestión de errores

---

# Ya entiendo, <i>no reinventar la rueda</i>

Exacto; tradicionalmente el desarrollo de un robot era una tarea muy tediosa
- En esencia se construían desde cero prácticamente todos sus componentes

Con ROS se intenta minimizar ese efecto de reinventar la rueda; para ello:
- Se incluyen múltiples librerías de componentes de uso típico
- Se ofrece una infraestructura de comunicación <i>language agnostic</i>
  - ¡Incluso entre componentes de una misma aplicación!

---

# Versiones

En la actualidad coexisten dos versiones independientes en desarrollo
1. ROS, la versión original
   - Bastante extendida, aunque en desuso

1. ROS2, la sucesora
   - Soporte desde 0 para Python 3.X
   - Nuevas funcionalidades y mejoras en la funcionalidades existentes

¿Cuál debemos usar?
- ROS2 siempre que sea posible
- Cuando no, intentar migrar la aplicación existente a ROS2, y entonces ROS2

---

<!--
   _class: transition
-->

# Instalación de ROS2

---

# ¿Qué distribución elegir?

La lista se encuentra en [https://index.ros.org/doc/ros2/Releases/](https://index.ros.org/doc/ros2/Releases/)
- Órden alfabético $\equiv$ órden cronológico
- Para elegir (si el proyecto no depende de una versión en concreto):
  - Comprobar la <i>End of Life</i> (EOL)
  - Comprobar si es <i>Long Term Support</i>
  - Comprobar el sistema operativo sobre el que funciona

Nosotros usaremos **Humble Hawksbill** sobre **Ubuntu GNU/Linux 22.04**
- _Una máquina virtual sería una buena tarea opcional..._

<!--
---

PONER UN VÍDEO DE LA INSTALACIÓN SI DA TIEMPO

---
-->

---

# Nodos y la CLI

---

# Antes de nada

Las aplicaciones en ROS se componen de nodos principalmente
- Se puede pensar en ellos como **procesos independientes**
- Se agrupan en **paquetes**

¿Paquetes?
- **Componentes** de nuestro programa; incluyen los fuentes de este
- Se encuentran en el directorio de instalación de ROS o en nuestro <i>workspace</i>


¿<i>Workspace</i>?
- Espacio de trabajo (**directorio**) con las aplicaciones a ejecutar

---

# Creación de un espacio de trabajo

El desarrollo suele ser un proceso tedioso, porque implica muchas tareas:
- Crear y gestionar paquetes
- Gestionar las dependencias de componentes
- Compilar paquetes
- Desplegar

Ójala existiese una herramienta para gestionar los espacios de trabajo

---

# `colcon`

Herramienta para la gestión de los espacios de trabajo
- Está creada específicamente para ROS2
- Pero no viene instalada por defecto

Instalación (como superusuario)

```bash
$ apt install python3-colcon-common-extensions
```

Para habilitar el autocompletado (recomendable añadir al `~/.bashrc`)

```bash
$ source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash
```

---

# Ahora sí, creación de un espacio de trabajo

Los pasos a realizar son los siguientes:

1. Creamos un directorio para nuestro <i>workspace</i> (e.g. bajo `$HOME/ros_ws`):
1. Accedemos al espacio de trabajo y creamos un nuevo directorio llamado `src`:
   - Aquí se almacenará todo el código fuente de nuestros componentes
1. Creamos nuestro espacio de trabajo, usando la herramienta `colcon`
   ```bash
   $ colcon build
   ```
   - Creará directorios `install/` y `logs/` si no existen
   - También los ficheros de configuración de <i>workspace</i> si no existen
   - Construirá todos los componentes (paquetes) de nuestra aplicación
1. Cargamos `setup.bash` del directorio `install/`, creado tras `build`:
   - Suele ser útil añadirlo al `~/.bashrc`

---

# Creación de un paquete

Los pasos a realizar son los siguientes

1. Vamos al directorio `src/` de nuestro <i>workspace</i>
1. Ejecutamos el comando para la creación de paquetes
   ```bash
   $ ros2 pkg create super_pkg --build-type ament_python --dependencies rclpy
   ```
   - Esto creará un paquete llamado `super_pkg`...
   - ... usando el sistema <i>ament</i> para la creación de paquetes ...
   - ... de tipo `python`
   - ... dependiente de la librería `rclpy`

`rclpy` es la librería base de ROS y la usaremos prácticamente siempre

---

# ¿Y qué es un nodo?

Son el componente principal de nuestras aplicaciones
- Un único nodo debería tener (idealmente) un único propósito
- Se comunican entre sí a través de la infraestructura de mensajería de ROS

<center>

![w:720 center](../img/t2/nodes-and-packages.png)
<center>

---

# Fuentes de un nodo básico en Python

```python
#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

def main(args=None):
    try:
        rclpy.init(args=args)
        node = Node('py_test')
        node.get_logger().info('Hello, 🤖!')
        rclpy.spin(node)
    finally:
        rclpy.shutdown()

if __name__ == '__main__':
    main()
```

---

# Configuración de la instalación

Fichero `setup.cfg`

```python
[develop]
script-dir=$base/lib/NOMBRE_DEL_PAQUETE
[install]
install-scripts=$base/lib/NOMBRE_DEL_PAQUETE
```

Fichero `setup.py`

```python
from setuptools import setup
#...
setup(
    # ...
    entry_points={'console_scripts': ["exec_name = PAQUETE.NODO:main"],},
)
```

---

# Plantilla de un nodo como clase

```python
#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

class MyNode(Node):
    def __init__():
        super().__init__('py_test')
        self.get_logger().info('Initializing py_test')

def main(args=None):
    try:
        rclpy.init(args=args)
        node = MyNode()
        rclpy.spin(node)
    finally:
        rclpy.shutdown()

if __name__ == '__main__':
    main()
```

---

# Un nodo que hace algo (pero poco)

```python
#!/usr/bin/env python3

import rclpy
from rclpy.node import Node

class MyNode(Node):

    def __init__(self):
        super().__init__("py_test")
        self.i = 0
        self.create_timer(0.5, self.timer_callback)

    def timer_callback(self):
        self.i += 1
        self.get_logger().info("Hello, world! {self.i}")

def main(args=None):
    try:
        rclpy.init(args=args)
        node = MyNode()
        rclpy.spin(node)
    finally:
        rclpy.shutdown()

if __name__ == '__main__':
    main()
```

---

# Recapitulando

Hemos visto qué son espacios de trabajo, paquetes y nodos
- Sabemos crear el espacio de trabajo de nuestro robot (`colcon`)
- Sabemos construir paquetes que contendrán el software de nuestra aplicación

Los nodos son subprogramas existentes dentro de nuestra aplicación
- Cada uno es **responsable de una y solo una funcionalidad**
- Se comunican a través de <i>topics</i>, <i>servicios</i> y <i>parámetros</i> (para que haga poso)

Los nombres del fuente, el instalado y el nodo no tienen por qué coincidir
- Sí, hemos aprendido también a instalar los paquetes
- Y a lanzarlos
   ```bash
   $ ros2 run <paquete> <executable>
   ```

---

<!--

Un recorrido de las herramientas de la CLI estaría guay

Decimos un recap diciendo que ya sabeos escribir un nodo, ya sabemos ejecutarlo a pelo, sabemos instalarlo y ejecutarlo a través de ros2 run. Vamos a experimentar un poco con las herramientas de la línea de comando que nos vendrán bien, sobre todo, para saber el estado de nuestra aplicación en cada momento

ros2 tab tab vemos todos los comandos. Y de hecho ya hemos usado run y pkg. Vamos a ver otros.

ros2 run espera que le indiquemos un paquete y un nodo perteneciente a ese paquete. Esto quiere decir que podemos lanzar cualquier ejecutable que exista dentro del directorio global de ros y del directorio de instalación de nuestro workspace (gracias a que los hemos añadido al PATH al hacer el source en nuestro .bashrc).
    
Cuando hacemos un ros2 run demo_nodes_cpp talker, lo que estamos haciendo es ejecutar el ejecutable talker del paquete demo_nodes_cpp que hay en el directorio global de la instalación de ROS.
    
Por supuesto, también podemos ejecutar ros2 run tab tab y ver todos los paquetes accesibles desde nuestra posición.
    
con ros2 run -h vemos la ayuda, como la convención para todo ejecutable de ros.
    
EXPLICAR QUÉ PASA CUANDO NO ESTÁN HECHO LOS SOURCE (COMENTARLOS Y ABRIR UNA NUEVA TERMINAL).
    
Abrimos cuatro terminales. En la TL ros2 run my_py_pkg py_node y que se quede corriendo.
    
En la TR podemos ejecutar ros2 node tab tab y vemos que tenemos dos opciones, info y list.
    
list nos muestra todos aquellos nodos que están funcionando en un momento dado. (vemos que se está ejecutando el nuestro. Si lo matamos y ejecutamos list, se ve que nos muestra nada.

Lanzamos el nodo otra vez y con info, ponemos el nombre del nodo y nos da información de dicho nodo (subscribers, publishers, etcétera).
    
Según esto, tenemos dos publishers y 6 service servers en nuestro nodo. No los hemos creado explícitamente, son elementos que se crean automáticamente para cada nodo. Concretamente hay uno denominado /rosout. Aunque veremos luego concretamente los publishers, esto lo que hace básicamente es lanzar todas las líneas de log por ese punto.
    
También veremos más adelante los parámetros, y con ello entenderemos la gestión de parámetros que se puede hacer sobre el nodo a través de estos servicios.
    
ros2 node -h nos dará la ayuda para este comando.
    
Si matamos el nodo y necesitamos extraer información de un nodo que no existe, nos dará error. ¿Por qué? porque al matarlo ya no existe en el grafo de nodos.

Puede ocurrir que queramos lanzar un mismo nodo varias veces, pero claro, lanzarlo da error (probarlo. Se verá que no falla, pero nos advierte que esto es terrible).Si hacemos un info también nos adbvierte. además, ¿de cuál nos estaría dando información?
    
Esto es porque se llaman igual, y en el grafo de ejecutables sólo puede existir el mismo elemento una única vez, y dicho elemento viene identificado por su nombre.
    
Para poder ejecutar un mismo nodo varias veces, tenemos que darle un nombre alternativo (y parámetros, que sería lo lógico). Por ejemplo, si estamos gestionando un vehículo y tenemos un nodo que se encarga del registro de la odometría de una rueda, podemos querer crear cuatro nodos, uno para cada rueda, apuntando cada uno de estos a la dirección en el Bus CAN de cada rueda. Son cuatro instancias del mismo nodo corriendo con una configuración diferente.
    
Se puede renombrar cuando lo ejecutamos a través de ros2 run my_py_pkg py_node --ros-args --remap __node:=abc
    
Dar un poco de vueltas explicando esto que se puede inicializar con lo que queramos y renombrarlo. Y luego ejecutarlos con diferentes nombres y ver que no nos da ningún warning
    
Todos los argumentos de ros se añaden después de --ros-args
    
--remap es lo mismo que -r

Lanzarlos en las diferentes terminales salvo en la última y ahí vamos haciendo los list y los info
    
Esta funcionalidad será muy útil cuando queramos replicar comportamientos. Es más, más adelante veremos que podemos renombrar (remapear) prácticamente todo (topics, services) obteniendo nodos completamente únicos a partir del mismo código.

Recordatorio: para que funcione el autocompletion con colcon, hay que tener el source en el .bashrc.
    
colcon build: Para construir el workspace. Esto construye todos los packages que hay dentro del directorio src
colcon build --packages-select paquetes: Para especificar los paquetes a construir. Ver el tabtab

(Corremos nuestro nodo) Si modificamos algo y arrancamos de nuevo, no se ven los cambios. Si hago un build de mis paquetes, se ve que se ven los cambios. Por tanto, cada vez que modifiquemos los fuentes, tenemos que reconstruir.
    
Pero si usamos --symlink no es necesario
    
colcon build --packages-select my-ww  py-pkg --symlink-install
    
Esto lo que hace es que en lugar de lanzar el ejecutable cuando hacemos un ros2 run, lo que ha hecho es crear un link entre los ficheros (enseñarlo y luego enseñar cómo se ha creado el enlace simbólico) por lo que en tiempo de desarrollo puede ser muy útil. Esto funciona sólo en lenguajes interpretados (python), porque en los demás (e.g. C++) un enlace simbólico al fuente no vale, es necesario compilar éstos a un ejecutabvle, que es el que se copia.
    
Ahora, es súperimportante que dicho fichero sea eejcutable, porque es un enlace simbólico, y por defecto los ficheros se crean de lectura-escritura (enseñarlo).

Rqt y rqt-graph


-->

---

<!--
   _class: transition
-->

# Topics y mensajes

---

<!--
   _class: transition
-->

# Servicios

---

<!--
   _class: transition
-->

# Launchers

---

<!--
   _class: transition
-->

# Parametros

---
<!--
   _class: transition
-->

# ¡GRACIAS!
