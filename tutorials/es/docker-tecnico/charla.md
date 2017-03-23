# ¿Qué es docker?

*¿Qué es docker? ¿Para qué sirve? ¿Con qué se come?* En esta presentación voy a explicar en qué consiste este nuevo-viejo servicio que cada vez es más popular y crece constantemente.


## Docker

Es una plataforma de código abierto que nos permite aislar aplicaciones en *containers*.
¿Qué sería *aislar* una aplicación? Es, a grosso modo, crear un entorno virtual, también llamado *jaula*, para nuestra aplicación, de forma que este no tenga acceso al sistema operativo host.
¿A qué me refiero con *enlatar*? Docker nos da muchas prestaciones para que nuestras aplicaciones puedan ser guardadas y distribuidas con poco esfuerzo

Las primeras versiones de Docker estaban basadas en el proyecto *LXC* (Linux containers), luego crearon su propia biblioteca *libcontainer*, también de código abierto, disponible en github.


## Containers

Recién mencioné la palabra *container*. Un container es un entorno aislado donde se va a ejecutar una aplicación. Es básicamente un directorio en nuestro sistema operativo.
Los containers se crean a partir de una imagen base, es decir, una "foto" del entorno sobre el que queremos trabajar.
Al crear un container se corre un comando de entrada que puede venir configurado en la imagen, o podemos setear nosotros mismos.

Estos comandos van a correr dentro del container como si no existiera nada fuera del mismo.


## Containers vs VMs

Todo esto suena muy parecido a algo que conocemos hace mucho, las *VMs*, que nos permiten aislar los procesos, controlar recursos etc ¿En qué difieren?

### VMs

En principio, como dice su nombre, las VMs son **máquinas** virtuales, *hardware virtual*. Los servicios de VMs, como Vagrant o VirtualBox, emulan un hardware sobre el que se instala un sistema operativo completo.

Las máquinas virtuales son administradas por un monitor conocido como hipervisor.

### Container

La magia de Docker proviene de utilizar features del kernel para aislar y administrar los recursos. Es el mismo kernel del sistema host el que se comparte entre todos los containers, con el mismo scheduler, manejador de memoria, etc.

Esta falta de abstracción u *overhead* provee ventajas como rapidez en levantar un contenedor y menor consumo de recursos, pero también hay que tener en cuenta que utilizar el mismo kernel para los containers y el host es más inseguro para el sistema.


## VMs vs docker (gráfico)

Acá hay un ejemplo de VMs sobre un hipervisor y containers sobre docker.
Como se puede apreciar, las VMs poseen un sistema operativo propio, como puede ser Windows, Solaris, BSD, etc.
Por el otro lado, docker solo puede correr containers de linux sobre el kernel de linux, pero no tiene que lidiar con la carga del sistema operativo.


## Imágenes

Ya hablamos bastante de cómo trabaja docker y cómo se diferencia de una VM, volvamos a los containers, que es lo más jugoso de la charla.
Repasamos: ¿Qué es un container? Una *caja*. ¿Cómo se crean los containers? A partir de una imagen, una *foto*.
Una imagen es un *archivo inmutable* que almacena una serie de *cambios en el filesystem*, además de configuraciones para los containers que va a generar.
Como son archivos grandes generalmente se componen de otras imágenes, funcionando como *capas*.


## Creación de imágenes

Hay varias formas de obtener imágenes, como puede ser descargarlas desde internet o importándolas desde un archivo.
Una de las formas más populares es construir imágenes a partir de una serie de instrucciones en un script llamado **Dockerfile**. Un Dockerfile es un archivo de texto con las instrucciones para generar una imagen paso a paso, generalmente a partir de otra imagen ya preexistente. Si la imagen no existe en nuestro sistema, se intentará descargar de internet.


## Dockerfile

La sintaxis de un dockerfile es muy similar a la de bash, con equivalencias como

* **run**: Ejecuta un comando

* **workingdir**: Cambia de directorio (*cd*)

* **add**: Copia un archivo desde el sistema host a la imagen

También hay comandos que ayudan a la configuración de la imagen, como setear variables de entorno, abrir puertos, agregar metadata, etc.

Para compilar la imagen, ejecutamos *docker build*, más el directorio donde se encuentra el dockerfile.
Cada comando que se ejecuta agrega una capa al paso anterior (con algunas excepciones, como workingdir o expose), por lo que es una muy buena práctica concatenar los comandos para reducir el número de capas (por ende, el tamaño de la imagen).
Si un comando falla, docker build devuelve el código de error de ese comando, y todos los pasos anteriores quedan guardados en un cache.

Docker build acepta muchas opciones de ejecución. Algunas opciones, por ejemplo, permiten elegir el nombre a la imagen generada, o activar/desactivar el cache de imágenes.


## Crear containers

Los containers se crean a partir de una imagen utilizando el comando

	docker create <img> <comando>

Este comando prepara un container, asignándole un hash y un nombre aleatorio. La configuración del container se realiza en esta etapa.
(Notese que el comando a correr se setea en esta etapa)

#### Slide siguiente

Los containers son altamente configurables, se puede configurar su interfaz de red, límites de recursos, volumenes para persistir datos, etc.
También se puede sobreescribir el entrypoint de la imagen, variables de entorno, o vincular a otros containers.
Es una buena práctica nombrar containers, ya que luego será utilizado este nombre para iniciarlos. Si no les asignamos un nombre, docker lo hará por nosotros. Los nombres deben ser únicos, y docker va a chillar si creamos dos containers con el mismo nombre.


## Iniciar containers

Una vez que nuestro container está creado, está listo para correr.

El comando **start** es bastante sencillo, recibe como argumento el nombre del container a inicializar, y posee flags que permiten definir si corre en *primer plano* o como un *daemon*.

En contrapuesta tenemos el comando **stop**. El comando *stop* recibe también el nombre del container como argumento, y cuando es utilizado, envía una señal *SIGTERM* para que el proceso se apague de forma feliz. Si pasado cierto tiempo el proceso sigue corriendo, se lo mata con *SIGKILL*

Por último, notar que el comando *run* es equivalente a *create* + *start*


## Comandos útiles

A continuación voy a nombrar algunos comandos muy útiles para el mantenimiento de containers e imágenes.

* *inspect*: Muestra información muy detallada del container en formato *JSon*, desde el nombre del container hasta configuraciones como variables de entorno o puertos utilizados.

* *ps*: Lista, por defecto, containers activos. Con *-q* muestra inactivos y *-a* todos.

* *images*: Lista imagenes disponibles en el sistema local, incluyendo capas intermedias

* *rm*/*rmi*: Elimina containers/imagenes. ¡Importante para no saturar el disco!


## Docker registry

Cuando hablé sobre la creación de imágenes, mencioné la descarga de las mismas. Existe una servicio de repositorio de imágenes llamado **Docker registry**. Registry permite almacenar imágenes para luego ser descargadas de forma muy similar a *git*. Es más, al igual que en git, los comandos para subir y bajar imágenes son *push* y *pull*

### Docker Hub

El servidor oficial de docker es Docker-Hub, y la instalacion de docker viene configurado por defecto para que descarguemos imágenes desde ahí.


# Docker avanzado

## Aislamiento no es virtualización

Es un grave error decir que Docker es un servicio de *"algo tipo máquinas virtuales"*. Docker utiliza los siguientes features para aislar los containers, **pudiendo ser configurados según la necesidad del usuario**.

* *Kernel namespaces*: los procesos corren con ids de procesos, usuarios, rutas de archivos, etc propios; bajo ningún concepto pueden ver procesos o directorios de otro container o del host. Por ejemplo, si yo en un container hago "killall nginx", solo termina los procesos nginx de ese container.

* *Chroot*: la raíz del container se encuentra en directorio dentro del host, y el container no puede ver más afuera de ahí.

* *uid_map, gid_map*: Los usuarios y grupos dentro del container pueden corresponder a otros fuera del mismo. Por ejemplo, *root* en un container puede estar mappeado a un usuario no privilegiado fuera del container

* *Control groups*: Se puede limitar la cuota y cantidad de cpus, velocidad de transferencia a los dispositivos, memoria ram, etc.

* *Interfaz de red propia*: tal como suena, con sus propios puertos, ip, etc.


## Filesystem

Acá es donde se puede apreciar el concepto de capas en Docker. Se utiliza UnionFS ¿Qué ofrece este sistema? Básicamente permite almacenar archivos como una serie de cambios en vez del estado completo de los mismos. Es un concepto muy similar a *Git*, donde uno hace commits de *cambios* y no del estado completo de los archivos.
Para ser más explicito, supongamos que mi imagen Foo está compuesta de los archivos A, B y C. Utilizando a Foo como base, creo la imagen Bar, en la que se agrega el archivo D, pero se elimina A.
La imagen Bar no se almacenará como B, C y D, sino como una adición del archivo D y el borrado de A sobre la imagen Foo.

Esto permite reutilizar imágenes (por ejemplo, una imagen "nodejs" con el interprete instalado para que todas mis aplicaciones hechas con node lo usen como base); y también permite, fundamentalmente, que los containers se puedan escribir en disco sin alterar las imágenes de las que fueron creados, y sin duplicar información.


## Volumenes

La filosofía de Docker es que los contenedores sean volátiles y no contengan estado. La persistencia debe ser realizada por medio de puntos de montaje llamados **volúmenes**. 

Existe 3 formas de montar volúmenes dentro de un container

### Montar un directorio del host

La opción -v *path_host*:*path_container* nos deja montar un directorio del sistema host en la ruta especificada dentro el container. Los contenidos que estaban en ese path dentro del container son superpuestos por los que estan en el directorio del host. Las escrituras que se hagan dentro del directorio montado se harán con el uid y gid del usuario dentro del container (por lo que, si es *root* el usuario dentro del container, los archivos del host serán escritos por root)
Disclaimer: *verificar si ya es soportado el mapeo de ids en las nuevas versiones de docker*

### Volúmenes anónimos

A veces no queremos ser nosotros los que administramos los volúmenes, sino pasarle ese trabajo a docker. Si montamos un volumen sin asignar un path del host, docker lo montará en un directorio propio (dentro de /var/lib/docker). A diferencia de la opción anterior, los datos en el directorio montado dentro del container *son copiados* al volumen anonimo.
Estos volumenes pueden ser nombrados y al igual que los containers, necesitan mantenimiento, ya que pueden persistir luego de que se haya eliminado el container que los creó.

### Volumenes compartidos

Otra forma de montar volumenes es tomando los volumenes de otro container. Esta opción nos trae la ventaja de poder compartir datos entre varios containers, pero es importante tener en cuenta que los problemas de concurrencia que se pueden generar.


## Backups

### Exportar/importar imagenes

En caso de que necesitemos hacer back ups de las imágenes, o simplemente transportarlas físicamente, docker nos ofrece dos comandos para copiar desde y hacia un archivo binario:

	docker save <img> > <path>
	docker load <img> < <path>

*Save* nos permite guardar una imagen junto a todos sus metadatos, para que luego puedan ser reincorporados con el comando *load*.

​### Exportar/importar containers

Al igual que las imágenes, los containers pueden ser exportados e importados desde y hacia un archivo binario.

docker export <container> > <path>
docker import <container> < <path>

### Convertir container en imagen

docker commit permite que un container sea convertido en una imagen. Recordemos que un container mantiene el estado de la capa sobre la cuál escribe, por lo que si contamos al container como una capa extra del sistema, commit simplemente convierte esta capa en una imagen.
Nota: esta nueva imagen no contiene los metadatos del container.


## Limitar recursos


## Topologías de red