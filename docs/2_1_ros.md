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

---

# Sobre los mensajes en ROS

En la página sobre interfaces se describen todos los tipos de datos básicos
- [https://docs.ros.org/en/humble/Concepts/About-ROS-Interfaces.html]()

Los tipos de datos complejos suelen tener sus propios repositorios
- E.g. [http://github.com/ros2/example_interfaces]()
- Se encuentran bajo `msg/` (y `srv/`, pero eso lo veremos más adelante)
- Los ficheros `.msg` dan la misma información que ejecutar `ros2 interfaces`

Un repositorio muy útil para aplicaciones reales es `common_interfaces`
- [http://github.com/ros2/common_interfaces]()
- Se instalan por defecto al realizar la instalación de `ros desktop`


---

# Mensajes personalizados

Un topic se caracteriza por un **nombre** y una **interfaz** o tipo
- El tipo de mensaje se describe con una sintáxis propia de ROS
- Durante la compilación del <i>workspace</i> (`colcon`) cada mensaje se <i>transpila</i>
- Con este proceso se generarán los fuentes específicos para cada lenguaje

<center>

![](../img/t2/transpiling.png)
</center>


Un convenio que se sigue a rajatabla es:
- Si el tipo es básico, empieza en minúscula (e.g. `int`, `string`)
- Si el tipo es compuesto, en mayúscula (e.g. `Header`)

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

---

# Tipos de mensajes (interfaces) personalizados

Las interfaces se suelen crear en paquetes dedicados a exclusivamente a ello
- Por reducir dependencias; se pueden crear en cualquier paquete
   ```
   $ ros2 pkg create sensor_interfaces
   ```
- Lo del sufijo `_interfaces` es otro convenio que se suele usar en ROS
- El directorio `src/` no se suele usar, así que lo más común es borrarlo

Cada tipo de mensaje va en un fichero `.msg` dentro del directorio `msg/`
- Si el directorio no existe, es necesario crearlo
- El convenio para nombrar ficheros de mensaje es `CamelCase`

---

# Pasos para la creación de una interfaz

Dentro del paquete donde queramos definir la interfaz:

1. Creamos la interfaz (fichero `.msg`) dentro del directorio `msg/`
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

# Usando una interfaz

Al igual que hemos hecho con las interfaces preinstaladas, basta con:

1. Añadir la dependencia del paquete que contiene la interfaz a `package.xml`
   ```xml
   <depend>paquete_con_interfaces</depend>
   ```
1. Importar la interfaz del paquete en nuestros fuentes
   ```xml
   <depend>from paquete_con_interfaces.msg import Interfaz</depend>
   ```

---

<!--
   _class: transition
-->

# Servicios

---

# Servicio

Es un sistema de comunicación de arquitectura **cliente/servidor**
- Permiten la comunicación **síncrona o asíncrona** entre nodos
- Están pensados para la comunicación bidireccional entre nodos
  - Dos tipos de mensaje, uno para la <i>request</i> y otro para la <i>response</i>
  - Eso sí, ambos tipos se encuentran dentro del mismo fichero `.msg`
- Un único servidor sólo puede existir una vez en una aplicación
  - Eso sí, puede ser accedido por múltiples clientes
---

# Creación de un servidor

Un servicio se caracteriza por un **nombre único** y una **interfaz**
- Vamos, como un <i>topic</i>
- Eso sí, las interfaces incluyen dos tipos de mensaje: **request** y **response**
- Se separan por tres guiones (encima <i>request</i>, debajo <i>response</i>)

Por ejemplo, un servicio para localizar el número de vehículos en un área:
```
float32 lat
float32 lon
float32 radius
---
int64 n
```

---

Para crear el servidor usaremos el método `create_service` de `Node`:
```python
server = <nodo>.create_service(<mensaje>, <name>, <callback>)
```
- Convenio para nombrar los servicios: Comenzar su nombre por un verbo
- Por ejemplo, `'get_number_of_vehicles'`

El <i>callback</i> será una función que recibirá dos parámetros
- Objeto <i>request</i> con el contenido de la petición hecha al servidor
- Objeto <i>response</i> a rellenar para devolver al cliente de la petición
   ```python
   def callback_get_number_of_vehicles(self, request, response):
      response.sum = request.a + request.b
      self.get_logger().info(f'{request.a} + {request.b} = {response.sum}')
      return response
   ```

Podemos ver que el funcionamiento es similar al de los <i>topics</i>

---

Por último, nos quedaría la configuración:

1. Añadir el nodo al setup.py
   ```python
   get_number_of_vehicles_server = paquete.get_number_of_vehicles_server:main
   ```
2. Construir y desplegar el paquete
   ```bash
   $ colcon build --packages-select my_py_pkg --symlink-install
   ```

En este punto ya podemos lanzar nuestro nodo
```bash
$ ros2 run my_py_pkg get_number_of_vehicles
```

Para comprobar el funcionamiento necesitaremos un cliente que acceda al servicio

---

# Breve nota sobre la CLI (sí, otra más)

Siempre es posible testear el server directamente desde la terminal
- Para conocer los servicios disponibles usamos el siguiente comando
   ```bash
   $ ros2 service list
   ```
- También podemos saber la información de un servicio en concreto
   ```bash
   $ ros2 service info get_number_of_vehicles_server
   ```
- Por último, si lo que queremos es hacer una llamada a un servicio:
   ```bash
   $ service call /get_number_of_vehicles paquete/srv/NoOfVehicles "{ \
      lat: 40.3831651, \
      lon: -3.6222915, \
      radius: 250 \
   }"
   ```

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

Para realizar llamadas a un servicio necesitamos crear un cliente

```python
client = <node>.create_client(<interface>, <nombre>)
```

Las llamadas se realizan usando el método `call` del cliente
```python
response = client.call(request)
```

Al igual que con el servidor o con un topic, es necesario:
1. Actualizar el `setup.py`
   ```python
   get_number_of_vehicles_client = paquete.get_number_of_vehicles_client:main
   ```
2. Construir y desplegar el paquete

---

Cuidado, los nodos son independientes entre sí:
- Puede pasar que se llame a un servicio sin que este esté se haya arrancado
- Para que el método no dé error, lo típico es realizar una espera
   ```python
   while not client.wait_for_service(<timeout>):
      node.get_logger().warn('Esperando al servicio ...')
   ```
- El timeout es opcional; si no se especifica esperará indefinidamente

---

# Llamadas síncronas y asíncronas

`call` realiza una **llamada bloqueante**, y lo más común es usar `call_async`
   ```python
   future = client.call_async(request)
   ```
   - Un <i>future</i> es un objeto que en algún momento tendrá la respuesta a la llamada
   - Podemos dejar el proceso esperando a la respuesta de la siguiente manera:
      ```python
      rclpy.spin_until_future_complete(node, future)
      ```
   - Una vez la instrucción finaliza, en el objeto future tenemos la respuesta
      ```python
      try:
         Response = future.result()
         self.get_logger().info(a + b = sum)
      except Exception as e:
         node.get_logger().error(f‘Error: {e}’)
      ```

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
