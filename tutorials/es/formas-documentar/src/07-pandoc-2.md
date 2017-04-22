# Pandoc revisitado

Para darle cierre a la muestra, vamos a combinar varias de las herramientas vistas para generar documentos de alta calidad

## Markdown + Latex

Pandoc nos permite nos permite mezclar insertar marcas de lenguajes dentro de markdown.
Por ejemplo

~~~ {.markup}
# Seccion 1

## Subseccion

Texto texto
![imagen](imagen.png)

\newpage

Más texto

$f(x,\lambda) = \lambda e^{- \lambda x}$

## Otra subseccion

Texto de otra subseccion

# Seccion 2
~~~

Esto genera código latex que puede ser includo muy fácilmente.

~~~ {.bash}
pandoc archivo.md -o archivo.tex
~~~

### Incluir subsecciones

Latex posee la directiva *\include*, para tomar el contenido de un archivo tex y pegárselo.

Por ejemplo, podemos tener un archivo *principal* donde diseñamos la carátula, y en una sección del cuerpo escribimos la siguientes lineas:

*Principal.tex*:

~~~ {.latex}
\begin{document}
\include{archivo}
\end{document}
~~~

Por consola escribimos

~~~ {.bash}
pandoc archivo.md -o archivo.tex
pdflatex principal.tex
~~~
