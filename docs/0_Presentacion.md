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
![bg left:33%](https://camo.githubusercontent.com/aa347732b8e27513a8ee971b2a95671241861795fa047cefb9dc34b9816e4c55/68747470733a2f2f696d616765732e756e73706c6173682e636f6d2f70686f746f2d313536323735383737382d6535363338623562363630373f69786c69623d72622d312e322e3126697869643d4d6e77784d6a4133664442384d48787761473930627931775957646c66487838664756756644423866487838266175746f3d666f726d6174266669743d63726f7026773d36323726713d3830)

<div class="title">Presentación de la asignatura</div>
<div class="subtitle">Robótica</div>
<div class="author">Alberto Díaz y Raúl Lara</div>
<div class="date">Curso 2022/2023</div>
<div class="organization">Departamento de Sistemas Informáticos</div>

[![height:30](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-informational.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

---

# Presentación

- Profesores
  - Alberto Díaz Álvarez <a href="mailto:alberto.diaz@upm.es">alberto.diaz@upm.es</a>
  - Raúl Lara Cabrera <a href="mailto:raul.lara@upm.es">raul.lara@upm.es</a>
  - Departamento de Sistemas Informáticos

- Información básica
  - Moodle de la UPM: <https://moodle.upm.es/>
  - Repositorio de GitHub: <https://github.com/laracabrera/robotica>

- Recomendaciones
  - Álgebra lineal
  - Análisis matemático
  - Python

---

# ¿De qué va la asignatura?

El mundo está cada vez más <i>robotizado</i>

- Veremos que la automatización y la robótica domina nuestras vidas
- En esta asignatura estudiaremos los fundamentos y tecnologías de la robótica

La robótica abarca tres disciplinas principales:

- Mecánica
- Electrónica
- **Informática**

Nosotros pondremos especial énfasis en esta última parte

- Que es la más interesante, todo sea dicho

---

# Temario

 1. Introducción
 2. Tecnologías
 3. Percepción del entorno
 4. Actuación sobre el entorno
 5. Control y optimización
 6. Toma de decisiones
 7. Aplicaciones

---

# Objetivos

Que pasados unos cuantos años desde hoy, los estudiantes:

- Puedan determinar el qué alcance tienen las aplicaciones robóticas
- Sean capaces de reflexionar sobre su impacto en la sociedad
- Sepan documentar proyectos de sistemas complejos (por ejemplo, un robot)
- Puedan identificar herramientas de uso común en aplicaciones robóticas
- Entiendan el funcionamiento por separado y en conjunto de los diferentes subsistemas de un robot
- Sepan por qué hemos dedicado tantas horas a álgebra, cálculo, probabilidad...

---

# ¿Qué se espera que aprenda el estudiante?

- *RA467*: Desarrolla aplicaciones en el ámbito de la Robótica
- *RA466*: Plantea el diseño de sistemas robóticos específicos
- *RA141*: Es capaz de trabajar como miembro de un equipo con la finalidad de contribuir a desarrollar proyectos con pragmatismo y sentido de la responsabilidad, asumiendo compromisos y teniendo en cuenta los recursos disponibles. Se desenvuelve de modo que logra generar confianza y credibilidad en un grupo de colaboradores, además del compromiso para el logro de la visión corporativa a través de negociaciones y motivaciones, y no de manera coercitiva e individualista.
- *RA464*: Resuelve problemas en el ámbito de la Robótica, considerando y valorando alternativas
- RA135: Analiza las necesidades de automatización de un proceso industrial
- RA465: Realiza el análisis de robots manipuladores

---

# Organización de la asignatura

- 4 horas a la semana, que se dividen en (aproximadamente)
  - 2 horas de teoría
  - 2 horas de prácticas en laboratorio

- Todas las actividades se realizarán en grupos de 2 alumnos
  - Excepto los cuestionarios, claro

- Las actividades tienen un mínimo, **no un máximo**; se valorará **mucho**:
  - Que el alumno profundice
  - Que proponga prácticas adicionales
  - Que genere documentación
  - Que corrija o amplíe teoría

---

# Evaluación

La asistencia a clase **es obligatoria**; pero no se controla la asistencia

- Estamos cursos superiores, ya somos mayorcitos

Nota de la asignatura:

- Convocatoria ordinaria: 30% cuestionarios + 70% práctica (**obligatoria**)
- Convocatoria extraordinaria: 30% teoría + 70% práctica (**obligatoria**)
- La nota mínima para aprobar será un 5.0

¿Cómo subir nota si estoy aprobado?:

- Con prácticas opcionales: Se propondrán a lo largo de la asignatura
- Participación en clase, corrección y generación de material

---

# Normas

- Realizar las **actividades a tiempo**
- **Respetar a los compañeros** y a su derecho a la educación
- Citar claramente todas las fuentes (incluidos colaboradores). De esta manera mantendremos una correcta ética de trabajo y, como efecto colateral, el equipo docente puede sugerir dichas fuentes a futuros estudiantes
- La colaboración con otros humanos se debería limitar a discusión. El código y la documentación deberá realizarla el grupo responsable de la práctica
- Cada estudiante debe ser capaz de responder a cuantas preguntas se le hagan sobre sus tareas cuando se le solicite
- Se mantiene una **tolerancia cero ante el plagio**. Cualquier plagio detectado implicará un suspenso en ambas convocatorias de la asignatura

---

# Desglose en créditos

- 6 créditos a 26 horas de trabajo por crédito $\equiv$ 156 horas de trabajo
  - Asistencia a clase: 60 horas
  - Prácticas y proyectos: 90 horas
  - Cuestionarios (preparación y realización): 6 horas

- Por supuesto, esto es orientativo; depende de la capacidad del alumno

---

<!--
   _class: transition
-->

# Recursos de aprendizaje

---

# Recursos

Moodle de la UPM (<https://moodle.upm.es>)

- Materiales de teoría, de evaluación y demás información
- *Corregir y ampliar contenido tendrá un impacto positivo*

Repositorio de la asignatura (<https://github.com/laracabrera/robotica>)

- Fuentes de las transparencias y de programas usados durante la asignatura
- *Corregir y ampliar contenido tendrá un impacto positivo*

Libros

- Fundamentos de robótica. Antonio Barrientos y otros
- Robotics, Vision and Control, Springer, Peter Corke
- Introduction to Autonomous Mobile Robots, Roland Siegwart y otros

---
<!--
   _class: transition
-->

# Gracias
