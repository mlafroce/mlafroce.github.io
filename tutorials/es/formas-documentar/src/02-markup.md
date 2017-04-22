# Lenguajes de markup

El markup es una forma de texto enriquecido basado en marcas para definir la estructura y estilo.

## Diferencias con el texto plano

A diferencia del texto plano, el texto estilizado posee marcas para que una aplicación pueda leerlo y mostrarlo (de ahora en adelante *renderizarlo*) con un formato más amigable.
Por ejemplo, el formato wiki markup, que utilizan los "wikis", posee un formato similar al siguiente

~~~ {.wiki}

= Este es un título =
== Este es un subtítulo ==

Esta es una lista:

* La armo con asteriscos

* Permite sublistas

** Esta es una sublista

También permite '''Resaltar'''

~~~

Cómo se puede ver, el texto sigue siendo legible al ojo humano, pero tiene algunas notaciones para definir el tipo de contenido.
Por supuesto existen editores visuales que nos ayudan a escribir sin tener que conocer el lenguaje, pero eso no nos priva de la posibilidad de usar un editor de texto plano.

(Ver renderizado final en html)

## HTML, el markup de los browsers

Es imposible no mencionar al que seguramente es el lenguaje de markup más conocido en internet: el HTML

HTML es el lenguaje utilizado por los browsers para mostrar páginas web. El formato, en pseudocódigo, es como el siguiente:

~~~ {.html}

<html>
  <cabeza>
    (Datos como el título de la página, estilos, etc)
  </cabeza>
  <cuerpo>
    <texto>Texto de la página</texto>
    <tabla>(marcas para generar tablas)</tabla>
    <texto>Texto de la página</texto>
  </cuerpo>
<html>

~~~

HTML además puede ser estilizado fácilmente mediante otro lenguaje de estilos conocido como CSS.
Una de las ventajas del HTML es que los navegadores modernos permiten renderizaciones muy complejas, pero a la vez, un texto html básico se adapta muy rápido a la pantalla, ya sea de una pc, tablet, celular, reader, etc.

Si bien el formato puede llegar a ser difícil de leer para un usuario no entrenado, hay otros lenguajes más amenos y que se ajustan a las necesidades del usuario, como por ejemplo LaTeX o Markdown, que veremos más adelante.
