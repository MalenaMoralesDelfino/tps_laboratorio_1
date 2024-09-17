import json
import re
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


def validar_lista(lista:list):
    '''
    Verifica si una lista no está vacía.
    Parámetros:
        - lista (list): La lista que se desea validar.
    Retorna:
        - bool: True si la lista tiene elementos, False si la lista está vacía.
    '''
    if not lista: #Valida que la lista no esté vacia
        return False
    return True


def stark_normalizar_datos(lista: list):
    '''
    Normaliza los datos de una lista de héroes, 
    convirtiendo claves numericas a tipos de dato int o float.
    Validaciones:
        - La lista de héroes no debe estar vacía para realizar sus acciones.
    Parámetros:
        - lista_heroes (list): La lista de héroes a ser normalizada.
    Retorno:
        - bool: True si al menos un dato fue normalizado, False en caso contrario.
    '''
    if not hasattr(stark_normalizar_datos, 'datos_ya_normalizados'): #Toma un objeto y devuelve true si tiene ese atributo
        stark_normalizar_datos.datos_ya_normalizados = False

    if validar_lista(lista) and not stark_normalizar_datos.datos_ya_normalizados:
        dicc_clave_tipo ={   'altura':float,
                            'peso':float,
                            'fuerza':int}
        
        datos_normalizados = False  # Bandera para verificar si se realizó alguna modificación

        for elemento in lista:
            for clave,tipo in dicc_clave_tipo.items():
                if clave in elemento and isinstance(elemento[clave], str): # Verifica si la clave existe y si su valor es una str
                    valor_sin_espacios = elemento[clave].strip()
                    # Intentar convertir el valor de la clave al tipo de dato correspondiente
                    elemento[clave] = tipo(valor_sin_espacios)
                    datos_normalizados = True
        # Si se modificaron datos, retornar True
        if datos_normalizados:
            print("\n•Datos normalizados")
            stark_normalizar_datos.datos_ya_normalizados = True
        else:
            print("\n•Hubo un error al normalizar los datos.")
            return False
    else:
        print("\n•Los datos ya han sido normalizados anteriormente.")
        stark_normalizar_datos.datos_ya_normalizados = True
        return True


def preguntar_atributo():
    '''
    Pide al usuario una opcion, valida que correcta y la devuelve.
    Si lo ingresado no es correcto, se repetirá el else hasta que se valide.
    retorno:
        -respuesta: str.
    '''
    opciones_validas = {'a': 'identidad', 
                        'b': 'altura',
                        'c': 'peso', 
                        'd': 'genero',
                        'e': 'color_ojos',
                        'f': 'color_pelo', 
                        'g': 'fuerza',    
                        'h': 'inteligencia'}
    while True:
        respuesta = input("\nDesea ver  los superhéroes filtrados según:\n"
                                "a) La identidad\n"  
                                "b) La altura\n"
                                "c) El peso\n"
                                "d) El genero\n"
                                "e) El color de ojos\n"
                                "f) El color de pelo\n"
                                "g) La fuerza\n"
                                "h) El tipo de inteligencia.  ").lower()
        if respuesta is not False and respuesta in opciones_validas:
            return opciones_validas[respuesta]
        else:
            print("\nError. Debe ingresar una opcion válida: ")


def preguntar_key_numerica()->str:
    '''
    Pide al usuario una clave, valida que sea la opcion correcta y la devuelve.
    Si lo ingresado no es correcto, se repetirá el else hasta que se valide.
    retorno:
        -respuesta: str.
    '''
    while True:
        respuesta = input("\nElija un atributo: 'fuerza', 'peso' o 'altura'? ").lower()
        if respuesta is not False and respuesta in ['fuerza','peso','altura']:
            return(respuesta)
        else:
            print("\nError. Debe ingresar una opcion correcta: ") 


def preguntar_genero()->str:
    '''
    Pide al usuario un género, valida que sea la opcion correcta y la devuelve.
    Si lo ingresado no es correcto, se repetirá el else hasta que se valide.
    retorno:
        -respuesta: str.
    '''
    while True:
        respuesta = input("\nQué tipo de género? No binario ('NB'), femenino ('F') o masculino('M'): ").upper()
        if respuesta is not False and respuesta in ['F','M','NB']:
            return(respuesta)
        else:
            print("\nError. Debe ingresar un caracter válido: ")


def preguntar_extremo()->str:
    '''
    Pide al usuario una extremo, valida que sea la opcion correcta y la devuelve.
    Si lo ingresado no es correcto, se repetirá el else hasta que se valide.
    retorno:
        -respuesta: str.
    '''
    while True:
        respuesta = input("\nDesea ver el maximo o el minimo? ").lower()
        if respuesta is not False and respuesta in ['maximo','minimo']:
            return(respuesta)
        else:
            print("\nError. Debe ingresar una opcion correcta: ")


def preguntar_key_str():
    '''
    Pide al usuario una opcion, valida que correcta y la devuelve.
    Si lo ingresado no es correcto, se repetirá el else hasta que se valide.
    retorno:
        -respuesta: str.
    '''
    opciones_validas = {'a': 'color_ojos',
                        'b': 'color_pelo',
                        'c': 'inteligencia'
                        }
    while True:
        respuesta = input("\nDesea ver  los superhéroes agrupados según:\n"
                                "a) el color de ojos\n"  
                                "b) el color de pelo\n"
                                "c) el tipo de inteligencia.  ").lower()
        if respuesta is not False and respuesta in opciones_validas:
            return opciones_validas[respuesta]
        else:
            print("\nError. Debe ingresar una opcion válida: ")



###########################################################################################################################

def imprimir_menu_desafio_5():
    '''
    Muestra al usuario diferentes opciones.
    '''
    print(  "\n"
            "A) Normalizar datos.\n"
            "B) Mostrar un atributo de cada superhéroe.\n"
            "C) Mostrar y guardar los superhéroes según el género.\n"
            "D) Mostrar y guardar el máximo o mínimo de los héroes segun el atributo.\n"
            "E) Mostrar y guardar el promedio de un atributo numérico de todos los superhéroes.\n"
            "F) Mostrar y guardar la cantidad de superhéroes según un atributo.\n"
            "G) Mostrar y guardar superhéroes según un atributo.\n"
            "Z) Salir.")
    

def stark_menu_principal_desafio_5():
    '''
    Muestra un menú principal, solicita al usuario que ingrese una opción y valida
    que la opción ingresada sea un número entero dentro del rango del 1 al 6. Si la opción no es válida,
    se mostrará un mensaje de error y se repetirá la solicitud hasta que se ingrese una opción válida.
    Retorna:
        - valor (int): La opción válida seleccionada por el usuario.
    '''
    imprimir_menu_desafio_5()
    while True:
        valor = input("Que desea hacer?: ")
        valor =  sanitizar_string(valor)
        if valor not in ['a', 'b', 'c', 'd', 'e','f','g', 'z']:
            print("Error, ingrese una opcion valida (a, b, c, d, e, f, g, z)->  \n")
        else:   
            return valor
        

def stark_marvel_app_3(lista:list):
    '''
    Presenta un menú interactivo al usuario. 
    Dependiendo de la opción seleccionada por el usuario, realiza diversas
    acciones como normalizar datos, mostrar información de héroes, calcular promedios, etc.
    Parámetros:
        - lista (list): La lista que se utilizará en la aplicación.
    '''
    datos_normalizados = False
    while True:
        opcion = stark_menu_principal_desafio_5()
        match opcion:
            case 'a':
                stark_normalizar_datos(lista)
                datos_normalizados = True

            case 'b':
                if datos_normalizados:
                    key=preguntar_atributo()
                    print(f"\n • Superhéroes filtrados según {key}:")
                    for elemento in lista:
                        #for key in elemento.keys():
                        print(f"\n{obtener_nombre_y_dato(elemento, key)}")
                else:
                    print("\n•No se normalizaron los datos.\n")

            case 'c':
                if datos_normalizados:
                    genero = preguntar_genero()
                    stark_guardar_heroe_genero(lista,genero)
                else:
                    print("\n•No se normalizaron los datos.\n")

            case 'd':
                if datos_normalizados:
                    key=preguntar_key_numerica()
                    extremo = preguntar_extremo()
                    genero = preguntar_genero()
                    stark_calcular_imprimir_guardar_heroe_genero(lista,key,genero,extremo)
                else:
                    print("\n•No se normalizaron los datos.\n")

            case 'e':
                if datos_normalizados:
                    key = preguntar_key_numerica()
                    genero = preguntar_genero()
                    stark_calcular_imprimir_guardar_promedio_genero(lista,key,genero)
                else:
                    print("\n•No se normalizaron los datos.\n")
            
            case 'f':
                if datos_normalizados:
                    key = preguntar_key_str()
                    stark_calcular_cantidad_por_tipo(lista,key)
                else:
                    print("\n•No se normalizaron los datos.\n")
                    
            case 'g':
                if datos_normalizados:
                    key = preguntar_key_str()
                    stark_listar_heroes_por_dato(lista,key)
                else:
                    print("\n•No se normalizaron los datos.\n")
                
            case 'z':
                print("\nHasta luego\n")
                break


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


def obtener_nombre_capitalizado(dicc:dict):
    '''
     Obtiene y capitaliza el nombre de un héroe si está presente en el diccionario.
    Parámetros:
        - dicc (dict): El diccionario que representa al héroe.
    Returns:
        - str: El nombre capitalizado del héroe si se encuentra en el diccionario, 
                o un mensaje de error si el nombre no está presente.

    '''
    if validar_datos_dicc(dicc, "nombre"):
        nombre = dicc['nombre']
        nombre_capitalizado = capitalizar_palabras(nombre)
        return f"Nombre: {nombre_capitalizado}"
    else:
        return "Nombre no encontrado en el diccionario del héroe."

 
def obtener_nombre_y_dato(dicc:dict, key: str)->str:
    '''
    Obtiene el nombre y el dato (key) de un héroe y lo formatea en un string.
    Parámetros:
        - dicc_heroe (dict): El diccionario que representa a un héroe.
        - key (str): La clave que representa el dato deseado ('altura', 'fuerza', 'peso', u otro).
    Retorna:
        - str: El nombre del héroe y el dato formateado como "Nombre: Nombre del héroe | dato: Valor del dato".
          Si el diccionario no contiene la clave 'nombre' o la clave especificada no existe, retorna "Error: Datos no disponibles".
    '''
    if validar_datos_dicc(dicc,key):
        nombre = obtener_nombre_capitalizado(dicc)
        valor = dicc[key]
        return (f"{nombre} | {key.capitalize()} = {valor}")



################################################        2       ################################################

def es_genero(dicc: dict, genero:str)->bool:
    '''
    Verifica si un héroe cumple con un género específico.
    Parámetros:
        - dicc (dict): El diccionario que representa al héroe.
        - genero (str): El género a verificar (M, F o NB).
    Returns:
        - bool: True si el héroe cumple con el género especificado, False en caso contrario.
    '''
    if validar_datos_dicc(dicc,"genero"):
        if dicc["genero"] == genero:
            return True
    else:
        return False



def stark_guardar_heroe_genero(lista:list, genero:str):
    '''
    Filtra héroes por género, guarda los nombres en un archivo CSV y retorna True si se guarda con éxito.
    Parámetros:
        - lista (list): La lista de héroes representados como diccionarios.
        - genero (str): El género (M, F o NB) por el cual se desea filtrar a los héroes.
    Returns:
        - bool: True si se guarda el archivo con éxito, False si no se encontraron héroes con el 
        género especificado o si ocurrió un error al guardar el archivo.
    '''
    if validar_lista(lista):
        heroes_filtrados = []
        for heroe in lista:
            if es_genero(heroe, genero):      
                nombre_heroe = obtener_nombre_capitalizado(heroe)
                heroes_filtrados.append(nombre_heroe) 
        
        if not heroes_filtrados:
            print(f" • No se encontraron héroes con el género '{genero}'.")
            return False
        
        print(f"\n  • Heroes genero {genero}:")
        for heroes in heroes_filtrados:
            print("\n",heroes)

        nombre_archivo = f'heroes_{genero}.csv'
        contenido_a_guardar = '\n'.join(heroes_filtrados)
        guardar_archivo(nombre_archivo, contenido_a_guardar)
        return True
    else:
        return False



################################################        3       ################################################

def calcular_min_genero(lista:list, atributo:str, genero:str)->str:
    '''
    Encuentra al héroe con el valor mínimo de un atributo específico, filtrando por género.
    Parámetros:
        - lista (list): La lista de héroes representados como diccionarios.
        - atributo (str): El atributo por el cual se buscará el valor mínimo.
        - genero (str): El género (M, F o NB) por el cual se desea filtrar a los héroes.

    Returns:
        - dict: El diccionario del héroe o heroína con el valor mínimo del atributo especificado y el género deseado.
        - None: Si no se encuentra un héroe o heroína que cumpla con el género especificado o si la lista está vacía.
    '''
    valor_min = None
    heroe_min = None  # Inicializar como None para manejar casos en los que no se encuentra un héroe
    for heroe in lista:
        if es_genero(heroe,genero):  # Filtrar por género
            valor = heroe.get(atributo)
            if valor is not None and (valor_min is None or valor < valor_min):
                valor_min = valor
                heroe_min = heroe

    return heroe_min


def calcular_max_genero(lista:list, atributo:str, genero:str)->str:
    '''
    Encuentra al héroe con el valor maximo de un atributo específico, filtrando por género.
    Parámetros:
        - lista (list): La lista de héroes representados como diccionarios.
        - atributo (str): El atributo por el cual se buscará el valor maximo.
        - genero (str): El género (M, F o NB) por el cual se desea filtrar a los héroes.

    Returns:
        - dict: El diccionario del héroe con el valor maximo del atributo especificado y el género deseado.
        - None: Si no se encuentra un héroe que cumpla con el género especificado o si la lista está vacía.
    '''
    valor_max = None
    heroe_max = None  # Inicializar como None para manejar casos en los que no se encuentra un héroe
    for heroe in lista:
        if es_genero(heroe,genero):  # Filtrar por género
            valor = heroe.get(atributo)
            if valor is not None and (valor_max is None or valor > valor_max):
                valor_max = valor
                heroe_max = heroe

    return heroe_max


def calcular_max_min_dato_genero(lista, atributo, genero, extremo)->dict:
    """
    Encuentra al héroe con el valor máximo o mínimo de un atributo específico, filtrando por género.

    Parámetros:
        - lista (list): La lista de héroes representados como diccionarios.
        - atributo (str): El atributo por el cual se buscará el valor máximo o mínimo.
        - genero (str): El género por el cual se desea filtrar a los héroes.
        - operacion (str): 'maximo' o 'minimo' para indicar si se busca el máximo o mínimo.

    Returns:
        - dict: El diccionario del héroe con el valor máximo o mínimo del atributo especificado y el género deseado.
        - None: Si no se encuentra un héroe que cumpla con el género especificado, si la lista está vacía o 
                si el atributo es inexistente en algún héroe.
    """
    if extremo == 'maximo':
        heroe = calcular_max_genero(lista, atributo, genero)
    elif extremo == 'minimo':
        heroe = calcular_min_genero(lista, atributo, genero)
    else:
        return None  # Operación no válida

    return heroe


def stark_calcular_imprimir_guardar_heroe_genero(lista, atributo, genero, extremo):
    """
    Calcula, imprime y guarda en un archivo CSV el héroe con el valor 
    máximo o mínimo de un atributo específico, filtrando por género.

    Parámetros:
        - lista (list): La lista de héroes representados como diccionarios.
        - atributo (str): El atributo por el cual se buscará el valor máximo o mínimo.
        - genero (str): El género por el cual se desea filtrar a los héroes.
        - operacion (str): 'maximo' o 'minimo' para indicar si se busca el máximo o mínimo.

    Returns:
        - bool: True si pudo guardar el archivo, False en caso contrario.
    """
    if validar_lista(lista):
        heroe = calcular_max_min_dato_genero(lista, atributo, genero, extremo)
        
        if heroe is None:
            print(f"\n • No se encontraron heroes {extremo} de {atributo} en el género '{genero}'.")
            return False
        
        print(f"\n  El héroe {extremo} de {atributo} en el género '{genero}' es: \n")
        print(obtener_nombre_y_dato(heroe, atributo),"\n")

        nombre_archivo = f'heroes_{extremo}_{atributo}_{genero}.csv'
        contenido = (
            f"{capitalizar_palabras(extremo)}\n"
            f"{capitalizar_palabras(atributo)}\n"
            f"{obtener_nombre_y_dato(heroe, atributo)}"
        )
        guardar_archivo(nombre_archivo, contenido)
        
        return True
    else:
        return False



################################################        4       ################################################

def sumar_dato_heroe_genero(lista:list,key:str,genero:str)->float:
    '''
    Recorre la lista de héroes y suma los valores de la característica especificada
    (por ejemplo, fuerza, altura, peso) para los héroes que tienen dicha característica, segun el genero.
    Parámetros:
        - lista (list): La lista de héroes de la cual se desea sumar los valores de la característica.
        - key (str): El nombre de la característica (atributo) que se desea sumar.
        - genero (str): El género por el cual se desea filtrar a los héroes.
    Retorna:
        - acumulador(float): que contiene la suma total de los valores de la característica
        - -1: Si no se encuentran héroes con la característica especificada o si la suma es igual a cero.
    '''
    acumulador = 0
    for elemento in lista:
        if validar_datos_dicc(elemento,key):
                if es_genero(elemento,genero):
                    acumulador += elemento[key]
                
        else:
            return -1
    return (acumulador)


def cantidad_heroes_genero(lista:list, genero:str)->int:
    '''
    Cuenta la cantidad de héroes que coinciden con el género especificado.

    Parámetros:
        - lista (list): La lista de héroes de la cual se desea contar los héroes por género.
        - genero (str): El género por el cual se desea filtrar a los héroes.

    Retorna:
        - contador (int): La cantidad de héroes que coinciden con el género especificado.
        - -1: Si no se cumple con las validaciones.
    '''
    contador = 0

    for elemento in lista:
        if es_genero(elemento,genero):
            contador += 1
    if contador == 0:
        return -1
    else:
        return contador


def dividir(dividendo:float, divisor: float)->float:
    '''
    Toma un dividendo y un divisor como parámetros y realiza la división
    entre ambos. Retorna el resultado de la división.
    Parámetros:
        - dividendo (float): El número que se desea dividir.
        - divisor (float): El número por el cual se desea dividir el dividendo.

    Retorna:
        - float: El resultado de la división.

    '''
    if divisor == 0:
        return False
    resultado = dividendo/divisor
    return resultado


def calcular_promedio_genero(lista:list,key:str,genero:str)->float:
    '''
    Muestra en pantalla el promedio de los valores de la característica especificada
    (por ejemplo, fuerza, altura, peso) para los héroes que tienen dicha característica.

    Parámetros:
        - lista (list): La lista de héroes de la cual se desea mostrar el promedio de los valores de la característica.
        - key (str): El nombre de la característica (atributo) para la cual se desea mostrar el promedio.
    '''
    acumulador = sumar_dato_heroe_genero(lista,key,genero)
    contador = cantidad_heroes_genero(lista,genero)
    promedio = dividir(acumulador,contador)
    return promedio


def stark_calcular_imprimir_guardar_promedio_genero(lista:list,key:str,genero:str):
    '''
    Calcula el promedio de los valores de una característica específica para los héroes de un género dado.
    Imprime en la consola y guarda en un archivo CSV el promedio de los valores de la característica
    para el género especificado.

    Parámetros:
        - lista (list): La lista de héroes representados como diccionarios.
        - key (str): El nombre de la característica (atributo) para la cual se calculará el promedio.
        - genero (str): El género (M o F) por el cual se desea filtrar a los héroes.
    Returns:
        - None: Si la lista de héroes está vacía o si no se encuentran héroes del género especificado.
    '''
    if validar_lista(lista):
        promedio = calcular_promedio_genero(lista, key, genero)
        if promedio <= 0:
            print(f"\n • No se encontraron héroes en el género '{genero}'.")
            return False
        mensaje = f"{key.title()} promedio del genero {genero}: {promedio}.\n"
        print(f"\n {mensaje}")
        nombre_archivo = f'heroes_promedio_{key}_{genero}.csv'
        if guardar_archivo(nombre_archivo, mensaje):
            return True
    else:
        print("Error, lista de héroes vacía")
        return False




################################################        5       ################################################

def calcular_cantidad_tipo(lista:list,key:str)->dict:
    '''
    Calcula la cantidad de elementos por tipo y devuelve un diccionario con los resultados.
    Parámetros:
        - lista (list): La lista de elementos representados como diccionarios.
        - key (str): La clave por la cual se calculará la cantidad de elementos.
    Retorna:
        - dict: Un diccionario con los tipos como claves y la cantidad de elementos como valores.
    '''
    atributo_dict = {}
    
    if validar_lista(lista):
        for elemento in lista:
            atributo = elemento.get(key, "N/A")  # se utiliza para obtener el valor asociado a una clave específica. " "=valor por defecto, opcional
            
            # Reemplaza el valor vacío con "no tiene"
            if not atributo:
                atributo = "no tiene"
                
            atributo = capitalizar_palabras(atributo)

            if atributo in atributo_dict:
                atributo_dict[atributo] += 1
            else:
                atributo_dict[atributo] = 1

        return atributo_dict
    else:
        error = {"error": "la lista se encuentra vacía"}
        return error


def guardar_cantidad_heroes_tipo(diccionario: dict, key: str) -> bool:
    '''
    Guarda en un archivo CSV la cantidad de héroes para distintas variedades de un tipo de dato.
    Parámetros:
        - datos (dict): Un diccionario que representa las distintas variedades del tipo de dato como clave y sus cantidades como valor.
        - tipo_dato (str): El nombre del tipo de dato (por ejemplo, "color_pelo", "color_ojos").
    Retorna:
        - bool: True si se pudo guardar el archivo correctamente, False en caso contrario.
    '''
    contenido = []
    for clave, valor in diccionario.items():
        mensaje = f"Caracteristica: {key}: {clave} - Cantidad de heroes: {valor}"
        contenido.append(mensaje)
    
    archivo_nombre = f'heroes_cantidad_{key}.csv'
    guardar_archivo(archivo_nombre, "\n".join(contenido))  # Unimos las líneas en una sola cadena
    return True
    

def stark_calcular_cantidad_por_tipo(lista:list, key:str):
    '''
    Calcula la cantidad de héroes por tipo y guarda la información en un archivo CSV.
    Parámetros:
        - lista (list): La lista de héroes representados como diccionarios.
        - key (str): La clave por la cual se calculará la cantidad de héroes.
    Retorna:
        - bool: True si el cálculo y guardado son exitosos, False si hay algún error.
    '''
    dicc_tipo = calcular_cantidad_tipo(lista, key)
    print(f"\n   • Heroes agrupados por '{key}': ")
    for clave, valor in dicc_tipo.items():
        print(clave, valor)
    return guardar_cantidad_heroes_tipo(dicc_tipo, key)




################################################        6       ################################################

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
stark_marvel_app_3(copia_lista_juegos)
