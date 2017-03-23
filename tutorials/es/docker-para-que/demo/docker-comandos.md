# Crear containers

## Demo versiones

*Carpeta 00-java*

En esta demo se arma una aplicación sencilla que emite *hola mundo* más el número de versión.

### Descargar imágenes

*Docker pull* descarga la imagen desde hub.docker.io

	docker pull openjdk:7-jre

	docker pull openjdk:9-jre

### Compilar

**NOTA** Asumo que el host tiene openjdk para compilar java.

**TODO**: compilar desde un container docker :)

	javac -source 1.7 -target 1.7 -Xlint:-options Demo.java

### Ejecutar

* *-v* monta la carpeta actual (asumo que está sobre 00-java, con el código fuente compilado) en /opt/demo del container

* *-ti* inicia el container como un bash interactivo, según qué versión de java se quiere correr, ejecutar uno de los siguientes:

* *--rm* marca al container como volatil, de manera que, cuando se termine la ejecución, se elimine automáticamente.

Notar que, por simplicidad de código se está usando *docker run* en vez de *docker create* más *docker start*.

	docker run --rm -ti -v $PWD:/opt/demo openjdk:7-jre

	docker run --rm -ti -v $PWD:/opt/demo openjdk:9-jre

Iniciado el container correr:

	cd /opt/demo

	java Demo

## Demo json-server

*Carpeta 00b-json-server*

En esta demo se levantan multiples servidores, para mostrar como cada uno maneja su propia interfaz de red

*json-server* es una aplicación en javascript (o sea, corre sobre node) con la que se inicia una api rest que responde al formato de un archivo json

* *-d* Es un flag que indica que el container correrá en segundo plano, es decir *detached*

* *--name* le da un nombre al container, para ubicarlo más fácilmente.

	docker run -d --rm --name server-00 -v $PWD/db0.json:/data/db.json clue/json-server

	docker run -d --rm --name server-01 -v $PWD/db1.json:/data/db.json clue/json-server

Notar que clue/json-server no lo *pulleamos* con anticipación, en caso de no existir pero docker automáticamente lo va a buscar al registro.

Para saber las ips de los contenedores, ejecutar *docker inspect <nombre>*, y buscar en el json NetworkSettings->Networks->bridge->IPAddress

Obtenida la ip, acceder a ella mediante un browser, se puede utilizar como una api rest comun y corriente.

Recordar parar los containers con *docker stop <nombre>*

## Demo imagen custom

*Carpeta 01-java-custom*

En este ejemplo se muestra como enlatar una aplicación construyendo una imagen propia, simplificando las tareas de la demo 00

	docker build -t java-demo .

## Demo wordpress

*No requiere archivos*

En este ejemplo se crea un container de mariadb (clon mysql) y de wordpress, con las imágenes oficiales. Se las vincula mediante *--link*, y se muestra como pasar variables de entorno desde

    docker create --name demo-maria -e MYSQL_ROOT_PASSWORD=pony mariadb

    docker create --name demo-wordpress --link demo-maria:mysql -p 8080:80 wordpress

Iniciar las imagenes con docker start, y entrar a localhost:8080

## Demo compose

*Carpeta 02-compose*

Nota: la versión que trae ubuntu es viejísima, bajar desde el sitio oficial, para tener soporte de compose.yml v2

Simplemente ejecutar

	docker-compose up

### Inspeccionar la base de datos

Si se está usando compose, primero listar las redes disponibles con

	docker network list

Suponiendo que la red es 02compose_default

	docker run -it --rm --network=02compose_default mariadb mysql -hmaria -p 

* --network es para unirnos a la red de compose (por defecto se una la red "default")

* -h*maria* funciona porque existe el container maria en la red 02compose_default. MAGIA PURA
