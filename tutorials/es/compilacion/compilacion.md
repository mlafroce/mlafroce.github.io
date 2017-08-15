# Compilación

Esta charla es una introducción al uso del compilador *gcc* y makefiles. 

NOTA: En los ejemplos se utilizará el compilador g++, pero las mismas reglas se aplican a gcc para compilar C.

## GCC y la cadena de herramientas

### Hola mundo

Lo primero que hacemos al empezar a aprender un lenguaje, framework, herramienta, etc nuevo es el clásico *hola mundo*.
Nuestra primera compilación será entonces del siguiente código:

~~~ {.cpp #hola-mundo}
#include <iostream>

int main (int argc, char** argv) {
    std::cout << "Hola mundo" << std::endl;
}
~~~

El código será guardado en un archivo **hello.cpp** lo compilaremos corriendo

~~~ {.bash}
g++ hello.cpp -o hello
~~~

Notar que usamos *g++* debido a que el código compilado es C++, si compilaramos C, el compilador a invocar sería *gcc*.
Si nuestro compilador está correctamente instalado, se genera un archivo ejecutable *hello*.

### Paso a paso

Al invocar gcc/g++, por defecto se ejecutan una serie de pasos para generar un ejecutable:

* **Preproceso**: En esta etapa, el *preprocesador* (cuyo nombre es *cpp*, por C PreProcessor) expande las directivas y macros como *include*, *define*, etc.
Se le puede indicar a gcc detenerse en esta etapa ejecutando.

~~~ {.bash}
g++ -E
~~~

O bien se ejecuta de forma independiente con el comando *cpp archivo.cpp -o archivo.i*.

* **Compilación**: Esta es la etapa de *compilación* propiamente dicha, donde se convierte el código expandido en *código assembly*.
Se le puede indicar a gcc detenerse en esta etapa ejecutando

~~~ {.bash}
g++ -S
~~~

* **Assembly**: Esta es la etapa donde el código assembly se transforma en *código objeto*. Este ya es código en lenguaje de máquina, pero con algunas anotaciones y variables parametrizadas para luego ser utilizados en la etapa de *linkeo*. Para detenerse en este paso ejecutar

~~~ {.bash}
g++ -c
~~~

* **Link**: En esta última etapa, se acomodan los distintos pedacitos de código objeto generados con bibliotecas ya preexistentes en nuestro sistema, se enlaza con las bibliotecas dinámicas (.so en unix, .dll en windows) y se genera un ejecutable.

### Modo verboso

Compilar utilizando *g++ -v <fuente>* nos muestra por consola todos los flags utilizados en varias etapas de la compilación.

## Bibliotecas

### Crear bibliotecas estáticas

Una biblioteca estática es básicamente un montón de código objeto que generalmente se indexa para ser utilizado en otras compilaciones. Su extensión en unix es *.a* y en windows es *.lib*, como por ejemplo *libzip.a*, que permite operar con archivos zipeados.

Crear una biblioteca es muy fácil, primero ejecutamos *g++ -c* para crear el código objeto que queremos empaquetar. Para empaquetarlo utilizamos el comando:

~~~ {.bash}
ar -crs <nombre-lib.a> <archivos.o>
~~~

* *-c*: Crea el archivo de salida, o lo actualiza si existe. Si el flag se omite y el archivo no existe, lanza un warning.

* *-r*: Reemplaza las entradas ya repetidas.

* *-s*: Indexa el archivo.

Para inspeccionar los contenidos de una biblioteca, utilizamos:

~~~ {.bash}
ar -t <libfoo.a>
~~~

O bien para ver qué símbolos están definidos dentro:

~~~ {.bash}
nm -C <libfoo.a>
~~~

### Compilar contra una biblioteca estática

Compilar contra una biblioteca estática es muy fácil porque es muy similar a tener los archivos de código objeto. Podemos linkearlos como si fueran otro archivo ".o" más, por ejemplo:

~~~ {.bash}
g++ -c class0.cpp class1.cpp ...
ar -crs libclasses.a *.o
g++ main.cpp libclasses.a
~~~

### Crear una biblioteca dinámica

Crear una biblioteca dinámica es muy similar a compilar una aplicación. La diferencia fundamental es que el código objeto generado **debe** tener código independiente de la posición (*Position independent code*: PIC)

Para esto, recompilamos nuestros archivos fuente pasándole el parámetro *-fPIC*

~~~ {.bash}
g++ -fPIC -c class0.cpp class1.cpp ...
~~~

Y luego linkeamos en una biblioteca dinámica:

~~~ {.bash}
g++ -shared -o libclasses.so *.o
~~~

### Compilar contra una biblioteca dinámica

Al igual que una biblioteca estática, podemos usarlo como *target* de linkeo

~~~ {.bash}
g++ main.cpp libclasses.a
~~~

También podemos linkear contra bibliotecas instaladas en el sistema, pasando el flag *-l* seguido del nombre de la biblioteca (sin "lib" ni extensión)

Otro ejemplo:
	
~~~ {.bash}
g++ main.cpp -lzip
~~~

Este comando intentará encontrar el archivo libzip.so dentro de las bibliotecas del sistema (que son las de la variable *LIBRARY_PATH* que se puede ver al correr g++ en modo verboso)

Si se quiere agregar un directorio de bibliotecas, se debe utilizar el flag *-L*

Si existen tanto la versión estática como la dinámica de una biblioteca, se toma la dinámica.
Este comportamiento puede ser alterado utilizando los flags *-Bstatic* y *-Bdynamic* (En combinación con *-Wl,*)

#### Ver dependencias de bibliotecas

Para ver qué bibliotecas dinámicas son necesarias para cargar nuestra aplicación, utilizar el comando *ldd <ejecutable>*

\newpage


## Makefiles

### Introducción

Para simplificar la compilación, es muy común utilizar *make* para ejecutar las de compilación.
Make por defecto busca un archivo conocido como *Makefile*, que posee el siguiente esquema:

~~~ {.make}
target: dependencias
	instrucciones

otroTarget: otroTargetMas
	más instrucciones
~~~

El target por defecto es el primero que no tiene un "." por delante. Por convención el primer target es *all*

*** Ver Ejemplo 1 ***

### Phony: targets virtuales

Cuando se ejecuta un target, se revisa el timestamp del archivo con el mismo nombre, y el de sus dependencias, recursivamente. Si no hubo modificación en las dependencias (posterior al target), el target se encuentra actualizado, por lo que no se ejecuta.

Como se puede ver, el ejemplo tiene el grave defecto que si existen archivos all o clean, estos targets se ejecutarían siempre (excepto que actualicen dichos archivos). Es más, en el caso de clean, como no hay dependencias, se considera que siempre está al día, y nunca se ejecuta.

Para evitar esto se declaran estos targets como virtuales utilizando *.PHONY*

### Variables

*make* permite utilizar variables, viniendo con varias ya predefinidas para mayor flexibilidad.
Las variables se identifican porque vienen entre paréntesis precedidas de un signo "$"

Algunas variables ya vienen predefinidas, como por ejemplo, en un entorno linux *CC* suele referenciar a *gcc*, *CXX* a *g++*, *RM* a *rm -f*, entre otros.

También podemos declarar nuestras propias variables, lo que es una muy buena práctica para no hardcodear valores a lo largo del makefile.

*** Ver Ejemplo 2 ***

Como se puede ver, ahora los archivos objeto dependen de los *.cpp*. Por un lado la notación es más sencilla, pero por otro lado, modificar cualquier *.cpp* involucra recompilar todos los archivos objeto. Además, al ser una única tarea, no es paralelizable.
Una posible solución es crear a mano un target *.o* por cada *.cpp* presente, pero claramente esto es incómodo y poco viable.

#### Variables automáticas

Durante la ejecución de un target se crean distintas variables, por ejemplo:

* **$@**: Nombre del target

* **$<**: Nombre del primer prerequisito

* **$?**: Nombres de las dependencias que son más nuevas que el target

#### Patrones

Otro feature interesante es el de *pattern matching*. Utilizando el símbolo **%** declaro reglas implícitas, que son llamadas sobre cualquier target que haga match con el patrón utilizado.

*** Ver ejemplo 3 ***

Este ejemplo, si bien es paralelizable, tiene el defecto de que no detecta árboles de dependencias. Por ejemplo, si mi clase Foo hereda de Bar, y modifico la clase Bar, Foo no se recompila.

### Detección de dependencias básicas

Para crear un detector de dependencias básicos, utilizaremos el comando *gcc -MM*, que genera un listado de dependencias para los archivos pasados por parámetro.

Este generaremos un archivo .dep por cada target de compilación (Por fines didácticos se hará cambiando la extensión de .o a .cpp). Luego se incluirá el contenido de este .dep a dentro del makefile, sólo como targets con dependencias, sin ninguna instrucción en particular.

\newpage

# Bibliografía:

* https://linux.die.net/man/1/gcc

* https://www.gnu.org/software/make/manual/

* https://www3.ntu.edu.sg/home/ehchua/programming/cpp/gcc_make.html
