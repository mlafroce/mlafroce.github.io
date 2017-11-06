# Introducción a Git

## Sistemas de control de versionado

¿Qué es el control de versionado? Es una herramienta que nos *permite guardar distintas* versiones de un archivo para poder acceder a ellas según vayamos necesitando.
Esto nos evita malas prácticas como tener múltiples copias de un archivo y renombrarlo, ej: *tp1* *tp1.corregido* *tp1.bck* *tp1.nocompila*, etc.

Existen distintos sistemas de control de versionado, que ofrecen distintas metodologías de trabajo, cada una con sus ventajas y desventajas.
Aun así, la gran mayoría posee las siguientes características:

* *Repositorio*: Un repositorio es una carpeta donde se almacenan las distintas versiones de nuestros archivos. A medida que un proyecto avanza, se van guardando los avances en un repositorio para que, en caso de ser necesario, se pueda consultar versiones anteriores para consultar cambios, encontrar errores, etc.

* *Commits atómicos*: Un *commit* es un conjunto de cambios que se almacena en un repositorio. Cada commit simboliza una versión de nuestros archivos, y puede agrupar cambios de distintos archivos a la vez. Es buena práctica realizar commits frecuentemente.

* *Log de cambios*: Cada *commit* puede (y debe) ser acompañado por un texto que describe qué cambios introduce al proyecto.

* *Sistema de usuarios*: Cada *commit* puede estar asociado a un usuario que lo crea, de forma tal de saber quién es el responsable de los cambios en el proyecto.

Los sistemas de versionado suelen utilizarse con archivos de texto, debido a que utilizan herramientas como *diff* que les permite ver linea a linea qué cambios se introducen, entre otras facilidades que veremos más adelante.

Esto no significa que los sistemas de versionado no puedan usarse con archivos binarios, sólo que no se explotará el máximo potencial de la herramienta.

## ¿Qué es git?

**Git** es un *sistema de control de versionado* creado por Linus Torvalds en el 2005.

### Algunas características de git

* *Es distribuido*: A diferencia de sistemas de versionado *centralizados* como *SVN*, en donde requerimos un servidor a dónde subir nuestros cambios, en git cada directorio de trabajo es un repositorio en si.

* *Almacena cambios, no estados*: Cada *commit* en git no es una foto del archivo versionado, sino que es un conjunto de cambios. Por ejemplo, un commit puede decir que agregué una linea con el texto "hola" en la linea 20 de un archivo de texto, y que eliminé la linea 10 del mismo.

* *Permite un desarrollo no lineal*: No es necesario seguir una linea única de trabajo. Git permite que, desde un mismo commit, puedan originarse varias lineas de trabajo paralelas, realizar operaciones entre ellas, y unirlas en un proceso que se suele conocer como *merge*.

## Hola mundo en Git

Nuestro primer paso en git va a ser crear un repositorio local nuevo.
Para esto utilizaremos el comando `git init` sobre un directorio vacío.

Notar que al ejecutarlo se crea una carpeta oculta `.git`.
Nuestro directorio se convierte ahora en un *directorio de trabajo*, y el directorio *.git* en el repositorio local.

### Agregando un archivo a nuestro repositorio local

Primero creamos un archivo de texto *hola.md* y le agregamos el clásico texto *Hola mundo*.

Para ver el estado de nuestra área de trabajo, ejecutamos `git status`

Nuestro archivo *hola.md* es nuevo, por lo que aparece como **untracked file**.
Como indica la salida por consola, debemos ejecutar `git add` para alistar un archivo para un commit. `git add` puede recibir una lista de archivos o incluso una carpeta que contenga varios archivos a actualizar.

El proceso de commit tiene dos etapas en git: los cambios que no vamos a guardar se encuentran en el directorio de trabajo, también conocido como **working dir**. Cuando ejecutamos `git add`, se copian a lo que se conoce como **stage**

Luego de agregarlo con `git add`, ejecutamos `git status` para corroborar que se encuentra en el *stage*

Confirmada nuestra acción, ejecutamos `git commit` para realizar nuestro primer commit. Se nos abre un editor de texto que nos pide agregar un mensaje.
Se sugiere utilizar un mensaje corto y descriptivo. Hay [artículos en internet](https://chris.beams.io/posts/git-commit) sobre las buenas prácticas en mensajes de git.

Escribimos el mensaje, salimos del editor, y al salir nos indica los cambios efectuados con el siguiente formato:

    [<idBranch> <hashCommit>] <mensaje>

* *idBranch* es la rama de trabajo
* *hashCommit* es el identificador único del commit
* *mensaje* es el mensaje que hayamos escrito en el editor

¡Ya hicimos nuestro primer commit! Nuestra primera versión de *hola.md* ya está almacenada.

Para ver nuestro registro de commits, ejecutamos `git log`.

## Operaciones básicas

### Agregando cambios a un archivo existente

Ahora que tenemos una versión base de *hola.md*, agregamos nuestro primer cambio. Con un editor de texto agregamos unas lineas al archivo.

Ejecutamos `git status` para ver la situación de nuestro directorio de trabajo.
Como se puede ver, *hola.md* ahora figura como archivo modificado.
Para ver qué modificaciones se van a subir al *stage*, ejecutamos `git diff`.

La salida nos muestra, precedidos con el caracter "+" las lineas nuevas, y con el caracter "-" las lineas eliminadas.

Agregamos con `git add`, hacemos `git commit` y registramos nuestros cambios.

#### Deshacer subida al stage

Si se agregó un archivo o un cambio al stage y se quiere deshacer, hay dos formas de revertir esta acción:

* `git reset <nombre-archivo>`

* `git rm --cached <nombre-archivo>`

#### Eliminar un archivo

Para eliminar un archivo del area de trabajo y del repositorio, podemos hacer `git rm <nombre-archivo>`

También, si eliminamos el archivo por fuera de git, y queremos notificar esta acción, podemos hacer `git add <nombre-archivo>`

#### Recuperar un archivo eliminado

Para recuperar un archivo, ejecutar `git checkout <nombre-archivo>`

#### Agregar TODOS los cambios al repo

Se puede utilizar `git add -A` para agregar todos los cambios al stage

### Revisando el historial de cambios

No solo `git log` nos permite ver a través de los cambios en nuestro repositorio, `git whatchanged` nos brinda información resumida de los archivos que cambiaron. Ambas opciones **aceptan flags** para agregar o disminuir la información mostrada, como por ejemplo `--stat`

Para ver en detalle qué cambios hubo en un **determinado commit**, se puede ejecutar `git show <hash-commit>`.

**show** es una herramienta poderosísima en git, nos permite ver, por ejemplo, el estado de un archivo en determinado commit si le pasamos el hash del mismo como parámetro. 
Notar que este hash se puede obtener con *whatchanged*

### Moviéndose a través de versiones

Para navegar entre las distintas versiones de nuestra area de trabajo, usamos `git checkout`.

git checkout nos permite navegar entre distintos commits mientras no tengamos archivos modificados sin commitear.

#### Acerca de commits y branches

Una linea de trabajo está formada por varios commits. Cada linea de trabajo es representada por lo que se conoce como **branch**. Un *branch* es un puntero que indica cuál es el último commit de mi linea de trabajo.
Por defecto se crea un puntero llamado *master*, que convencionalmente apunta a la rama principal de desarrollo.

Al hacer *checkout*, lo que hacemos es movernos a otro commit que puede estar en cualquier linea de trabajo. Si no está al final de una linea, se dice que está **detached**, y no se puede hacer commit desde ahí (para hacerlo es necesario crear otro puntero, es decir, un **branch**, pero eso ya es más avanzado).

Para salir de un estado *detached*, se debe hacer checkout de uno de los punteros "branch", por ejemplo, haciendo `git checkout master`.

### Stash

El **stash** es un repositorio temporal, donde uno puede hacer algo similar a un commit, pero con forma de pila y, al igual que el stash, local y temporal.

`git stash` nos sirve cuando necesitamos tener el area de trabajo limpia pero no queremos hacer commit aun.

`git stash` se usa para apilar cambios, y `git stash pop` para desapilarlos.


## Repositorios remotos

Git es una herramienta para trabajar de forma colaborativa. Dicho esto, necesitamos que nuestro repositorio pueda comunicarse con otros repositorios para trabajar en equipo.

### Repositorios "en la nube"

Existen varios servidores de git gratuitos, como github, gitlab, bitbucket, etc.
Estos servidores requieren registrarse en el sistema, y luego, mediante interfaz web, permite crear un repositorio. Al momento de crearlo nos da la opción de utilizarlo como base para un proyecto nuevo nuestro, o de utilizar un repositorio local existente como base.

#### Repositorio demo

Para esta demo, crearemos un servidor local, utilizando el comando `git init --bare` sobre una carpeta nueva, por ejemplo "repo"

Al ejecutar ese comando, notamos como el contenido de nuestra carpeta repo se asemeja al de una carpeta *.git*

### Clonar un repositorio externo

Para utilizar un **repositorio remoto** como base, y poder trabajar con él, tenemos que **clonarlo**

El comando para clonarlo es `git clone <url> [nombre-destino]`

Al clonar un repositorio, nos **copia todos los commits** y el estado actual del proyecto. Si escribimos `git remote -v` podemos ver que se creó una referencia externa llamada *origin*

#### Utilizar un repositorio existente como base para un externo

Si ya tenemos un repositorio local y queremos inicializar un repositorio externo, primero tenemos que configurarlo

Ejecutamos `git remote add <nombre-remoto> <url>` para agregar una referencia a un servidor remoto.

### Sincronización de repositorios remotos

Para sincronizar repositorios hay 2 operaciones:

`git push`: carga los commits locales nuevos en el repositorio remoto

`git pull`: descarga commits nuevos del repositorio remoto