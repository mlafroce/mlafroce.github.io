# Latex

Latex es un lenguaje bastante complejo, pero muy utilizado en el ámbito profesional para la redacción de artículos, publicaciones científicas, libros, etc. 

## Presentación del lenguaje

El lenguaje se basa fuertemente en *comandos*, del formato *\comando{}*, o encerrado en bloques *\begin{comando}* ... *\end{comando}*.
Permite programar *macros* que son como porciones de código que se copian cuando son llamados.

### Hola mundo en latex

El siguiente código se utiliza para 

~~~ {.latex}

\documentclass{article}
\title{FLISoL Berazategui 2017}
\author{Matías Lafroce}
\date{22 de abril del 2017}
\begin{document}
   \maketitle
   Hola FLISoL
\end{document}

~~~

El formato se puede ver que es muy verboso, y a grosso modo indica lo siguiente:

* *documentclass*: Define que el archivo será un artículo

* *title*: Define el título principal

* *date*: Formato de fecha

* *bloque document*: documento principal

* *maketitle*: pega el título

