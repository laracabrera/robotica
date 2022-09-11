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
  
# Contenidos
 
<div class="columns">
<div>
 
<!-- _class: cool-list -->

1. *whatever*
2. *Hannover*
3. *Freiburg im Breisgau*
4. *Heidelberg*
5. *Hamburg*
 
</div> 
<div>  

4. *Leipzig*
5. *Dresden*
6. *München*
7. *Köln*
8. *Köningsberg und Praga*

</div>
</div>   

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
  - ¡Incluso diferentes lenguajes dentro de una misma aplicación!

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

# ¿Y qué vamos a ver?

Veremos tanto el funcionamiento básico como las funcionalidades del core
- Consideramos que es suficiente para desarrollar nuestras primeras aplicaciones
- Veremos algunas librerías externas (pero no todas, que sería una locura)

Cada vez que os enfrentéis a nuevas aplicaciones afianzaréis estos conocimientos
- Y obtendréis nuevos que os harán más eficientes en los siguientes desarrollos

Si consideráis que falta, sobra, o que se podría mejorar algo...
- *... igual estaría bien proponer algún que otro <i>pull-request</i>...*

---

<!--
   _class: transition
-->

# Instalación de ROS2

---

# ¿Qué distribución elegir?

La lista se encuentra en [https://index.ros.org/doc/ros2/Releases/](https://index.ros.org/doc/ros2/Releases/)
- Órden alfabético $\equiv$ órden cronológico (<i>Dashing</i>, <i>Eloquent</i>, <i>Foxy</i>, etcétera)
- Para elegir (si el proyecto no depende de una versión en concreto):
  - Comprobar la <i>End of Life</i> (EOL)
  - Comprobar si es <i>Long Term Support</i>
  - Comprobar el sistema operativo sobre el que funciona
  - **Recomendación**: Usar la última LTS sobre GNU/Linux

Nosotros instalaremos **Humble Hawksbill** sobre **Ubuntu GNU/Linux 22.04**
- Proceso de instalación: [https://docs.ros.org/en/humble/Installation.html]()

<!--
PONER UN VÍDEO DE LA INSTALACIÓN SI DA TIEMPO
-->
---

# Hola mundo

De esta manera comprobamos que todo funciona

1. Abrimos dos terminales independientes
1. En la primera escribimos lo siguiente:
   ```bash
   $ ros2 run demo_nodes_cpp talker
   ```

1. En la segunda escribimos lo siguiente:
   ```bash
   $ ros2 run demo_nodes_cpp listener
   ```

Si en ambos se ven los mismos mensajes, nuestra instalación es correcta

---

# Breve nota sobre la <i>Command Line Interface</i> (CLI)

La CLI permite ejecutar instrucciones de un programa o sistema operativo
- Tras la instalación de ROS tenemos acceso al comando `ros2`
- `ros2` y pulsar dos veces `<TAB>` no dará la lista de todas las instrucciones

`ros2 run` espera que le indiquemos un paquete y uno de sus nodos
- Esto quiere decir que podemos lanzar cualquier ejecutable de ros

También podemos ejecutar `ros2 run` y pulsar dos veces `<TAB>`
- Así veremos todos los paquetes accesibles desde nuestra posición.

Con `-h` accederemos a la ayuda de cualquier comando de `ros2` (convenio)

---

<!--
   _class: transition
-->

# Nodos

---

# Sobre nodos, paquetes y <i>workspaces</i>

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

El espacio de trabajo es donde se escribe el código de nuestra aplicación y donde se compila

El desarrollo suele ser un proceso tedioso, porque implica muchas tareas:
- Crear y gestionar paquetes
- Gestionar las dependencias de componentes
- Compilar paquetes
- Desplegar

¡Ójala existiese una herramienta para gestionar los espacios de trabajo!

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

# Contenido de un paquete

La estructura de un paquete de tipo Python es la siguiente:
- Directorio `resource/` para incluir recursos necesarios que no son fuentes
  - Por ejemplo, archivos de configuración interna
- Directorio `test/`, con los fuentes para probar el paquete
- Fichero `package.xml`, que describe información del paquete como puede ser:
  - Metainformación relativa a nombre, versión, ...
  - Dependencias comunes y exclusivas para pruebas
  - Sistema de construcción (<i>build system</i>)
- Fichers `setup.py` y `setup.cfg` para la instalación del paquete

Con esto se puede compilar el paquete a través de `colcon build`

---

# ¿Y qué es un nodo?

Son el componente principal de nuestras aplicaciones
- Un único nodo debería tener (idealmente) un único propósito
- Se comunican entre sí a través de la infraestructura de mensajería de ROS

<center>

![](../img/t2/nodes-and-packages.png)
<center>

---

# Creación de un nodo

Los fuentes de los nodos se almacenan dentro del paquete
- En un directorio que se llama igual que este
- Ahí crearemos el fichero de código de nuestro nodo
- Ojo, ROS2 funciona solo con Python 3, no con Python 2 (por suerte)

Crearemos la estructura para la ejecución de este fuente:

```python
#!/usr/bin/env python3

def main(args=None):
   pass

   if __name__ == '__main__':
      main()
```
- El <i>shebang</i> (`#!`) es obligatorio, ya que el fichero `.py` será el ejecutable

---

Lo primero que tenemos que hacer en nuestro programa será inicializar el sistema de comunicación de ROS
- Y pasarle los argumentos, en caso de que los haya

```python
#!/usr/bin/env python3

import rclpy

def main(args=None):
   rclpy.init(args=args)
   # Nuestro código
   rclpy.shutdown()

   if __name__ == '__main__':
      main()
```
- Si nos acordamos, `rclpy` real la dependencia con la que creamos el paquete

---

`rclpy.init` es la primera instrucción en prácticamente cualquier aplicación
- Entre otros, arranca el sistema de comunicación de ROS
- La aplicación fallará si intentamos usar cualquier característica antes

`rclpy.shutdown` debe ser la última línea de nuestra aplicación
- Cerrará la infraestructura de comunicación

Hasta ahora no hemos creado ningún nodo
- Esto es únicamente la preparación del entorno en el que se ejecutará

---

Ahora crearemos un nodo en la funciḉon `main` de nuestro `script`

```python
...
from rclpy.node import Node
...
   rclpy.init(args=args)
   node = Node('Sensor')
   rclpy.shutdown()
...
```

`Sensor` será el nombre de nuestro nodo
- Por convención no se usa la palabra <i>node</i> porque sería redundante

Ahora podemos ejecutar nuestro nodo de la siguiente manera:

```bash
\$ chmod u+x my_first_node.py
\$ ./my_first_node.py
```

---

En este punto hemos creado un nodo; concretamente
1. Nos conectamos a la infraestructura de ROS, creándola si no existía
2. Creamos un nodo y lo arrancamos
3. Nos desconectamos de la infraestructura y cerramos la aplicación

De acuerdo, de utilidad nos ha quedado un poco regular, pero quedémonos con tres conceptos:
1. **El nodo NO es el fichero** de Python, sino que se crea dentro de este
1. **El nombre del nodo NO es el nombre del fichero**, sino que es el nombre del objeto cuando lo creamos

Ahora, hagamos algo más visible

---

Sacaremos por pantalla un mensaje de <i>log</i>
- Para ello usaremos el logger asociado al nodo


```python
...
   node = Node('Sensor')
   node.get_logger().info('Hello, world!')
   rclpy.spin(node)
...
```

`rclpy.spin` es un método extremadamente importante
- Se usará en prácticamente todos los fuentes desarrollados en ROS
- Su cometido es pausar el programa y dejar el nodo en modo escucha
- Los <i>callbacks</i> asociados a los mensajes se llamarán desde este método

Si queremos parar el proceso basta con ejecutar `CTRL+C`

---

# Estructura básica de un nodo en Python

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

# Instalación del nodo

La ejecución que hemos hecho el nodo ha sido un poco trampa
- En realidad hemos ejecutado el fichero fuente, no el nodo desplegado

Podríamos trabajar así, pero es poco escalable
- Al no estar instalados en el workspace, no están dentro del `PATH`
- Por ello, queremos instalar y desplegar los nodos


Al estar usando Python, nos evitaremos un paso (transparente para nosotros)
- En C++ los fuentes hay que compilarlos, en Python no
- Únicamente se copiarán los fuentes de un lado a otro

---

Instalaremos nuestro paquete usando dos ficheros de configuración:
- Fichero `setup.cfg`: Información de dónde se instalarán nuestros fuentes
   ```python
   [develop]
   script-dir=$base/lib/NOMBRE_DEL_PAQUETE
   [install]
   install-scripts=$base/lib/NOMBRE_DEL_PAQUETE
   ```
- Fichero `setup.py`: Metainformación de nuestros fuentes
   ```python
   from setuptools import setup
   #...
   setup(
      # ...
      entry_points={'console_scripts': ["exec_name = PAQUETE.NODO:main"],},
   )
   ```
   <!-- En entry_points->'console_scripts' hay que indicar cuáles son los nodos que instalamos, con una línea donde se especifica el ejecutable. Lo que hará es coger ese fichero .py, copiarlo, realizar una serie de modificaciones, entre las que se incluye hacerlo ejecutable (como hemos hecho nosotros) e instalarlo en el directorio install de nuestro workspace -->

El comando `colcon build` realizará la instalación de los fuentes

<!-- Necesitamos especificar un nombre para nuestro ejecutable: "py_node = my_py_pkg.my_first_node:main" -->

---

Tras la ejecución de `colcon build`, nuestros nodos:
- Se habrán compilado (sólo en el caso de C++)
- Se habrán desplegado en el directorio indicado en `setup.cfg`
- Se habrán marcado como ejecutables

Ya podemos ejecutar nuestro nodo como cualquier otro nodo de ROS:

```bash
$ ros2 run nombrepaquete nombrenodo
```
- Esto es así porque hemos añadido nuestro <i>workspace</i> al `PATH` de ROS

---

# (BONUS TRACK) Plantilla de un nodo como clase

```python
#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class MyNode(Node):
    def __init__(self):
        super().__init__('py_test')
        self.i = 0
        self.create_timer(0.5, self.timer_callback)

    def timer_callback(self):
        self.i += 1
        self.get_logger().info('🤖 #{self.i}')

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

Los nombres del fuente, el instalado y el nodo no tienen por qué coincidir
- Sabemos instalar los paquetes, y lanzarlos con
   ```bash
   $ ros2 run <paquete> <executable>
   ```

---

<!--
   _class: transition
-->

# <i>Topics</i> y mensajes

---

# Topic

Es un bus de datos para el intercambio de datos entre nodos
- Está caracterizado por un **nombre único** y un **tipo de mensaje**
- Provee de un mecanismo de **comunicación unidireccional**
- Los datos que se intercambian se denominan **mensajes**

La **comunicación** es, en principio, **anónima**
- Quien envía el mensaje no sabe quién lo quiere recibir y viceversa
  - **<i>Publisher</i>**: Publica un mensaje en el bus
  - **<i>Subscriber</i>**: Recibe un mensaje del bus

<i>Publisher</i> y <i>subscriber</i> de un **mismo topic** deben compartir el **mismo tipo de mensaje**

---

# Enviando mensajes

El envío de mensajes es tipo <i>broadcast</i>: sé qué envío, pero no quién escucha

Para crear un bus usaremos el método `create_publisher` de `Node`:
```python
publisher = <nodo>.create_publisher(<mensaje>, <publisher>, <buffer>)
```
- No hemos visto tipos de mensajes, así que usaremos uno ya existente:
   ```bash
   ros2 interface show example_interfaces/msg/String
   ```
  - `ros2 interface` ayuda a encontrar los interfaces (tipos de mensajes)
  - Usaremos el mensaje `String` del paquete `example_interfaces`
  - Más adelante aprenderemos cómo crear nuestros propios mensajes
- Ojo: si el <i>buffer</i> se llena, los mensajes se dejan de enviar y se descartan

---

Los mensajes se importan en nuestro código como cualquier módulo:
```python
from example_interfaces.msg import String
```
 - Al ser de un paquete, tenemos que especificar la dependencia (`package.xml`)
   ```xml
   <depend>example_interfaces</depend>
   ```

Tras la importación ya se puede usar en nuestro código, creando el publisher:
```python
self.publisher = self.create_publisher(String, 'emisora', 10)
```
Y enviando mensajes
```python
msg = String()
msg.data = 'Hola 🤖!'
self.publisher.publish(msg)
```

---


# Ejemplo de <i>publisher</i>

```python
#!/usr/bin/env python3

...
from example_interfaces.msg import String


class RadioStationNode(Node):

    def __init__(self):
        super().__init__("station")

        self.publisher = self.create_publisher(String, "radio_station", 10)
        self.timer = self.create_timer(0.5, self.publish)
        self.get_logger().info("Radio station launch!")

    def publish_news(self):
        msg = String()
        msg.data = ‘Hi there! There are no new news’
        self.publisher.publish(msg)

...
```

---

# Breve nota sobre la CLI

Si ejecutamos este nodo, podemos ver los topics que hay ejecutando:

```bash
$ ros2 topic list
```
- Nos permite ver **TODOS** los topics que están funcionando en este mismo momento

Si queremos ver el contenido que se está publicando en un topic concreto:

```
$ ros2 topic echo /emisora
```

---

# Recibiendo mensajes

Para recibir mensajes publicados en un <i>topic</i> decimos que nos **suscribimos**

Un <i>subscriber</i> se crea de forma muy parecida a un <i>publisher</i>:

```python
subscriber = <nodo>.create_subscription(<mensaje>, <publisher>, <callback>, <buffer>)
```
- `callback` será el nombre de la función que se ejecutará al recibir un mensaje

---

# Ejemplo de <i>subscriber</i>

```python
#!/usr/bin/env python3

...
from example_interfaces.msg import String


class SmartphoneNode(Node):
    def __init__(self):
        super().__init__("smartphone")
        self.subscriber = self.create_subscription(
            String, "radio_station", self.callback, 10
        )
        self.get_logger().info("Smartphone is listening!")

    def callback(self, msg):
        self.get_logger().info(msg.data)
...
```

---

# Topics y la línea de comandos (I)

Algunos comandos muy útiles relacionados con topis de la CLI son:
- Listado de todos los topics que se están usando
  ```bash
  $ ros2 topic list
  ```
- Información concreta del topic
  ```bash
  $ ros2 topic info <topic>
  ```
- Saca por pantalla la información que se está publicando en el topic
  ```bash
  $ ros2 topic echo <topic>
  ```
- Estima la frecuencia a la que se publica la información en el topic
  ```bash
  $ ros2 topic hz <topic>
  ```
---

# Topics y la línea de comandos (y II)

- Calcula el ancho de banda usado por los mensajes del topic
  ```bash
  $ ros2 topic bw <topic>
  ```
- Publica el mensaje en el topic
  ```bash
  $ ros2 topic pub <topic> <tipo> {json_data}
  ```
- Renombra el topic
  ```bash
  $ ros2 run power_pkg news_station \
           --ros-args -r <old_topic>:=<new_topic>
  ```

<!--
Hasta ahora hemos visto las herramientas de línea de comandos de ros ros2 pkg (para crear paquetes) y ros2 run (para ejecutarlos). También hemos visto colcon, que no es directamente de ros pero es la herramienta de facto para crear y gestionar los workspaces. Por último, hemos visto ros2 topic hace poco para ver los topics que existían y leer los mensajes que se publican en estos. Vamos a ver un poquitín más de detalle.

ros2 topic tabtab

Vamos a arrancar nuestro nodo.

Ros2 list

Nos enseña los topics que se están usando. Si nos cargamos el nodo, desaparece. Lo arrancamos de nuevo

Ros2 ropic info /robot_news

Éste es súperútil. Con él podemos ver el tipo de mensaje que se está usando en el topic, cuántos publishers están enviaándo información y cuántos subscribers están suscritos a éstos.

Ros2 topic echo /robot_news

Vemos que estamos recibiendo mensajes. Si lanzamos de nuevo ros2 topic info /robot_news, vemos que tenemos un nuevo suscriptor, Lo paramos, y otra vez 0.

Ros2 interface show example_interfaces/msg/String

Como ya hemos visto antes, nos da información de la estructura del mensaje en cuestión.

ros2 topic  hz /robot_news

hz nos da la frecuencia de publicación de un topic (estimada)

Ros2 topic bw /robot_news

Bw (bandwidth) nos dice cuánto ancho de banda está ocupando el stream de datos de un topic

Finalmente, podemos publicar mensajes en un topic  a través de la terminal:

Ros2 topic pub -r 10 /robot_news example_interfaces/msg/String {data: ‘Hello, world! I’m the terminal!’}

Volvemos a lanzar el info y vemos que tenemos dos publishers y un echo.

Como recordatorio del tema anterior, si ejecutamos:

Ros2 node list

Vemos el nodo que hemos creado funcionando. Si ejecutamos

ros2 node info /robot_news_station

Veremos toda la información, incluido todo lo que publica. Concretamente estamos publicando un topic nuevo diferente al de defecto que es el que hemos creado.

RENOMBRANDO UN TOPIC

Igual que vimos en la sección anterior que podíamos renombrar un nodo:

Ros2 run my_py_pkg robot_news_station --ros-args -r __node:=my_station

Ahora el nodo está corriendo como my_station. Hacemos el list vemos que está funcionando, y si vemos la lista de topics vemos que está publiacndo nuestro topic, con el nombre que le dimos previamente. Para renombrar el topic:

Ros2 run my_py_pkg robot_news_station --ros-args -r __node:=my_station -r robot_news:=my_news

Hacemos un list y vemos que ha sido renombrado. Si arrancamos el nodo con el subscriber, tiene sentido que ahora no recibamos nada, porque está publicando en otro lado. Si hacemos otro list vemos que sí aparece robot-news, pero porque el subscriber está escuchando ahí. Pero son topics diferentes. Para escuchar del topic renombrado (remapping) es similar al parámetro de antes:

Ros2 run my_py_pkg smartphone --ros-args -r robot_news:=my_news
-->

---

# Mensajes personalizados

Un topic se caracteriza por un **nombre** (e.g. `/name`) y una **interfaz** (e.g. `iface/msg/String`)
- El tipo de mensaje se describe con una sintáxis propia de ROS
- Durante la compilación del <i>workspace</i> (`colcon`) cada mensaje se <i>transpila</i>
- Con este proceso se generarán los fuentes específicos para cada lenguaje

<center>

![](../img/t2/transpiling.png)
<center>

---

# Estructura de una interfaz (`PointCloud2.msg`)

```
# This message holds a collection of N-dimensional points, which may
# ...
# such as stereo or time-of-flight.

# Time of sensor data acquisition, and the coordinate frame ID (for 3d points).
std_msgs/Header header

# 2D structure of the point cloud. If the cloud is unordered, height is
# 1 and width is the length of the point cloud.
uint32 height
uint32 width

# Describes the channels and their layout in the binary data blob.
PointField[] fields

bool    is_bigendian # Is this data bigendian?
uint32  point_step   # Length of a point in bytes
uint32  row_step     # Length of a row in bytes
uint8[] data         # Actual point data, size is (row_step*height)

bool is_dense        # True if there are no invalid points
```
<!--
En la página de ROS2 interfaces podemos encontrar todos los tipos de datos que podemos usar en las definiciones de mensajes.

Vemos que podemos usar tanto tipos simples (enteros, de coma flotante, lógicos, cadenas) así arrays de dichos tipos simples. Vemos también la correspondencia en otros lenguages.

Si vamos al paquete de interfaces de ejemplo (http://github.com/ros2/example_interfaces), dentro del directorio msg  (
Más adelante veremos el directorio srv, que son los mensajes para servicios) podemos ver un montón de ficheros que se corresponden con los tipos de mensaje que tenemos disponibles a través de este paquete.

Si entramos, por ejemplo, en Int64.msg podemos ver la misma información que tenemos disponible cuando ejecutamos ros2 interfaces sobre un mensaje en concreto. La información que vemos es una interfaz donde sólo existe un dato, llamado “data” de tipo int64.

Existe un repo con paquetes que se usan mucho en aplicaciones reales: common_interfaces. Si vamos al repo (http://github.com/ros2/common_interfaces) veremos que aquí hay paquetes más específicos (tanto para mensajes como para servicios). Éstos se instalan por defecto al realizar la instalación de ros desktop, pero en caso de que falte alguno, por ejemplo geometry, basta con instalarlo con un apt install.

Vamos por ejemplo a sensor_msgs. Si entramos a msg, vemos un montón de definiciones de mensajes (vamos a un mensaje (que tenga header), decimos que es muy útil para algo de construcción y lo describimos). El header que vemos aquí no es un tipo básico, sino que viene de otro package (std_msgs). La forma es nombredepaquete/nombredelmensaje, y sirve para agrupar partes comunes de mensajes (por ejemplo, en este caso, la cabecera de un mensaje).

Un convenio que se sigue a rajatabla es que el tipo, si es básico, empieza en minúscula (int, string, …). Si es un tipo complejo, empieza con mayúscula (e.g. Header).

Enseñar también el mensaje de PointCloud2.

Por tanto, para crear mensajes podemos usar:
Tipos primitivos
Otros mensajes del mismo u otros paquetes
-->

---

# Creación de un mensaje personalizado

<!--
Vamos a crear un mensaje personalizado. Primero, ¿dónde debemos crearlo? Técnicamente, podemos hacerlo en cualquier paquete, pero lo más común suele ser crear paquetes específicos para la definición de mensajes. De esta manera se evita que los paquetes que usan esos mensajes como publishers o como suscribers no dependan de los paquetes que los usan como subscribers o publishers respectivamente. Vamos, que nos evitamos un dependency mess en el fuuturo

Creamos un paquete

Ros2 pkg create my_robot_interfaces

Usar interfaces al final es un convenio que se suele usar. Otro es “msg”. Como no hemos especificado un tipo de paquete, nos lo crea por defecto de C++, pero ya que no va a tener fuentes, sólo mensajes, la verdad es que nos da un poco ifgual.

Vamos dentro 

Cd my_robot_interfaces

Borramos el directorio de fuentes

Rm -rf include src

Y nos creamos un directorio msg

Mkdir msg

Ahora, antes de crear nuestro mensaje, tenemos que hacer un poco de configuración, es decir, tocar los ficheros CMakeLists.txt y package.xml. Si vamos a package.xml, añadimos (entre buildtool y test_depend):

<build_depend>rosidl_default_generators</build_depend>
<exec_depend>rosidl_default_runtime<exec_depend>
<member_of_group>rosidl_interface_packages</member_of_group>

Esta es la funcionalidad necesaria para transpilar las interfaces del paquete y que se puedan exportar al resto. Una vez hemos hecho esto, no necesitamos cambiar nada más en el package.xml.

En el CMake… nos zumbamos el default c99 y el if build_testing y añadimos (reemplazando donde ponde uncomment blablabla

find_package(rosidl_default_generators REQUIRED)

Y ya podemos creatr nuestro mensaje personalizado. Vamos a msg y creamos el fichero

Cd msg
Touch HardwareStatus.msg

Para los nombres de los mensajes es importante comenzarlos en mayúscula, con CamelCase y sin Msg.

Rellenamos el fichero con:

Int64 temperature
Bool ready
String debug

Vamos a CMakeList.txt y ponemos debajo del findpackage

rosidl_generate_interfaces(${PROJECT_NAME}
  “msg/HardwareStatus.msg”
)

Construimos el workspace

Colcon build --packages-select my_robot_interfaces

Vamos a ver exactamente d´onde se ha instalado.

Vamos a install/my_robot_interfaces
Cd lib/python3.8/site-packages/my_robot_interfaces/msg

Entramos en el _hardware_status.py y enseñamos donde están los tres campos y poco más.

Si vamos a ros2 interface show my_robot_interfaces/msg/HardwareStatus vemos la estructura del mensaje que está instalado
-->

---

# Pasos para la creación de una interfaz

Dentro del paquete donde queramos definir la interfaz:

1. Si no existe, creamos directorio `msg/` y creamos la interfaz (debe ser `.msg`)
1. Añadimos (si no existen) las dependencias del transpilador a `package.xml:`
   ```
   <build_depend>rosidl_default_generators</build_depend>
   <exec_depend>rosidl_default_runtime<exec_depend>
   <member_of_group>rosidl_interface_packages</member_of_group>
   ```
2. Las añadimos también (si no existen ya) al fichero `CMakeList.txt`:
   ```
   find_package(rosidl_default_generators REQUIRED)
   ```
1. Añadimos el mensaje al transpilador
   ```
   rosidl_generate_interfaces(${PROJECT_NAME} "msg/<INTERFAZ>.msg")
   ```

---

# Usando un mensaje personalizado

<!--
En el package.xml tenemos que añadir la dependencia

<depend>my_robot_interfaces</depend>

Vamos a nuestro nodo anterior

From my_robot_interfaces.msg import HardwareStatus

Y en el publisher:

Msg = HardwareStatus()
Msg.temperature = 45
Msg.ready = True
Msg.debug = “Nai”
self.publisher.publish(msg)

Construimos y ejecutamos y vemos que funciona

Ros2 topic list
Ros2 topic info /hardware_status
Ros2 topic echo /hardware_status
-->

---
<!--
   _class: transition
-->

# Servicios
<!--
Existen dos mecanismos de comunicación en ros. Uno son los topics, que acabamos de ver. Ahora veremos el otro: los servicios.

Mientras que los topics están pensados desde un punto de vista asíncrono unidireccional (arquitectura publish/subscribe), los servicios están pensados para comunicación bidireccional (arquitectura cliente/servidor)

En esta sección:
Entenderemos qué son los servicios de ros
Escribiremos nuestro propio servicio
Usaremos herramientas de la terminal para debugear un poco
-->

---

# Servicio

Es un sistema de comunicación de arquitectura cliente/servidor
- Permiten la comunicación síncrona o asíncrona entre nodos
- Están pensados para la comunicación bidireccional entre nodos
  - Dos tipos de mensaje, uno para la <i>request</i> y otro para la <i>response</i>
- Un único servidor sólo puede existir una vez en una aplicación
  - Eso sí, puede ser accedido por múltiples clientes
---

# Creación de un servidor

<!--
Vamos a crear un servicio muy tonto que va a sumar dos enteros. En la request le vamos a enviar dos números a sumar y en la response vamos a recibir el número de la suma.

Un servicio está definido por dos cosas, el nombre y su tipo (la interfaz). Ya hemos visto interfaces para los topics, las de los servicios son un poquitín diferentes. Vamos a usar alguna ya existente. Para ello:

ros 2 interface show example_interfaces/srv/AddTwoInts

Primero, convenio: definiciones de servicios en directorio srv en lugar de msg.
Segundo, 2 bloques separados por tres guiones. Parte superior, interfaz del mensaje de request, parte inferior interfaz del mensaje de response.

Vamos a usar esa interfaz de servicio. Vamos a my_py_pkg/my_py_pkg y creamos el nodo.

Touch add_two_ints_server.py
Chmod u+x add_two_ints_server.py

Usamos la template y le cambiamos los nombres a AddTwoIntsServerNode y add_two_ints_server

Ahora vamos a añadir el servidor del servicio en el inicializador.

From example_interfaces.srv import AddTwoInts

Recordad que tenemos que añadir, si no lo tenemos ya, la dependencia en el package.xml. Seguimos:

self.server _ = self.create_service(AddTwoInts, ‘add_two_ints’, self.callback_add_two_ints).

Requiere tres argumentos, la interfaz de servicio, el nombre y la función de callback.

Un convenio que se sigue tanto para los servicios de ros como para servicios en general es comenzar su nombre por un verbo, ya que normalmente un servicio va a realizar una acción o un proceso.

Def callback_add_two_ints(self, request, response):

En este método recibiremos dos objetos, la request, que es el mensaje que nos ha enviado el cliente que quiere usar el servicio, y la response, que será el mensaje que rellenaremos para devolverle cuando terminemos de hacer lo que etngamos que hacer.

Def callback_add_two_ints(self, request, response):
  Response.sum = request.a + request.b
  self.get_logger().info(f‘{request.a} + {request.b} = {response.sum}’)
  Return response

Como podemos observar, el funcionamiento es muy parecido a cómo funcionan los mensajes en los topics.

Añadimos el nodo al setup.py

Add_two_ints_server = my_py_pkg.add_two_ints_server:main

Construimos el paquete

Colcon build --packages-select my_py_pkg --symlink-install

Y Ahora vamos a lanzar nuestro nodo

Ros2 run my_py_pkg add_two_ints_server

Aunque no tenemos un cliente, podemos testear el server directamente desde la terminal. Para ello, escribimos

Ros2 service list

Ahí vemos los servicios existentes.

Ros2 node info add_two_ints_server

Ahí podemos ver que adermás de los servicios existentes, se ha añadido este de aquí, con su nombre y su tipo

Con:

Ros2 service call /add_two_ints example_interfaces/srv/AddTwoInts “{a: 3, b: 4}”

Describimos lo que ha pasado en ambas terminales.
-->

---

# Ejemplo de servidor

```python
#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from example_interfaces.srv import AddTwoInts

class AddTwoIntsServerNode(Node):
    def __init__(self):
        super().__init__('add_two_ints_server')
        self.server = self.create_service(AddTwoInts, ‘add_two_ints’, self.callback_add_two_ints)
        self.get_logger().info('Add two ints server has been started.')

    def callback_add_two_ints(self, request, response):
        response.sum = request.a + request.b
        self.get_logger().info(f'{request.a} + {request.b} = {response.sum}'))

        return response
```

---

# Creación de un cliente

<!--
Creamos fichero y lo hacemos ejecutable

Touch add_two_ints_client.py
Chmod u+x

Client = self.create_client(AddTwoInts, ‘add_two_ints’)

En este punto, si hacemos ua request al servidor, y éste no está arrancado, fallará, así que vamos  a hacer una espera para que el nodo espere a que el servidor se arranque.

While not client.wait_for_service(1.0):
  node.get_logger().warn(‘Waiting for server…’)

Si no es especifica timeout, espera siempre

Vamos a lanzarlo, pero para ello hay que actualizar el setup.py

“Add_two_ints_client = my_py_pkg.add_two_ints_client:main”

Colcon builñd packages-select my_py_pkg --symlink-install
Ros2 run my_py_package add_two_ints_client

Estará esperando a que se arranque el servidor. Una vez arranquemos el servidor:

Ros2 run my_py_package add_two_ints_server

Nuestro cliente termina porque ha realizado la conexión. Bueno, nos vamos a crear un objeto request de nuestra interfaz:

Request = AddTwoInts.Request()
Request.a = 1
Request.b = 2

client.call()

Esta es una llamada bloqueante. Es muy raro usarla, pero bueno, está bien saber qué existe. Lo que hace es hasta que no hay respuesta, el cliente se queda esperando. Nosotros vamos a usar una llamada no bloqueante:

Future = client.call_async(request)

Un future, para el que no so sepa, es un objeto que tiene la respuesta a la llamada entre ahora y más adelante. Y ahora vamos a dejar funcionando el servicio hasta que se complete la llamada.

rclpy.spin_until_future_complete(node, future)

Una vez se ha acabado esto, sabemos que ha habido respuesta

try:
  Response = future.result()
  self.get_logger().info(a + b = sum)
Except Exception as e:
  node.get_logger().error(f‘Error: {e}’)

Lo lanzamos y probamos.

REESCRIBIR TODO ESTO PARA QUE SE ADAPTE A LO QUE TENEMOPS DE OOP
--->

---

# Ejemplo de cliente

```python
#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from functools import partial

from example_interfaces.srv import AddTwoInts

class AddTwoIntsClientNode(Node):
    def __init__(self):
        super().__init__('add_two_ints_client')
        self.call_add_two_ints_server(1, 2)

    def call_add_two_ints_server(self, a, b):
        client = self.create_client(
            AddTwoInts, 'add_two_ints'
        )
        while not client.wait_for_service(1.0):
            self.get_logger().warn(
                'Waiting for server'
            )
        request = AddTwoInts.Request()
        request.a = a
        request.b = b

        future = client.call_async(request)
        future.add_done_callback(partial(
            self.callback_call_add_two_ints,
            a=a, b=b
        ))

    def callback_call_add_two_ints(
        self, future, a, b
    ):
        try:
            response = future.result()
            self.get_logger().info(
                f'{a} + {b} = {response.sum}')
            )
        except Exception as e:
            self.get_logger().error(‘{e}')
```

---

# Tipos de servicio personalizados

<!--
Como ya sabemos crear tipos de mensaje personalizados, la verdad es que crear tipos de servicio personalizados no tiene mucho más misterio.

Dónde ponemos nuestro servicio? En el directorio srv (convenio)

Vamos a crear uno simple, por ejemplo

Touch ComputeRectangleArea.srv

Es importante que su extensión sea srv y no msg.

Rellenamos el servicio

float64 length
float64 width
---
float64 area

Para construir los servidores, no tenemos que hacer nada más que una cosa porque ya lo hicimos previamente para nuestro mensaje personalizado. Añadimos la lína en CMaketxt

(dentro de generate_interfaces)
“srv/ComputeRectangleArea.srv”

Y ya está; Construimos…

Colcon build --packages-select my_robot_interfaces

Y yas podemos trabajar con dicha definición de la misma forma que los mensajes personalizados

Ros2 interface show my_robot_interfaces/ tab tab

Ros2 interface show my_robot_interfaces/srv/ComputeRectangleArea
-->

---


<!--
   _class: transition
-->

# <i>Launchers</i>

<!--
Hemos visto nodos que publican mensajes en topics, otros que se suscriben a ellos, servicios, clientes y servidores. Teniendo en cuenta esto, y que las aplicaciones están compuestas de muchos de estos nodos, el arrancar una aplicación con todos sus componentes puede ser un desparrame. Imaginaos 20 nodos. ¡O 100!

En esta sección vamos a aprender aarrancar todos nuestros nodos y parámetros desde un fichero denominado launcher. Concretamente vamos a aprender:
Entenderlos y saber cuándo usarlos
Cómo crearlos, instalarlos y lanzaros

¿POR QUÉ UN LAUNCHER?

Es fácil saber por qué necesitamos un launcher. Pongamos que estamos desarrollando el software de control de un vehículo autónomo. Hemos desarrollado un nodo para la gestión de la cámara (de las cuales tenemos dos porque estamos usando visión estéreo). Tenemos también un nodo para gestionar el lidar (de los cuales tenemos cuatro). Claro, cada uno de ellos lleva su propia configuración. Luego tenemos los nodos encargados de gestionar este flujo de datos. Están también los nodos de los sensores infrarojos, GPS, Bus CAN, comunicaciones (que a su vez tiene un montón de nodos, pero es de un tercero). Por último tenemos el nodo para la fusión de sensores, el nodo de navegación y el nodo de control. Pensad en la cantidad de parámetros que requiere esta aplicación, que además queremos tener para varios vehículos (diferentes, por supuesto, por lo que ahbrá que modificar las configfuarciones de muchos de estos nodos).

Luego está el tema de las comunicaciones y el remapeo de los topics y servicios, porque el mismo nodo en diferentes instancias tienen que tener diferentes nombres.

No tiene mucho sentido crear lanzar desde la terminal todos estos nodos. Ni siquiera tiene mucho sentido configurarlo con un script bash, porque lo mismo el intérprete de uno de los ordenadores a bordo es bash, el otro sh, el otro vete tú a saber qué…

Para ello existen los launcher. Un fichero launcher permite el arranque de todo desde un fichero de configuración. 

-->
---

# Creación de un <i>launcher</i>

<!--
Vamos a crear un launchfile para nuestra aplicación publish/subscribe, es decir, lanzará dos nodos diferentes.

Nos creamos un paquete para nuestros launchers

Ros2 pkg create my_robot_bringup

Suele ser lo normal el meter los launchers de nuestra aplicación en un único paquete.

Entramos y nos zumbamos include y src

Rm -rf include src

Creamos directorio launch

Mkldir launch

Editamos CMakeLists.txt, borramos lo de 99 y el if y decimos dónde están los launchfile para que los instale (todos, no es necesario decir uno a uno).

(defajo de find_package)

install(DIRECTORY
  launch
  DESTINATION share/${PROJECT_NAME}
)

Ahora vamos a crearlo

cd launch
Touch number_app.launch.py

Son ficheros python y la convención es nosequé.launch.py
Chmod u+x number_app.launch.py

Editamos el fichero. No es un fichero típico de python. Lo  único que necesitamos es una función que se llame generate_launch_description():

From launch import LaunchDescription

def generate_launch_description():
  ld = LaunchDescription()

  Return ld

Esta es la template para los launchers que hagáis

Lo construimos y probamos que funciona (y que no hace nada)

Colcon build
Ros2 launch my_robot_bringup number_app.launch.py

Vamos a hacer ahora nuestro launcher

From launch import LaunchDescription
From launch_ros.actions import Node

Def generate_launch_description():
  Ld = LauncherDescription()
  Number_publisher_node = Node(
    package=’my_py_package’,
    executable=’number_publisher’,
  )

  Counter_node = Node(
    Package = ‘my_cpp_pkg’,
    Executable = ‘number_counter’,
  )

  ld.add_action(number_publisher_node)
  ld.add_action(counter_node)

Ojo, tenemos que añadir las dependencias en nuestro paquete. En este caso, sólo necesitamos dependencias de ejecución, no las necesitamos para construir el paquete, por lo que:

<exec_depend>my_py_package</exec_depend>
<exec_depend>my_cpp_package</exec_depend>

Lo lanzamos y vemos que funciona
-->

---

# Argumentos de un <i>launcher</i>

<!--
Al igual que podemos modificar desde la línea de comandos prácticamente todo, podemos hacerlo desde los launcher

Cambiar nombre de nodo

Node(
  package=...,
  executable=...,
  name=’nuevo nombre’,
)

Cambiar el nombre de un topic o de un servicio

Node(
  package=...,
  executable=...,
  name=’nuevo nombre’,
  remappings=[
    (‘number’, ‘my_number),
    ...
  ]
)

Añadir parámetros (no los hemos visto)

…
parameters=[
  {‘publish_frequency’:10}
]
-->

---

<!--
   _class: transition
-->

# Parámetros

---
<!--
   _class: transition
-->

# ¡GRACIAS!
