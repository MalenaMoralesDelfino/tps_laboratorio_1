
import re
from data_stark_1 import lista_personajes
from typing import Union

'''
5.2
'''
def validar_entero(numero_str: str) -> bool:
    '''
    Verifica si el string contiene solo dígitos.
    parametro: numero a verificar
    retorno:
        -True o False.
    '''

    if numero_str.isdigit():
        return True
    else:
        return False
    
            #Interaccion con el usuario

def preguntar_opcion()->int:
    '''
    Pide al usuario una clave, valida que sea la opcion correcta y la devuelve.
    Si lo ingresado no es correcto, se repetirá el else hasta que se valide.
    retorno:
        -respuesta: str.
    '''
    while True:
        respuesta = input("\nSi desea buscar extremos a partir de un n° "
                            "en particular ingrese uno, de lo contrario ingrese '0' (cero): ")
        if respuesta is not False and validar_entero(respuesta):
            return float(respuesta)
        else:
            print("\nError. Debe ingresar un numero valido: ")       


def preguntar_key()->str:
    '''
    Pide al usuario una clave, valida que sea la opcion correcta y la devuelve.
    Si lo ingresado no es correcto, se repetirá el else hasta que se valide.
    retorno:
        -respuesta: str.
    '''
    while True:
        respuesta = input("\nElija un atributo: 'fuerza', el 'peso' o la 'altura'? ").lower()
        if respuesta is not False and respuesta in ['fuerza','peso','altura']:
            return(respuesta)
        else:
            print("\nError. Debe ingresar una opcion correcta: ")            


def preguntar_extremo()->str:
    '''
    Pide al usuario una extremo, valida que sea la opcion correcta y la devuelve.
    Si lo ingresado no es correcto, se repetirá el else hasta que se valide.
    retorno:
        -respuesta: str.
    '''
    while True:
        respuesta = input("\nDesea ver el mayor o el menor? ").lower()
        if respuesta is not False and respuesta in ['mayor','menor']:
            return(respuesta)
        else:
            print("\nError. Debe ingresar una opcion correcta: ")


'''
0
'''

def validar_lista(lista:list):
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
    datos_ya_normalizados = True
    if validar_lista(lista) and not datos_ya_normalizados:

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
            return True
        else:
            print("\n•Hubo un error al normalizar los datos.")
            return False
    else:
            print("\n•Los datos ya han sido normalizados anteriormente.")
            return True



'''
1.1.
'''


def obtener_datos(dicc: dict,key:str)->bool:
    '''
    Valida si un diccionario no esta vacio y contiene una clave "nombre".
    Parámetros:
        - dicc_heroe (dict): El diccionario que representa a un héroe.
        - key (str): La clave que se debe validar ("nombre").
    Retorno:
        - bool: True si el diccionario no está vacío y contiene la clave "nombre", False en caso contrario.
    '''
    if not dicc or key not in dicc:  #valida que dic no este vacio y key se encuentre en las keys
        return False
    return True
'''
1.2 
'''
def obtener_nombre(dicc:dict):
    '''
     Obtiene el nombre formateado de un héroe.
    Parámetros:
        - dicc_heroe (dict):representa a un héroe.
    Retorno:
        - str: El nombre del héroe formateado, False si no se cumple la validación.
    '''
    if obtener_datos(dicc, "nombre"):
        nombre = dicc["nombre"]
        return (f"Nombre: {nombre}")
    return False

'''
2 
'''
def obtener_nombre_y_dato(dicc:dict, key: str):
    '''
    Obtiene el nombre y el dato (key) de un héroe y lo formatea en un string.
    Parámetros:
        - dicc_heroe (dict): El diccionario que representa a un héroe.
        - key (str): La clave que representa el dato deseado ('altura', 'fuerza', 'peso', u otro).
    Retorna:
        - str: El nombre del héroe y el dato formateado como "Nombre: Nombre del héroe | dato: Valor del dato".
          Si el diccionario no contiene la clave 'nombre' o la clave especificada no existe, retorna "Error: Datos no disponibles".
    '''
    if obtener_datos(dicc,key):
        nombre = obtener_nombre(dicc)
        valor = dicc[key]
        return (f"Nombre {nombre} | {key} = {valor}")



'''
3.1 3.2
'''
def obtener_extremo(lista:list, key: str,extremo: str):
    '''
    Obtiene el valor extremo (mayor o menor) de un atributo específico en una lista de héroes.
    Parámetros:
        - lista (list): La lista de héroes de la cual se desea obtener el valor extremo.
        - key (str): El nombre del atributo por el cual se busca el valor extremo.
        - extremo (str): La dirección del extremo a buscar, puede ser "mayor" o "menor".
    Retorna:
        - float o int: El valor extremo del atributo especificado (mayor o menor).
        - False: Si la lista está vacía, no contiene el atributo o el atributo no es de tipo int o float.
    '''
     #isinstance verifica que la key sea float o int and (isinstance(key, int) or isinstance(key, float))
    if validar_lista(lista) and obtener_datos(lista[0], key):
        valor_extremo = None
        for elemento in lista:
            if key in elemento:
                valor = elemento[key]
                if isinstance(valor, (int, float)):
                    if extremo == "mayor":
                        if valor_extremo  is None or valor_extremo < elemento[key]:
                            valor_extremo = elemento[key]
                
                    elif extremo == "menor":
                        if valor_extremo  is None or valor_extremo > elemento[key]:
                            valor_extremo = elemento[key]
        return valor_extremo
    else:
        return False

'''
3.3 
'''    
def obtener_dato_cantidad(lista:list,valor:Union[float,int],key:str):
    '''
    Obtiene una lista de héroes que tienen un valor específico en una característica dada.
    Parámetros:
        - lista (list): La lista de héroes de la cual se desea obtener los héroes con el valor específico.
        - valor (Union[float, int]): El valor que se desea buscar en la característica especificada.
        - key (str): El nombre de la característica (atributo) en la cual se busca el valor.
    Retorna:
        - list: Una lista de héroes que tienen el valor específico en la característica especificada.
        - list: Una lista que contiene un único elemento ("No hay ningún héroe con ese valor en la característica especificada.")
        si no se encuentran héroes con el valor especificado.
        - False: Si la lista está vacía.
    '''
    if validar_lista(lista):
        heroes = []
        for elemento in lista:
            if elemento[key] == valor:
                heroes.append(elemento)
        if heroes:
            return heroes
        else:
            return ["No hay ningún héroe con ese valor en la característica especificada."]
    else:
        return False
'''
3.4 
'''  
def stark_imprimir_heroes(lista: list):
    '''
    Imprime la información de los héroes contenidos en una lista en un formato estructurado.
    Parámetros:
        - lista (list): La lista de héroes de la cual se desea imprimir la información.
    '''
    if validar_lista(lista):
        for elemento in lista:
            print("\n• Información del héroe:")
            for clave, valor in elemento.items():
                print(f"    {clave}: {valor}")
            print("_" * 25)


'''
4.1
'''
def sumar_dato_heroe(lista:list,key:str)->float:
    '''
    Recorre la lista de héroes y suma los valores de la característica especificada
    (por ejemplo, fuerza, altura, peso) para los héroes que tienen dicha característica.
    Parámetros:
        - lista (list): La lista de héroes de la cual se desea sumar los valores de la característica.
        - key (str): El nombre de la característica (atributo) que se desea sumar.
    Retorna:
        - tuple: Una tupla que contiene la suma total de los valores de la característica y la cantidad
        de héroes para los cuales se sumaron los valores.
        - False: Si no se encuentran héroes con la característica especificada o si la suma es igual a cero.
    '''
    acumulador = 0
    contador = 0
    for elemento in lista:
        if obtener_datos(elemento,key):
            if isinstance(elemento[key], (int, float)):
                acumulador += elemento[key]
                contador += 1
    if acumulador == 0:
        return False
    return (acumulador,contador)

'''
4.2
'''
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

'''
4.3
'''
def calcular_promedio(lista:list,key:str):
    '''
    Muestra en pantalla el promedio de los valores de la característica especificada
    (por ejemplo, fuerza, altura, peso) para los héroes que tienen dicha característica.

    Parámetros:
        - lista (list): La lista de héroes de la cual se desea mostrar el promedio de los valores de la característica.
        - key (str): El nombre de la característica (atributo) para la cual se desea mostrar el promedio.
    '''
    acumulador, contador = sumar_dato_heroe(lista,key)
    promedio = dividir(acumulador,contador)
    return promedio


'''
4.4
'''
def mostrar_promedio_dato (lista:list,key:str):
    '''
    Calcula el promedio de los valores de la característica especificada
    (por ejemplo, fuerza, altura, peso) para los héroes que tienen dicha característica.
    Parámetros:
        - lista (list): La lista de héroes de la cual se desea calcular el promedio de los valores de la característica.
        - key (str): El nombre de la característica (atributo) para la cual se desea calcular el promedio.

    Retorna:
        - float: El promedio de los valores de la característica especificada.
    '''
    if validar_lista(lista):
        for elemento in lista:
            if isinstance(elemento[key], (int, float)):
                promedio = calcular_promedio(lista,key)
        print(f"\n•El promedio de {key} es de: {promedio}.\n")



'''
5.1
'''    
def imprimir_menu():
    '''
    Muestra al usuario diferentes opciones.
    Mediante la funcion pedir_opcion_menu(), pide un valor.
    y lo devuelve.
    retorno:
        -opcion: int con la opcion seleccionada.
    '''
    print(  "\n"
            "1) Normalizar datos.\n"#0
            "2) Imprimir nombre y/o dato de cada superhéroe.\n" #1.2 y 2
            "3) Mostrar el superhéroe el mayor o menor de los heroes.\n" #3.3 3.4
            "4) Mostrar el promedio de un atributo numérico de todos los superhéroes.\n"#4.4
            "5) Salir.\n"
        )




'''
5.3
'''
def stark_menu_principal():
    '''
    Muestra un menú principal, solicita al usuario que ingrese una opción y valida
    que la opción ingresada sea un número entero dentro del rango del 1 al 6. Si la opción no es válida,
    se mostrará un mensaje de error y se repetirá la solicitud hasta que se ingrese una opción válida.
    Retorna:
        - valor (int): La opción válida seleccionada por el usuario.
    '''
    imprimir_menu()
    while True:
        valor = input("Que desea hacer?: ")
        if validar_entero(valor):
            valor = int(valor)
            if valor in range(1, 7):
                return valor
        else:
            print("Opción no válida. Por favor, ingrese un número válido del 1 al 6.")
            return False
        
     
'''
6
'''       
def stark_marvel_app(lista:list):
    '''
    Presenta un menú interactivo al usuario. 
    Dependiendo de la opción seleccionada por el usuario, realiza diversas
    acciones como normalizar datos, mostrar información de héroes, calcular promedios, etc.
    Parámetros:
        - lista (list): La lista de héroes que se utilizará en la aplicación.
    '''
    datos_normalizados = False
    while True:
        opcion = stark_menu_principal()
        match opcion:
            case 1:
                    stark_normalizar_datos(lista)
                    datos_normalizados = True

            case 2:
                if datos_normalizados:
                    key = preguntar_key()
                    for elemento in lista:
                        resultado = obtener_nombre_y_dato(elemento,key)
                        print(f"\n {resultado}")
                else:
                    print("\n•No se normalizaron los datos.\n")

            case 3:
                if datos_normalizados:

                    key = preguntar_key()
                    extremo = preguntar_extremo()
                    opcion = preguntar_opcion()
                    if opcion == 0:
                        valor = obtener_extremo(lista,key,extremo)
                    else:
                        valor = opcion
                    lista_personalizada= obtener_dato_cantidad(lista,valor,key)
                    stark_imprimir_heroes(lista_personalizada)
                else:
                    print("\n•No se normalizaron los datos.\n")

            case 4:
                if datos_normalizados:
                    key = preguntar_key()
                    mostrar_promedio_dato(lista,key)
                else:
                    print("\n•No se normalizaron los datos.\n")

            case 5:
                print("\nHasta luego\n")
                break

stark_marvel_app(lista_personajes)




'''
#print(lista_personajes)
print(stark_normalizar_datos(lista_personajes))
#print(lista_personajes)

for heroes in lista_personajes:
    print(obtener_nombre(heroes))


for heroe in lista_personajes:
    dato = "altura"  # Cambia esto por la clave del dato que desees obtener (por ejemplo, 'fuerza', 'peso', etc.)
    resultado = obtener_nombre_y_dato(heroe, dato)
    print(resultado)

extremo = preguntar_extremo()
valor = obtener_extremo(lista_personajes,"fuerza",extremo)
lista = obtener_dato_cantidad(lista_personajes,valor,"fuerza")
for heroes in lista:
    print(heroes)


#stark_imprimir_heroes(lista_personajes)


print(sumar_dato_heroe(lista_personajes,"nombre"))
'''