# Comandos

Resumen de los comandos utilizados en la demo

## Repositorio local

### Crear repositorio nuevo

~~~{.bash}
mkdir repoTest
cd repoTest
git init
~~~

### Ver el estado del directorio de trabajo

~~~{.bash}
git status
~~~

### Agregar archivo al stage

Requiere que exista un archivo *hola.md*

~~~{.bash}
git add hola.md
~~~

### Hacer un commit

~~~{.bash}
git commit
~~~

### Ver registro de commits

~~~{.bash}
git log
~~~

### Ver cambios en el area de trabajo

Requiere que los archivos hayan sido versionados previamente, ignora cambios en el stage.

~~~{.bash}
git diff
~~~

#### Cambios listos para el commit

La opción `--cached` indica que hay que comparar los archivos del stage con el repositorio.

~~~{.bash}
git diff --cached
~~~

### Eliminar archivos del repositorio

Elimina del directorio de trabajo y notifica al stage

~~~{.bash}
git rm <nombre-archivo>
~~~

`git add` también sirve para notificar eliminaciones.


## Navegación por el repositorio

### Visualizar historial de cambios

~~~{.bash}
git whatchanged
git whatchanged --stat
~~~

### Visualizar detalle de cambios en un commit

~~~{.bash}
git show <hash-commit>
~~~

### Visualizar estado de un archivo en determinado commit

~~~{.bash}
git whatchanged 
git show <hash-archivo>
~~~


## Repositorios remotos

### Crear repositorio nuevo

mkdir repo
git init --bare

### Clonar repositorio (servidor local)

~~~{.bash}
git clone file://matias@localhost:/home/matias/intro-git/repo hola-git-2
~~~

### Agregar referencias a repositorio remoto

Desde un repositorio ya existente ejecutar

~~~{.bash}
git remote add origin file://matias@localhost:/home/matias/intro-git/repo
~~~

### Sincronizar repositorios

Para subir commits

~~~{.bash}
git push origin master
~~~

Para descargarlos

~~~{.bash}
git pull
~~~