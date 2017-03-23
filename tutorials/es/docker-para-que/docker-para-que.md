# Docker ¿Para qué?

Docker es una aplicación que, utilizando tecnologías del kernel para aislar recursos, permite crear *containers* con los que se puede correr procesos en entornos aislados entre si.

Esta charla se centrará más en la utilidad que en los detalles técnicos.

## ¿Para qué sirve Docker?

* Ejecutar procesos en *containers*, es decir, entornos virtuales.

* Armar y compartir imágenes a través del registry (docker hub)

## ¿Para qué no sirve Docker?

* Unir servidores o VMs

* Para aislar containers entre si (comparten el kernel)


### ¿Dockers o VMs?

Las **máquinas virtuales** son entornos completamente aislados, hardware "virtual". Una VM usa su propio BIOS, almacenamiento en disco, cpu, ram, interfaz de red, y, en particular, su propio sistema operativo.

Los **containers** no abstraen el hardware, sino a nivel del sistema operativo. A nivel proceso para ser más preciso.
Cada container comparte el mismo sistema operativo, el mismo kernel, reduciendo el overhead para llegar al host.
Cada container está hecho para correr un único comando

Notar que, al compartir kernel, los containers son más vulnerables que las VMs.

## Docker es como Java

Una frase icónica de Java es "Escribir una vez, correr en todos lados". Java nos permite compilar código que resulta en archivos .class, que puede ejecutarse en cualquier JVM (bueno, siempre y cuando el código use features soportados por la versión de la JVM)
La filosofía de Docker es la misma: crear imágenes para que puedan correr en cualquier máquina con docker.

### Imágenes ¿Como git?

Una imagen es un conjunto de capas que contienen archivos que serán usados como base de nuestro container.
Por ejemplo, podemos tener una imagen de debian, con sus bibliotecas standard, y arriba de esa imagen armar otra con, por ejemplo, una versión específica de java, o de posgresql.

## Algunos usos de docker

### Distribución de aplicaciones

Al crear una imagen con nuestra aplicación, le facilitamos a los usuarios la instalación de la misma, ya que no tiene que manejar dependencias, y no hay riesgo de conflicto de las mismas.
Enlatamos la aplicación para que el usuario las pueda ejecutar de forma sencilla

### Aislar aplicaciones

*AppA requiere la biblioteca libfoo.1.2, pero es incompatible con AppB que requiere libfoo.2.0*, *Este servidor catalina requiere java 4.0*.... etc, son típicos escenarios de una máquina con aplicaciones de distinta generación que corren en simultaneo.

Docker nos permite crear un entorno virtual para cada proceso, de modo que este utiliza las bibliotecas provistas por la imagen.

Otro escenario molesto es el de *El puerto nn está en uso*
Además de un entorno propio, cada proceso tiene su propia interfaz de red, además de que se puede controlar los recursos que utiliza cada proceso: RAM, CPU, transferencia a disco, etc.

    Ver demo 00-java y 00b-json-server

### Debuggear

*Subí este cambio y el servidor crasheó*, *En mi máquina anda*:
Docker permite duplicar el entorno de desarrollo en segundos. Al ser el mismo entorno en todas las máquinas, disminuye el riesgo de errores cuando se migra de un entorno de desarrollo a otro. Además, se pueden guardar múltiples instancias de las imágenes o container para comparar las distintas ejecuciones de una aplicación.

### Fácil orquestación de aplicaciones

Docker nos permite orquestar distintos containers mediante la herramienta *compose*. Compose nos permite levantar distintos containers, vincularlos entre si, asignar recursos compartidos, puntos de montaje, etc.
Un ejemplo clásico es levantar un container que corra una base de datos, otro con una API rest, otro un servidor web.

    Ejemplo de docker compose: mostrar wordpress o flask
    comunicandose con un container sql

### Tests de integración

Crear un container a partir de una imagen es casi instantaneo. Si creamos una imagen con nuestros datos de pruebas listos para ser utilizados, no solo nos aseguramos que todos puedan correr las mismas pruebas, sino que, en caso de modificación de los datos mismos (por ejemplo, ingresar o eliminar datos en una base de datos), se puede eliminar rápidamente el container y crear otra vez uno nuevo.
Recordar que Docker opera con un sistema de capas, lo que facilita mucho la destrucción y creación de containers.
Con esta misma filosofía, podemos hacer una especie de integración continua con ayuda de docker.

    Ejemplo de una api rest ¿Reutilizar la demo de flask?


### Otros usos

Algunos otros usos son

* *Probar aplicaciones sospechosas*

* *Limitar recursos a un proceso*: Posee una sintaxis sencilla para limitarle recursos a un proceso

* *Mockear servicios*: Si tenemos que desarrollar contra un servicio inaccesible, se puede levantar un container que replique la funcionalidad deseada.

* *Validar dependencias de nuestras aplicaciones*