# Restructured Text

La combinación de Markdown + Pandoc puede ser muy útil y versátil, pero posee un gran problema que es la falta de estandarización.
Si bien la implementación de *CommonMark* hizo un intento por estandarizar el lenguaje, es muy común encontrar variaciones entre las distintas formas de implementar el lenguajes.

Una alternativa que cubre estos problemas es **ReStructured Text**

ReStructured Text posee una sintaxis muy similar a la de markdown (con algunas reglas más), pero además posee un formateo por bloques que contribuye a la claridad del texto.
A su vez, el lenguaje tiene muchas más funciones predefinidas que reduce la posibilidad de ambiguedades a la hora de escribir documentos.

## Sphinx

El principal uso de RST se da mediante la herramienta de documentación **sphinx-doc**. Sphinx es una herramienta desarrollada en python creada principalmente para documentar proyectos (principalmente de python). Sin embargo, debido al esquema de archivos que tiene, también puede usarse para documentación en general al estilo wiki.

### Paseo general

Esta aplicación se encuentra en los repositorios oficiales de ubuntu, por lo que se instala con el comando
~~~ {.bash}
sudo apt install sphinx-doc sphinx-common
~~~

Sphinx "extiende" markdown con estructuras del formato:

~~~ {.rst}
.. estructura ::
    :opciones: valores

    Contenido
~~~

Por ejemplo

~~~ {.rst}
.. csv-table:: Mi tablita
    :header: "Columna 1", "Columna 2", "Columna 3"
    :width: 10, 20, 20

    1, "violeta", "Tinky winky"
    2, "verde", "Dipsy"
    5, "amarillo", "Laa laa"
    7, "rojo", "Po"
~~~

Generan una tabla como la siguiente:

Columna 1      Columna 2                    Columna 3
-------------- ---------------------------- ----------------------------
1              violeta                      Tinky winky
2              verde                        Dipsy
5              amarillo                     Laa laa
7              rojo                         Po

### Cómo iniciar un proyecto

Para iniciar un proyecto simplemente se escribe `sphinx-quickstart`, y nos inicia un asistente por consola para realizar configuraciones básicas del proyecto, como el nombre, carpetas, etc.

Una vez que termina el asistente, genera una estructura de archivos en los que cabe resaltar:

* *conf.py*: configuración general del proyecto

* *Makefile*: script *compilador*

* *index.rst*: raiz del proyecto, con el esquema básico para agregar documentos y generar un índice

Para agregar secciones al documento, se agregan los nombres de los documentos rst a la sección `.. toctree::
