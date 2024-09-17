'''
EXPRESIONES REGULARES EN EL PUNTO 3

re.match(r'^(F|M|NB)$', genero_heroe):

r antes de la cadena de texto indica que es una cadena cruda (raw string) para evitar el escape de caracteres especiales.
^ y $ son anclajes que aseguran que la expresión regular coincida con toda la cadena y no solo una parte de ella.
(F|M|NB) es una clase de caracteres que coincide con una sola letra, que debe ser "F" o "M". 
Esto valida que genero_heroe sea una cadena que contiene solo una de estas letras.


re.match(r'^\d+$', str(id_heroe)):
r antes de la cadena de texto indica que es una cadena cruda.
^ y $ son anclajes, al igual que en la expresión anterior.
\d es un atajo para cualquier dígito (0-9).
+ indica que el dígito debe aparecer al menos una vez, 
lo que significa que id_heroe debe ser una cadena que contenga al menos un dígito.






PUNTO 4
 la expresión regular r'\b\w+\b' se descompone de la siguiente manera:

\b: Este es un delimitador de palabra. Significa "inicio de una palabra" o "fin de una palabra". 
Marca el límite entre una palabra y lo que la rodea. ayuda a dividir las palabras.

\w+: Esto coincide con uno o más caracteres de palabra. Los caracteres de palabra son letras 
(mayúsculas y minúsculas) y dígitos numéricos. 
Por lo tanto, \w+ encuentra cualquier secuencia de letras y números.

\b: Nuevamente, este delimitador de palabra marca el final de la palabra.

'''