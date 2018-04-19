# Consulta de SERVADDO

Script de *python* para realizar búsquedas en el listado oficial, especialmente útil cuando el portal web del ABC está caido o no responde.
Mediante este *script* puede realizar búsquedas y descargar el resultado en formato *CSV*, para luego abrirlo con alguna aplicación de hojas de cálculo (como el *libre office calc* o *excel*)

## Requerimientos

Requiere python3. La versión 3.6 puede ser descargado de [acá](https://www.python.org/downloads/)

## Instrucciones

Descargue el script *servaddo.py* y ejecutelo con su interprete de python.
Desde un entorno Linux esto se realiza escribiendo en una consola
`python3 servaddo.py`

El script le preguntará sobre qué listado desea buscar. Ingrese uno de los códigos disponibles
(al momento solo pude corroborar la existencia del código *108b* y *fl2* para FINES)

Luego ingresa los criterios de búsqueda, al igual que la versión web.

Una vez ingresado el/los criterios de búsqueda, presione enter para iniciar la descarga.

Finalmente ingrese un nombre para el archivo de salida, que será guardado en formato **csv**

## IMPORTANTE

Para no saturar el servidor, se ha limitado la búsqueda a 2000 registros, de ser necesario, modifique el script en la linea marcada para este fin.


## Licencia

Se concede permiso, de forma gratuita, a cualquier persona que obtenga una copia de este software y de los archivos de documentación asociados (el "Software"), para utilizar el Software sin restricción, incluyendo sin limitación los derechos a usar, copiar, modificar, fusionar, publicar, distribuir, sublicenciar, y/o vender copias del Software, y a permitir a las personas a las que se les proporcione el Software a hacer lo mismo, sujeto a las siguientes condiciones:

El aviso de copyright anterior y este aviso de permiso se incluirán en todas las copias o partes sustanciales del Software.

EL SOFTWARE SE PROPORCIONA "TAL CUAL", SIN GARANTÍA DE NINGÚN TIPO, EXPRESA O IMPLÍCITA, INCLUYENDO PERO NO LIMITADO A GARANTÍAS DE COMERCIALIZACIÓN, IDONEIDAD PARA UN PROPÓSITO PARTICULAR Y NO INFRACCIÓN. EN NINGÚN CASO LOS AUTORES O TITULARES DEL COPYRIGHT SERÁN RESPONSABLES DE NINGUNA RECLAMACIÓN, DAÑOS U OTRAS RESPONSABILIDADES, YA SEA EN UNA ACCIÓN DE CONTRATO, AGRAVIO O CUALQUIER OTRO MOTIVO, QUE SURJA DE O EN CONEXIÓN CON EL SOFTWARE O EL USO U OTRO TIPO DE ACCIONES EN EL SOFTWARE.
