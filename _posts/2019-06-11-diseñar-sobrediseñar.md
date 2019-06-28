---
layout: post
title: Diseñar y sobrediseñar
description: Algunos errores muy comunes a la hora de diseñar
tags: blog programación diseño
---

Como programador, estudiante y docente, tuve mucho contacto con código ajeno. Algunas veces era código heredado (por ejemplo en el trabajo), otras era código escrito en conjunto con compañeros del trabajo / facultad, otras fueron trabajos de alumnos que debía corregir, e incluso código propio tan antiguo que parecía escrito por otra persona.

Leer código ajeno puede ser tan sencillo y tan complejo como leer un cuento. **Un código "bien" escrito es de fácil seguimiento y se entiende claramente sus intenciones**, mientras que uno "mal" escrito puede ser todo lo contrario.

Pero ¿Qué se entiende por *bien* y *mal*  escrito? Cómo en cualquier arte, esto puede ser algo subjetivo y puede variar en el tiempo.
Así como en sus inicios Van Gogh era un mal artista (o al menos eso se dice en internet), hoy, un código ultra performante en C nos puede parecer de mal gusto, pese a que 30 años atrás era excelente por su eficiencia en el uso de recursos.

En este post nos vamos a centrar en un problema frecuente a la hora de programar: diseñar nuestro código.

# Diseñar de afuera hacia adentro 

Un grave, muy grave error a la hora de diseñar software es comenzar por sus partes en vez de realizando un diseño general. Esto es más evidente aun cuando queremos utilizar técnicas como *Test Driven Development*, en las que, nos concentramos tanto en las pruebas unitarias, que dejamos de pensar en el sistema como un todo.

El diseño del código debe comenzar siempre por la capa visible de nuestra aplicación/servicio/biblioteca/*loquesea*. Para esto nos tenemos que concentrar en los casos de uso de nuestro código. **¿Cómo queremos llamar a nuestra lógica?** 

Un ejemplo con el que me topo constantemente es el diseño de sockets. La *API* de sockets de C tiene varias etapas, que dividimos según sus funciones principales. En el caso del servidor, tenemos los siguientes pasos.

* Iniciar el socket (`socket()`)
* Iniciar la estructura que posee la información de la conexión (`getaddrinfo()`)
* Reservar el puerto de escucha (`bind()`) e inicializar la cola de clientes (`listen()`)
* Aceptar un cliente(`accept()`)

_En el caso de ser un socket cliente, los últimos 2 pasos se cambian por el connect_

Sin embargo, generalmente el usuario llama a todos pasos juntos. La mayoría de las veces, **la necesidad del usuarios es mucho más acotada**, pudiendo ser tan básica como querer iniciar un socket servidor con un puerto al cuál escuchar, y un socket cliente con un puerto al cual conectarse.

El usuario puede querer hacer uso del siguiente código:

~~~{.cpp}
// Socket que escucha conexiones
TcpSocketListener acceptor("8080");
// Cliente conectado
TcpSocket client = acceptor.accept();
~~~

O del lado del cliente

~~~{.cpp}
// Socket que se quiere conectar a un cliente
TcpSocket server("172.17.0.2", "8080");
~~~

Es muy recomendable plantearse los casos de uso de una pieza de software antes de empezar a desarrollar la misma.

Esta recomendación es independiente del lenguaje sobre el que se trabaja. Obviamente algunos lenguajes facilitan esta práctica más que otros. Esto puede ser mediante el uso de *stubs* (código sustituto de prueba, por ejemplo `int getTemperatura() {return 42;}`), macros, etc.

## Top-down, bottom-up

Existen dos enfoques de desarrollo de software

* **Top-Down**: Comienza a desarrollar desde el punto de entrada principal de nuestra aplicación (la función `main` o sus equivalentes). Tiene la ventaja de que 

* **Bottom-up**: Comienza a desarrollar desde los módulos que componen la aplicación. Tiene la ventaja de que se pueden escribir las pruebas unitarias rápidamente, por lo que podemos usar técnicas de desarrollo como TDD para darle más robustes a nuestro código. Tiene la desventaja de que a veces programamos piezas que no sabemos para qué sirven. 
