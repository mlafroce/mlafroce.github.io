# Demo de SDL

Para compilar es necesario instalar `libsdl2-dev` y `libsdl2-image-dev`. Se recomienda el uso de CMake

## Compilar con CMake

Crear una carpeta vacía (ej: build) e invocar a CMake pasando como argumento el directorio donde está CMakeLists.txt

~~~{.bash}
mkdir build
cd build
cmake ..
make && make install
~~~

## Ejecución

Ejecutar escribiendo `./sdl-demo`


