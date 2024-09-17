import json
import re
import csv
import os


def sanitizar_string(valor_str: str)->str:
    '''
    Analiza el string recibido y determina si es solo texto (sin números).
    Quita los espacios en blanco de atras y adelante de ambos parámetros en 
    caso que los tuviese.
    parametros: 
        - valor_str: string que representa el texto a validar
    retornos:
        - “N/A”: En caso de encontrarse números.
        - valor_str: En caso que se verifique que el parámetro recibido es solo texto, se
        retorna el mismo convertido todo a minúsculas.
    '''
    valor_str = valor_str.strip()
    if re.search(r'\d', valor_str):#"Si hay algun caracter en valor_str que es número, entonces..."
        return -1
    return(valor_str.lower())


def leer_archivo(nombre_archivo:str)->list:
    '''
    Abre, lee y cierra un archivo JSON en modo lectura y retorna una lista de diccionarios.
    Parámetros:
        - nombre_archivo (str): El nombre y extensión del archivo JSON a leer.
    Retorna:
        - list: Una lista de diccionarios que representan a los héroes del archivo JSON.
    '''
    lista= []
    with open(nombre_archivo,"r") as archivo:
        dic_json = json.load(archivo)
        if "heroes" in dic_json:
            lista = dic_json["heroes"]
    return lista

def guardar_archivo(nombre_archivo: str, contenido: str) -> bool:
    '''
    Guarda contenido en un archivo con el nombre especificado y retorna True si se guarda con éxito.
    Parámetros:
        - nombre_archivo (str): El nombre del archivo en el que se guardará el contenido.
        - contenido (str): El contenido a guardar en el archivo.
    Returns:
        - bool: True si se guarda el archivo con éxito, False si ocurre un error al intentar guardarlo.
    '''
    with open(nombre_archivo, 'w+') as archivo:
        archivo.writelines(contenido)

    if os.path.exists(nombre_archivo):
        print(f"\n • Se creó el archivo: {nombre_archivo}")
        return True
    else:
        print(f"\n • Error al crear el archivo: {nombre_archivo}")
        return False
    

def validar_datos_dicc(dicc: dict,key:str)->str:
    '''
    Valida si un diccionario no esta vacio y contiene una clave.
    Parámetros:
        - dicc_heroe (dict): El diccionario que representa a un héroe.
        - key (str): La clave que se debe validar.
    Retorno:
        - bool: True si el diccionario no está vacío y contiene la clave, False en caso contrario.
    '''
    if not dicc or key not in dicc:  #valida que dic no este vacio y key se encuentre en las keys
        return False
    return True




def capitalizar_palabras(string: str)-> str:
    '''
    Convierte en mayuscula la primer letra de todas las palabras en una cadena si es válida.
    Parámetros:
        - string (str): La cadena de texto que se desea capitalizar (pasar a mayuscula).
    Returns:
        - str: La cadena con las palabras capitalizadas si es válida, o una cadena vacía si no es válida.
    '''
    if sanitizar_string(string):
        return string.title()



def obtener_lista_de_tipos(lista: list, key: str):
    '''
    Obtiene una lista de las variedades del tipo de dato pasado por parámetro en la lista de héroes.
    Parámetros:
        - lista (list): La lista de héroes de la cual se desea obtener las variedades del tipo de dato.
        - tipo_dato (str): El nombre del tipo de dato (por ejemplo, "color_pelo", "color_ojos").
    Retorna:
        - set: Un conjunto de las variedades del tipo de dato con la primera letra en mayúscula.
    '''
    variedades = set()
    for elemento in lista:
        valor = elemento.get(key, 'N/A')  #accede a un valor de a una clave. Si no existe, se guarda como 'N/A'
        valor = valor.strip()  # Elimina espacios en blanco al inicio y al final
        valor = capitalizar_palabras(valor)
        if not valor:
            valor = 'N/A'
        variedades.add(valor)  # Agrega las variedades capitalizadas a la lista
    
    return variedades
        
    
def normalizar_dato(dato: str, valor_default: str):
    '''
    Normaliza un dato de héroe, reemplazándolo con el valor por defecto si está vacío.
    Parámetros:
        - dato (str): El valor del dato de héroe.
        - valor_default (str): El valor por defecto a colocar en caso de que el dato esté vacío.
    Retorna:
        - str: El dato normalizado, con el valor por defecto si el dato está vacío.
    '''
    if not dato.strip(): # Elimina espacios en blanco al inicio y al final
        return valor_default
    return dato
    
    
def normalizar_heroe(dicc:dict,key:str):
    '''
    Normaliza y capitaliza un valor específico de un héroe, utilizando la función 'normalizar_dato'.
    Parámetros:
        - dicc (dict): El diccionario que representa un héroe.
        - key (str): La clave que se desea normalizar y capitalizar en el diccionario.
    Retorna:
        - dict: El diccionario del héroe con la clave especificada normalizada y capitalizada.

    '''
    # Normalizar y capitalizar el valor de la key especificada.
    if validar_datos_dicc(dicc,key) and isinstance(dicc[key],str):
        dicc[key] = capitalizar_palabras(normalizar_dato(dicc[key], 'N/A'))
    return True
    

def obtener_heroes_por_tipo(lista:list, variedades:set, key:str):
    '''
    Filtra y organiza los héroes según un conjunto de tipos/variedades y el tipo de dato a evaluar.
    Parámetros:
        - lista (list): La lista de héroes representados como diccionarios.
        - variedades (set): Un conjunto de tipos/variedades (por ejemplo, colores de ojos, colores de pelo, etc.).
        - key(str): El tipo de dato a evaluar en los héroes (la clave en cuestión, como color_ojos, color_pelo, etc.).
    Retorna:
        - dict: Un diccionario con cada variedad como key y una lista de nombres de héroes como valor.
    '''
    # Crea un diccionario para almacenar los héroes por tipo/variedad.
    filtrados_por_tipo = {}

    # Itera sobre el conjunto de tipos/variedades.
    for variedad in variedades:
        # Inicializa una lista vacía para los héroes de esta variedad.
        heroes_de_variedad = []

        # Itera sobre la lista de héroes.
        for elemento in lista:
            # Normaliza el valor del tipo de dato.
            normalizar_heroe(elemento, key)

            # Verifica si el valor normalizado coincide con la variedad actual.
            if elemento[key] == variedad:
                heroes_de_variedad.append(elemento["nombre"])

        # Agrega la lista de héroes de esta variedad al diccionario.
        filtrados_por_tipo[capitalizar_palabras(variedad)] = heroes_de_variedad

    return filtrados_por_tipo


def guardar_heroes_por_tipo(dicc:dict, key:str):
    '''
    Guarda en archivos CSV la lista de héroes agrupados por tipo y variedad.
    Parámetros:
        - heroes_por_tipo (dict): Un diccionario que contiene héroes agrupados por tipo y variedad.
        - key (str): El tipo de dato (clave) por el cual se han agrupado los héroes.
    Retorna:
        - bool: True si la operación de guardado es exitosa, False si hay algún error.
    '''
    exito = True  # Inicializa una bandera para registrar el éxito o fracaso de la operación

    contenido_lista = []  # Inicializa una lista para contener el contenido a escribir en el archivo

    for clave, valor in dicc.items():
        mensaje = f"Caracteristica: {key} {clave}: {', '.join(valor)}"  # Convertimos la lista de nombres a una cadena
        contenido_lista.append(mensaje)

    nombre_archivo = f"heroes_segun_{key}.csv"

    # Verifica si se pudo guardar el archivo
    if not guardar_archivo(nombre_archivo, '\n'.join(contenido_lista)):
        print(f"Error al guardar el archivo para {clave}.")
        exito = False  # Cambia la bandera a False en caso de error

    return exito  # Devuelve la bandera que registra el éxito o fracaso de la operación




def stark_listar_heroes_por_dato(lista:list, key:str):
    '''
    Organiza y guarda héroes por un tipo de dato específico.
    Parámetros:
        - heroes (list): La lista de héroes representados como diccionarios.
        - key (str): El tipo de dato (clave) por el cual se agruparán y guardarán los héroes.
    Retorna:
        - bool: True si la operación de agrupamiento y guardado es exitosa, False si hay algún error.
    '''
    exito = True  # Inicializa una bandera para registrar el éxito o fracaso de la operación

    # A. Obtener la lista de tipos (variedades) del tipo de dato.
    tipos_variedades = obtener_lista_de_tipos(lista, key)

    # B. Obtener un diccionario que agrupa los héroes por tipo y variedad.
    heroes_por_tipo = obtener_heroes_por_tipo(lista, tipos_variedades, key)
    print(f"\n • Heroes agrupados segun su {key}:")
    for clave,valor in heroes_por_tipo.items():
        print (f"\n{clave}: {', '.join(valor)}")
    # C. Guardar el archivo CSV con los héroes agrupados por tipo y variedad.
    if not guardar_heroes_por_tipo(heroes_por_tipo, key):
        print(f"Error al listar héroes por dato.")
        exito = False  # Cambia la bandera a False en caso de error

    return exito  # Devuelve la bandera que registra el éxito o fracaso de la operación



lista_juegos = leer_archivo("CUATRI2\T_P_Stark\TP5\data_stark_2.json")
copia_lista_juegos = lista_juegos.copy()


'''
for dicc in copia_lista_juegos:
    normalizar_heroe(dicc,"inteligencia")




variedades = (obtener_lista_de_tipos(copia_lista_juegos,"inteligencia"))
print(variedades)
filtros = obtener_heroes_por_tipo(copia_lista_juegos,variedades,"inteligencia")
for clave,valor in filtros.items():
    print(clave,valor,"\n")'''

stark_listar_heroes_por_dato(copia_lista_juegos,"color_ojos")