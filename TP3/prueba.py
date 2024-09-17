from typing import Union
lista_heroes=[  
    
    {
        "nombre": "Ghost Rider",
        "identidad": "Johnny Blaze",
        "empresa": "Marvel Comics",
        "altura": "188.50999999999999",
        "peso": "99.200000000000003",
        "genero": "M",
        "color_ojos": "Red",
        "color_pelo": "No Hair",
        "fuerza": "55",
        "inteligencia": "average"
    },
    {
        "nombre": "Blade",
        "identidad": "Eric Brooks",
        "empresa": "Marvel Comics",
        "altura": "188.44999999999999",
        "peso": "97.400000000000006",
        "genero": "M",
        "color_ojos": "Brown",
        "color_pelo": "Black",
        "fuerza": "30",
        "inteligencia": "good"
    },
    {
        "nombre": "Hawkeye",
        "identidad": "Clint Barton",
        "empresa": "Marvel Comics",
        "altura": "191.00999999999999",
        "peso": "104.93000000000001",
        "genero": "M",
        "color_ojos": "Blue",
        "color_pelo": "Blond",
        "fuerza": "15",
        "inteligencia": "average"
    },
    {
        "nombre": "Drax the Destroyer",
        "identidad": "Arthur Sampson Douglas",
        "empresa": "Marvel Comics",
        "altura": "193.00999999999999",
        "peso": "306.42000000000002",
        "genero": "M",
        "color_ojos": "Red",
        "color_pelo": "No Hair",
        "fuerza": "80",
        "inteligencia": "average"
    },
    {
        "nombre": "Iron Man",
        "identidad": "Tony Stark",
        "empresa": "Marvel Comics",
        "altura": "198.91",
        "peso": "191.88",
        "genero": "M",
        "color_ojos": "Blue",
        "color_pelo": "Black",
        "fuerza": "85",
        "inteligencia": "high"
    }
]


def obtener_extremo(lista:list, key: str,extremo: str):
    '''
    Obtiene el valor extremo (mayor o menor) de un atributo específico en una lista de héroes.
    Parámetros:
        - lista (list): La lista de héroes de la cual se desea obtener el valor extremo.
        - key (str): El nombre del atributo por el cual se busca el valor extremo.
        - extremo (str): La dirección del extremo a buscar, puede ser "mayor" o "menor".
    Retorna:
        - float o int: El valor extremo del atributo especificado (mayor o menor).
        - 
    '''
    valor_extremo = None  # Inicializamos valor_extremo con None
    for elemento in lista:
        if key in elemento:
            valor = float(elemento[key])
            if isinstance(valor, (int, float)):
                if extremo == "mayor":
                    if valor_extremo is None or valor_extremo < elemento[key]:
                        valor_extremo = elemento[key]
                elif extremo == "menor":
                    if valor_extremo is None or valor_extremo > elemento[key]:
                        valor_extremo = elemento[key]
                valor_extremo = float(valor_extremo)
    return valor_extremo


'''
3.3 
'''    
def obtener_dato_cantidad(lista:list,valor:Union[float,int],key:str,extremo:str):
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
    heroes = []
 
    for elemento in lista:
        numero =float(elemento[key])
        if numero == valor:
            heroes.append(elemento)
        elif numero != valor:
            if extremo == "mayor" and valor > numero:
                heroes.append(elemento)
            elif extremo == "menor" and valor < numero:   
                heroes.append(elemento)
    if heroes:
        return heroes
    else:
        return ["No hay ningún héroe con ese valor en la característica especificada."]
'''
3.4 
'''  
def stark_imprimir_heroes(lista: list):
    '''
    Imprime la información de los héroes contenidos en una lista en un formato estructurado.
    Parámetros:
        - lista (list): La lista de héroes de la cual se desea imprimir la información.
    '''
    for elemento in lista:
        if isinstance(elemento, dict):
            print("\n• Información del héroe:")
            for clave, valor in elemento.items():
                print(f"    {clave}: {valor}")
            print("_" * 25)
        else:
            print(elemento)  # Esto imprimirá el mensaje si no es un diccionario.




key = input("¿Qué atributo desea buscar?: ")
extremo = input("¿Qué extremo desea (mayor o menor)?: ")
valor_usuario = input("Ingrese un número o 0: ")
valor_usuario = float(valor_usuario)  # Convierte la entrada del usuario en un número de punto flotante.
if valor_usuario == 0:
    valor = obtener_extremo(lista_heroes,key,extremo)
else:
    valor = valor_usuario
lista_personalizada = obtener_dato_cantidad(lista_heroes, valor, key, extremo)
stark_imprimir_heroes(lista_personalizada)