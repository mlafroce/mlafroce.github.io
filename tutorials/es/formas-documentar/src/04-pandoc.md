# Pandoc

## Uso básico

Pandoc es una herramienta poderosísima que convierte archivos de un formato de texto a otro, como por ejemplo, *.odt* a *.html*, o a *.epub* para readers, o incluso a *.pdf* si tiene uno de los compiladores instalado.

Para utilizarlo simplemente se ejecuta

~~~ {.bash}
pandoc <entrada.ext> -o <salida.ext2>
~~~

Y la aplicación interpreta los formatos de entrada y salida según la extensión.

Por ejemplo

~~~ {.bash}
pandoc hola.md -o hola.odt
~~~

Genera un archivo de libreoffice writer manteniendo la estructura de markdown de entrada.

(Ver ejemplo con este documento)

## Generar archivos independientes y fragmentos

En algunos formatos, como html o Latex, nos da la opción de generar un archivo completo independiente, o sólo un fragmento que pueda ser insertado en otro documento.

Esto puede ser muy útil cuando tenemos un archivo con, por ejemplo, una carátula o un estilo muy elaborado, y nos resulta más cómodo generar el contenido en otro formato.

Para obtener un archivo independiente se agrega la opción *-s*, en caso contrario se genera un fragmento insertable.

~~~ {.bash}
pandoc hola.md -o hola.html
pandoc hola.md -so hola.html
~~~

