'''
Desafío #02:
Usando como base lo realizado en el anterior desafío realizar los siguientes
informes en un menú
A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
género NB
B. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
D. Recorrer la lista y determinar cuál es el superhéroe más débil de género M
E. Recorrer la lista y determinar cuál es el superhéroe más débil de género NB
F. Recorrer la lista y determinar la fuerza promedio de los superhéroes de
género NB


G. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
H. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
I. Listar todos los superhéroes agrupados por color de ojos.
J. Listar todos los superhéroes agrupados por tipo de inteligencia.
NOTA: Se debe aplicar el tema Funciones visto en clase para cada opción del menú


'''

from data_stark_1 import lista_personajes



    #PEDIR VALORES

def pedir_opcion_menu()->int:
    '''
    Pide al usuario un valor mediante entrada de texto, lo 'parsea' como entero,
    valida que no esté vacío y que esté dentro de los rangos pedidos, y lo devuelve.
    Si lo ingresado no es correcto, se repetirá el else hasta que se valide.
    retorno:
        -valor: int.
    '''
    while True:
        valor = input("Que desea hacer?: ")
        valor = int(valor)
        if valor is not False and valor in range(1, 7):
            return valor
        else:
            print("Error. El valor debe ser un número entero positivo: ")



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


def preguntar_key()->str:
    '''
    Pide al usuario una clave, valida que sea la opcion correcta y la devuelve.
    Si lo ingresado no es correcto, se repetirá el else hasta que se valide.
    retorno:
        -respuesta: str.
    '''
    while True:
        respuesta = input("\nDesea calcular el promedio de la 'fuerza', el 'peso' o la 'altura'? ").lower()
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


def preguntar_atributo():
    '''
    Pide al usuario una opcion, valida que correcta y la devuelve.
    Si lo ingresado no es correcto, se repetirá el else hasta que se valide.
    retorno:
        -respuesta: str.
    '''
    while True:
        respuesta = input("\nDesea ver  los superhéroes agrupados según:\n"
                                "a) el color de ojos\n"  
                                "b) el color de pelo\n"
                                "c) el tipo de inteligencia.  ").lower()
        if respuesta is not False and respuesta in ['a','b','c']:
            return(respuesta)
        else:
            print("\nError. Debe ingresar una opcion válida: ")



    #MENÜ

def mostrar_menu()->int:
    '''
    Muestra al usuario diferentes opciones.
    Mediante la funcion pedir_opcion_menu(), pide un valor.
    y lo devuelve.
    retorno:
        -opcion: int con la opcion seleccionada.
    '''
    print(  "\n"
            "1) Imprimir datos de cada superhéroe.\n"
            "2) Mostrar el superhéroe el mayor o menor de los heroes.\n"
            "3) Mostrar el promedio de un atributo numérico de todos los superhéroes.\n"
            "4) Mostrar los superhéroes agrupados según un atributo.\n"
            "5) Salir.\n"
        )
    opcion = pedir_opcion_menu()
    return(opcion)





        #FUNCIONES PEDIDAS


def imprimir_datos_por_genero (genero:str)->int:
    '''
    Imprime los datos de superhéroes de un género específico o un mensaje de error si no se encuentra ninguno.
    parametros:
        -genero (str):  El género por el cual se desea filtrar los superhéroes.
                        Puede ser "M", "F", "NB", u otro.
    '''

    #A. Recorrer la lista imprimiendo por consola todos los datos de cada superhéroe
    for heroe in lista_personajes:
        if heroe["genero"] == genero:
            print("{")
            for key in heroe:
                value = heroe[key]
                print(f"{key} : {value}")
            print("}\n")
        elif genero == "NB":
            print ("\nLo sentimos, no existe ningun superheroe con ese tipo de género.\n")
            break

'''    #B.C. Recorrer la lista y determinar cuál es el superhéroe más alto
def determinar_altura_maxima_genero(genero:str)->tuple: 
    ''
    Determina el superhéroe más alto de un género específico.
    Parametros:
        -genero (str): El género por el cual se desea filtrar los superhéroes. Puede ser "M", "F", u otro.
    Returns:
        tupla: contiene el nombre del superhéroe más alto y su altura máxima como una cadena.
               Si no se encuentra ningún superhéroe con el género especificado, devuelve (None, None).
    ''
    altura_maxima = None
    nombre_heroe_mas_alto = None
    if genero == "NB":
        print ("\nLo sentimos, no existe ningun superheroe con ese tipo de género.\n")
        return nombre_heroe_mas_alto, altura_maxima
    else:
        for heroe in lista_personajes:
            if heroe["genero"] == genero:
                if altura_maxima is None or altura_maxima < float(heroe["altura"]):
                    altura_maxima=float(heroe["altura"])
                    nombre_heroe_mas_alto = heroe["nombre"]
        return nombre_heroe_mas_alto, altura_maxima



def determinar_menor_fuerza_genero(genero:str)->str:
    ''
    Determina el superhéroe más debil de un género específico.
    Parametros:
        -genero (str): El género por el cual se desea filtrar los superhéroes. Puede ser "M", "F", u otro.
    Returns:
        tupla: contiene el nombre del superhéroe más alto y su altura máxima como una cadena.
               Si no se encuentra ningún superhéroe con el género especificado, devuelve (None, None).
    ''
    menor_fuerza = None
    nombre_heroe_mas_debil = None
    if genero == "NB":
        print ("\nLo sentimos, no existe ningun superheroe con ese tipo de género.\n")
        return nombre_heroe_mas_debil, menor_fuerza
    else:
        for heroe in lista_personajes:
            if heroe["genero"] == genero:
                if menor_fuerza is None or menor_fuerza > float(heroe["fuerza"]):
                    menor_fuerza=float(heroe["fuerza"])
                    nombre_heroe_mas_debil = heroe["nombre"]
        return nombre_heroe_mas_debil, menor_fuerza'''

def determinar_mayor_menor (extremo: str, genero:str, key:str)->tuple:
    '''
    Determina el superhéroe con el valor mayor o menor de un atributo específico y género.
    Parametros:
        -extremo (str): Especifica si se busca el valor "mayor" o "menor".
        -genero (str): El género por el cual se desea filtrar los superhéroes. Puede ser "M", "F", u otro.
        -key (str): El atributo por el cual se realizará la comparación, por ejemplo, "altura" o "fuerza".
    Returns:
        tuple: Una tupla que contiene el nombre del superhéroe con el valor extremo y el valor extremo como una cadena.
               Si no se encuentra ningún superhéroe con el género especificado, devuelve (None, None).
    '''
    valor_extremo  = None
    nombre_heroe = None
    if genero == "NB":
        print ("\nLo sentimos, no existe ningun superheroe con ese tipo de género.\n")
        return nombre_heroe, valor_extremo 
    else:
        for heroe in lista_personajes:
            if heroe["genero"] == genero:
                if extremo == "mayor":
                    if valor_extremo  is None or valor_extremo  < float(heroe[key]):
                        valor_extremo =float(heroe[key])
                        nombre_heroe = heroe["nombre"]
                if extremo == "menor":
                    if valor_extremo  is None or valor_extremo  > float(heroe[key]):
                        valor_extremo =float(heroe[key])
                        nombre_heroe = heroe["nombre"]

        return nombre_heroe, valor_extremo



def calcular_promedio(genero:str, key:str)->float:
    '''
     Calcula el promedio de un atributo específico para superhéroes de un género dado.
    Parametros:
        -genero (str): El género por el cual se desea filtrar los superhéroes. Puede ser "M", "F", u otro.
        -key (str): El atributo para el cual se calculará el promedio, por ejemplo, "altura" o "peso".
    Returns:
        float: El promedio del atributo para los superhéroes del género especificado.
               Si no se encuentra ningún superhéroe con el género especificado, devuelve None.
    '''
    acumulador = 0
    contador = 0
    if genero == "NB":
        print ("\nLo sentimos, no existe ningun superheroe con ese tipo de género.\n")
        return None
    else:
        for heroe in lista_personajes:
            if heroe["genero"] == genero:
                acumulador += float(heroe[key])
                contador += 1
        promedio = acumulador / contador
        promedio = float(promedio)
        return promedio



'''def contar_atributos(key:str)->dict:
    
    atributos_heroes = ()
    nombres_heroes = {}

    for heroe in lista_personajes:
        nombre = heroe["nombre"]
        atributo = heroe[key]

        if atributo in atributos_heroes:
            atributos_heroes[atributo] += 1
        else:
            atributos_heroes[atributo] = 1

    return atributos_heroes'''


def contar_atributos(key:str)->dict:
    '''
     Cuenta la cantidad de superhéroes que tienen un atributo específico y los agrupa en un diccionario.
    parametros:
        -key (str): El nombre del atributo por el cual se desea agrupar a los superhéroes, como "inteligencia" o "color_pelo".
    Returns:
        -dict: Contiene como clave el valor del atributo y como valor una lista de nombres de superhéroes.
    '''
    atributo_dict = {}

    for heroe in lista_personajes:
        nombre = heroe["nombre"]
        atributo = heroe[key]
        atributo = atributo.lower() #para incluir todos en un mismo atributo no importa las mayus/minus
        # Verificar si el atributo ya está en el diccionario
        if atributo not in atributo_dict:
            atributo_dict[atributo] = []

        # Agregar el nombre del héroe al atributo correspondiente
        atributo_dict[atributo] = atributo_dict[atributo] + [nombre]

    return atributo_dict






    #GENERAL 

while True:
    opcion = mostrar_menu()

    match opcion:

        case 1:
            genero = preguntar_genero()
            imprimir_datos_por_genero(genero)

        case 2:
            genero = preguntar_genero()
            key = preguntar_key()
            extremo = preguntar_extremo()
            
            nombre, atributo = determinar_mayor_menor (extremo, genero, key)
            if nombre is not None and atributo is not None:
                if genero =="F":
                    genero = "femenino"
                elif genero == "M":
                    genero = "masculino"
                print(f"\nEl superhéroe {genero} con el valor {extremo} en {key} es: {nombre}, con un valor de {atributo}\n")

        
            '''
            case 3:
            genero = preguntar_genero()
            nombre, fuerza = determinar_menor_fuerza_genero(genero)
            if nombre is not None and fuerza is not None:
                if genero =="F":
                    genero = "femenino"
                elif genero == "M":
                    genero = "masculino"
                print(f"\nEl superhéroe {genero} mas debil es: {nombre}, con una fuerza de {fuerza}.\n")'''



        case 3:
            genero = preguntar_genero()
            key = preguntar_key()
            promedio = calcular_promedio(genero,key)
            if promedio is not None:
                if genero =="F":
                    genero = "femenino"
                elif genero == "M":

                    genero = "masculino"
                print(f"\nEl promedio de {key} del género {genero} es: {promedio}.\n")


        case 4:
            atributo = preguntar_atributo()
            if atributo == "a":
                heroes_agrupados = contar_atributos("color_ojos")
                print("\nHeroes agrupados segun el color de los ojos")
            elif atributo == "b":
              heroes_agrupados = contar_atributos("color_pelo")
              print("\nHeroes agrupados segun el color del pelo")
            else:
                print("\nHeroes agrupados segun la inteligencia")
                heroes_agrupados = contar_atributos("inteligencia")

            for atributo in heroes_agrupados:
                print("\n" + atributo + ":")
                for heroe in heroes_agrupados[atributo]:
                    print("-", heroe)
                num_heroes = len(heroes_agrupados[atributo])
                print("Número de héroes:", num_heroes,"\n")


        case 5:
            print("Hasta luego")
            break


