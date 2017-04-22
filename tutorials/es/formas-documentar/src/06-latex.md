# Latex

Latex es un lenguaje bastante complejo, pero muy utilizado en el ámbito profesional para la redacción de artículos, publicaciones científicas, libros, etc. 

## Presentación del lenguaje

El lenguaje se basa fuertemente en *comandos*, del formato *\comando{}*, o encerrado en bloques *\begin{comando}* ... *\end{comando}*.
Permite programar *macros* que son como porciones de código que se copian cuando son llamados.

### Hola mundo en latex

El siguiente código se utiliza para 

~~~ {.latex}

\documentclass{article}
\usepackage[utf8]{inputenc} % Especifica la codificación de caracteres de los documentos.
\usepackage[spanish]{babel} % Indica que el documento se escribirá en español.
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

Latex está armado con la filosofía **WYCIWYG** que en humano es *Lo que compilás es lo que obtenés*. El código de hola mundo se verá igual sea cual sea la máquina, el sistema operativo, entorno, etc sobre el que está corriendo el compilador.

### Paquete matemático

Una de las características más llamativas de Latex son los paquetes de extensiones. Y una de sus extensiones más importantes es la de símbolos matemáticos, *amsmath*.

Amsmath tiene todo lo que el matemático (o el que sufre la matemática) puede necesitar, símbolos griegos, tipografías, operadores, alineación de ecuaciones, etc.

Ejemplo

f(x,\lambda) = \lambda e^{- \lambda x}

~~~ {.latex}

\documentclass{article}

\usepackage[utf8]{inputenc} % Especifica la codificación de caracteres de los documentos.
\usepackage[spanish]{babel} % Indica que el documento se escribirá en español.
\usepackage{amssymb, amsmath} % Paquete matemático

\title{FLISoL Berazategui 2017}

\author{Matías Lafroce}

\date{22 de abril del 2017}

\begin{document}

   \maketitle

   \newpage

   \tableofcontents

   \newpage
   
   \section{Ecuaciones}
   \(f(x,\lambda) = \lambda e^{- \lambda x}\)
\end{document}

~~~
