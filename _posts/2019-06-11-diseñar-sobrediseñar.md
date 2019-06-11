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

Supongamos que 

