# Introducción a QT5

## Instalación

Instalar los siguientes paquetes

~~~{.bashrc}
cmake
qt5-default
~~~

### Ejecutar en docker

Para armar la imagen ejecutar

~~~{.bashrc}
docker build --tag qt5-sandbox
~~~

Luego de que se hayan instalado los paquetes correspondientes y compilado la aplicación, crear un contenedor ejecutando

~~~{.bashrc}
docker create -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix \
    --name qt5-demo qt5-sandbox
~~~

La variable display y el volumen montados son necesarios para acceder a la interfaz gráfica desde el container.

Acto seguido ejecutar el container creado con el comando

~~~{.bashrc}
docker run qt5-demo ej<N>
~~~

Donde N es el número de ejemplo a ejecutar

Para ver los ejemplos haga click [aqui](doc/ejemplos.md)