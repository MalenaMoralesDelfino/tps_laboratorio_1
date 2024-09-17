'''
Desafío #04:
IMPORTANTE: Para todas y cada una de las funciones creadas, documentarlas
escribiendo que es lo que hacen, que son los parámetros que reciben (si es una lista,
un string, etc y que contendrá) y que es lo que retorna la función!

'''
from data_stark_1 import lista_personajes
import re



##########              PUNTO 1             ##########


def extraer_iniciales(nombre_heroe:str)->str:
    '''
    devuelve las iniciales de un nombre seguidas por un punto.
    elimina "the" y el "-" de los nombres.
    validaciones:
        -el string recibido no se encuentre vacío.
    parametros: 
        -nombre_heroe: un string con el nombre.
    retorno:
        -un nuevo string con las iniciales con puntos.
    
        
        #METODOS DE CADENAS

    if nombre_heroe == "":
        return("N/A")
    if "-" in nombre_heroe:
        nombre_heroe = nombre_heroe.replace("-"," ") #replace() reemplaza una cadena por otra
    if "the" in nombre_heroe:
        nombre_heroe= nombre_heroe.replace("the ", "")
    nombre_heroe = nombre_heroe.strip() #strip() elimina los espacios en blanco del principio y el fin de las cadenas
    lista_nombres = nombre_heroe.split(" ") # split() separa las cadenas segun el separador que le pases en el argumento
    iniciales = ""
    for nombre in lista_nombres:
        iniciales += nombre[0]
    iniciales = ".".join([nombre[0] for nombre in lista_nombres]) + "." #join()une una lista de srt en una sola usando el argumento como separador 
    return(iniciales)
    '''
    if not nombre_heroe:
        return "N/A"
    if nombre_heroe == "":
        return("N/A")
    if "-" in nombre_heroe:
        nombre_heroe = nombre_heroe.replace("-"," ") #replace() reemplaza una cadena por otra
    if "the" in nombre_heroe:
        nombre_heroe= nombre_heroe.replace("the ", "")
    nombre_heroe = nombre_heroe.strip() #strip() elimina los espacios en blanco del principio y el fin de las cadenas
    lista_nombres = nombre_heroe.split(" ") # split() separa las cadenas segun el separador que le pases en el argumento
    iniciales = ""
    for nombre in lista_nombres:
        iniciales += nombre[0]
    iniciales = ".".join([nombre[0] for nombre in lista_nombres]) + "." #join()une una lista de srt en una sola usando el argumento como separador 
    return(iniciales)

    ''' nombre_limpio = re.sub(r'^(the |-)', '', nombre_heroe, flags=re.IGNORECASE)    # sub para reemplazar "the - " . IGNORECASE para obviar mayus/minus

    iniciales = ''.join(re.findall(r'\b\w', nombre_limpio.upper()))# findall para encontrar iniciales . join para guardar todo en una lista

    mitad = len(iniciales) // 2   # Divide las iniciales a la mitad
    primera_mitad = iniciales[:mitad] #desde : el principio hasta la mitad
    segunda_mitad = iniciales[mitad:] #desde la mitad hasta el final:

    return f"{primera_mitad}.{segunda_mitad}"    #iniciales separadas por un punto.'''




def definir_iniciales_nombre(heroe: dict)->bool:
    '''
    agrega una nueva clave al diccionario recibido como parámetro. 
    La clave es ‘iniciales’ y su valor se obtiene de llamar a la función ‘extraer_iniciales’
    validaciones:
        -el dato recibido sea del tipo diccionario y que contengan la clave ‘nombre’.
    parametros: 
        -heroe: un diccionario con los datos de un personaje.
    retorno:
        -True o False.
    '''
    if isinstance(heroe, dict):
        if "nombre" in heroe: 
            iniciales = extraer_iniciales(heroe["nombre"])
            heroe["iniciales"] = iniciales
            #print(heroe) para chequear que se copiaron las iniciales
            return (True)
        else:
            return(False)
    else:
        return(False)


def agregar_iniciales_nombre(lista_heroes: list)->bool:
    '''
    Itera la lista_heroes pasándole cada héroe a la función definir_iniciales_nombre.
    validaciones:
        -lista_heroes sea del tipo lista y que contenga al menos un elemento.
        -si función definir_iniciales_nombre() retorna False imprime mensaje de error.
    parametros: 
        -lista_heroes: lista de personajes.
    retorno:
        -True o False.
    '''
    if isinstance(lista_heroes, list) and len(lista_heroes) > 0:
        for heroe in lista_heroes:
            if not definir_iniciales_nombre(heroe):
                print ("El origen de datos no contiene el formato correcto")
                return(False)
            #definir_iniciales_nombre(heroe)
        return(True)
    else:
        return(False)


def stark_imprimir_nombres_con_iniciales(lista_heroes: list):
    '''
    utiliza la función agregar_iniciales_nombre’ para añadirle
    las iniciales a los diccionarios contenidos en la lista_heroes.
    Imprime la lista completa de los nombres de los personajes
    seguido de las iniciales encerradas entre paréntesis ()
    parametros: 
        -lista_heroes: lista de personajes.
    retorno:
        -No tiene.
    '''
    if agregar_iniciales_nombre(lista_heroes):
        print("\nHeroes con sus respectivas iniciales: \n")
        for heroe in lista_heroes:
            mensaje = f"{heroe['nombre']}, {heroe['iniciales']}"
            print(mensaje)
        
    




##########              PUNTO 2             ##########

def generar_codigo_heroe(id_heroe: int, genero_heroe: str)->str:
    '''
    genera un id con el género recibido por parámetro seguido de un ‘-’ 
    (guión) y por último el identificador recibido.
    validaciones:
        -El identificador del héroe sea numérico.
        -El género no se encuentre vacío y esté dentro de los valores esperados
    parametros: 
        -id_heroe: entero que representa el identificador del héroe.
        -genero_heroe: string que representa el género del héroe.
    retorno:
        -n/a o id_heroe.

        if genero_heroe is not None and genero_heroe in ["F","M","NB"] and str(id_heroe).isdigit():
    '''
    if re.match(r'^(F|M|NB)$', genero_heroe) and re.match(r'^\d+$', str(id_heroe)):
        id_heroe = str(id_heroe).zfill(8)
        id_heroe = f"{genero_heroe}-{id_heroe}" #f str
        return(id_heroe)
    else:
        return("N/A")
    

def agregar_codigo_heroe(id_heroe: int, heroe: dict)->bool:
    '''
    Agrega una nueva clave llamada ‘codigo_heroe’ al diccionario ‘heroe’ 
    recibido como parámetro y le asigna como valor un código utilizando 
    la función ‘generar_codigo_heroe’
    validaciones:
        -El diccionario recibido como parámetro no se encuentre vacío.
        -El código recibido mediante generar_codigo_heroe tenga exactamente 10 caracteres.
    parametros: 
        -id_heroe: entero que representa el identificador del héroe.
        -heroe: diccionario con los datos del personaje
    retorno:
        -True o False.
    '''
    if isinstance(heroe, dict) and len(heroe) > 0:
        codigo_heroe = generar_codigo_heroe(id_heroe, heroe["genero"])
        if len(codigo_heroe) == 10:
            heroe["codigo_heroe"] = codigo_heroe
            return(True)
    else:
        return(False)


def stark_generar_codigos_heroes(lista_heroes: list,imprimir:bool):
    '''
    Itera la lista de personajes y agrega el código a cada uno de los personajes. 
    El código del héroe (id_heore) surge de la posición del mismo dentro de la 
    lista_heroes (comenzando por el 1). Reutiliza la función agregar_codigo_heroe 
    pasándole como argumentos el héroe que se está iterando y el id_heroe. 
    Una vez finalizado imprime por pantalla un mensaje.
    En caso de encontrar algún error, informa por pantalla.
    validaciones:
        -La lista contenga al menos un elemento.
        -Todos los elementos de la lista sean del tipo diccionario.
        -Todos los elementos contengan la clave ‘genero’.
    parametros: 
        -id_heroe: entero que representa el identificador del héroe.
        -heroe: diccionario con los datos del personaje
    retorno:
        -No tiene.
    '''
    if isinstance(lista_heroes, list) and len(lista_heroes) > 0:
        if all(isinstance(elemento, dict) for elemento in lista_heroes): #Todos los elementos de la lista sean del tipo diccionario
            for numero, heroe in enumerate(lista_heroes, start=1):
                if "genero" in heroe:
                    if not agregar_codigo_heroe(numero, heroe):
                        print ("El origen de datos no contiene el formato correcto")
                        return False
            print("\nSe asignaron ", numero, " códigos.\n")
            if imprimir:
                for heroe in lista_heroes:
                    mensaje =  f"{heroe['nombre']}, {heroe['codigo_heroe']}"
                    print(mensaje)
        else:
            print("No todos los elementos de la lista son diccionarios o no todos contienen la clave 'genero'")
    else:
        print("La lista de héroes está vacía o no es una lista")






##########              PUNTO 3             ##########

def sanitizar_entero(numero_str: str)->int:
    '''
    Analiza el string recibido y determina si es un número entero positivo.
    Quita los espacios en blanco de atras y adelante del string en caso que los tuviese.
    parametros:
        -numero_str: un string que representa un posible número entero.
    Devuelve distintos valores según el problema encontrado (retornos):
        -1: contiene carácteres no numéricos.
        -2: el número es negativo.
        -3: ocurren otros errores que no permiten convertirlo a entero
        -numero_int (numero_str): En caso que se verifique que el texto contenido en 
        el string es un número entero positivo. lo retorna convertido en entero.
    '''
    numero_str = numero_str.strip()
    
    # regex para buscar solo numeros, si no hay retorna -1
    if not re.match(r'^\d+$', numero_str):
        return -1

    # Conversión a entero
    numero_int = int(numero_str)

    # Validación para números negativos
    if numero_int <= 0:
        return -2

    return numero_int


def sanitizar_flotante(numero_str: str)->float:
    '''
    Analiza el string recibido y determina si es un número flotante positivo.
    Quita los espacios en blanco de atras y adelante del string en caso que los tuviese.
    parametros:
        -numero_str: un string que representa un posible número entero.
    Devuelve distintos valores según el problema encontrado (retornos):
        -1: contiene carácteres no numéricos.
        -2: el número es negativo.
        -3: ocurren otros errores que no permiten convertirlo a entero
        -numero_int (numero_str): En caso que se verifique que el texto contenido en 
        el string es un número entero positivo. lo retorna convertido en flotante.
    '''
    numero_str = numero_str.strip()
    
    # regex para buscar solo numeros decimales, si no hay retorna -1
    if not re.match(r'^\d+(\.\d+)$', numero_str):
        return -1.0
    numero_float = float(numero_str)
        
        # Validación para números negativos
    if numero_float <= 0:
        return -2.0
        
    return numero_float
    
   


def sanitizar_string(valor_str: str,valor_por_defecto: str = "-")->str:
    '''
    Analiza el string recibido y determina si es solo texto (sin números).
    En el caso que valor_str contenga una barra ‘/’ deberá ser reemplazada
    por un espacio (es un caracter válido).
    Quita los espacios en blanco de atras y adelante de ambos parámetros en 
    caso que los tuviese.
    parametros: 
        - valor_str: string que representa el texto a validar
        - valor_por_defecto: un string que representa un valor por defecto
        (parámetro opcional, se inicializa con ‘-’)
    retornos:
        - “N/A”: En caso de encontrarse números.
        - valor_str: En caso que se verifique que el parámetro recibido es solo texto, se
        retorna el mismo convertido todo a minúsculas.
        - valor_por_defecto: En el caso que el texto a validar se encuentre vacío se retorna 
        el valor por defecto convertido a minúsculas.


        if any(caracter.isdigit() for caracter in valor_str):#Si hay alguno de los caracteres de valor_str que es un dígito (número), entonces..."
        return("N/A")
    '''
    valor_str = valor_str.strip()
    valor_por_defecto = valor_por_defecto.strip()
    if re.search(r'\d', valor_str):#"Si hay algun caracter en valor_str que es número, entonces..."
        return "N/A"

    elif valor_str == "":
        return(valor_por_defecto.lower())
    else:
        if "/" in valor_str:
            valor_str = valor_str.replace("/"," ") # valor_str = re.sub(r'/', ' ', valor_str)
        return(valor_str.lower())


def sanitizar_dato(heroe:dict, clave:str, tipo_dato:str)->bool:
    '''
    Sanitiza el valor del diccionario correspondiente a la clave
    y al tipo de dato recibido.
    validaciones:
        - Que tipo_dato se encuentre entre los valores esperados (‘string, ‘entero,
        ‘flotante)’, debe soportar que nos lleguen mayúsculas o minúsculas. 
        En caso de encontrarse un valor no válido informa por pantalla: 
        ‘Tipo de dato no reconocido’.
        - Que clave exista como clave dentro del diccionario heroe. En caso de
        no encontrarse, informar por pantalla: ‘La clave especificada no
        existe en el héroe’. (en este caso la validación es sensible a
        mayúsculas o minúsculas).
    parametros: 
        - heroe: diccionario con los datos del personaje.
        - clave: string que representa el dato a sanitizar (la clave del
        diccionario). Por ejemplo altura.
        - tipo_dato: string que representa el tipo de dato a sanitizar. 
        Puede tomar los valores: ‘string’, ‘entero’ y ‘flotante’.
    retornos:
        - Devuelve True en caso de haber sanitizado algún dato y False en caso contrario.
    '''
    tipo_dato = tipo_dato.lower()
    if isinstance(heroe, dict) and len(heroe) > 0:
        if clave in heroe and tipo_dato in ['entero', 'flotante', 'string']:
                if tipo_dato == "entero":
                    valor_sanitizado = sanitizar_entero(heroe[clave])
                elif tipo_dato == "flotante":
                    valor_sanitizado = sanitizar_flotante(heroe[clave])
                elif tipo_dato == "string":
                    valor_sanitizado = sanitizar_string(heroe[clave])
                #print(valor_sanitizado)
                heroe[clave] = valor_sanitizado
                return True
        elif tipo_dato not in ['entero', 'flotante', 'string']:
            print("Tipo de dato no reconocido.")
            return False
        else:
            print("La clave especificada no existe en el héroe.")
            return False
        
def stark_normalizar_datos(lista_heroes: list):
    '''
    Recorre la lista de héroes y sanitiza los valores solo de las
    siguientes claves: ‘altura’, ‘peso’, ‘color_ojos’, ‘color_pelo’, ‘fuerza’
    e ‘inteligencia’. Una vez finalizado el proceso mostrar el mensaje 
    ‘Datos normalizados’. Reutiliza la función sanitizar_dato.
    Validaciones: 
        - Que la lista de héroes no esté vacía para realizar sus acciones,
    caso contrario imprimirá el mensaje: “Error: Lista de héroes vacía”.
    Parametros:
        - lista_heroes: la listas personajes.
    Retorno:
        - La función no retorna nada.
    '''
    if isinstance(lista_heroes, list) and len(lista_heroes) > 0:
        dicc_clave_tipo ={          'altura':'flotante',
                                    'peso':'flotante',
                                    'color_ojos':'string',
                                    'color_pelo':'string',
                                    'fuerza':'entero',
                                    'inteligencia':'string'}
        for heroe in lista_heroes:
            for clave,tipo in dicc_clave_tipo.items():
                sanitizar_dato(heroe, clave, tipo)
        print("\n*Datos normalizados*\n")
    else:
        print("\nError: Lista de héroes vacía\n")





##########              PUNTO 4             ##########

def generar_indice_nombres(lista_heroes: list)->list:
    '''
    itera la lista de personajes y generar una lista donde cada
    elemento es cada palabra que componen el nombre de los personajes.
    En caso de encontrar algún error, informar por pantalla: 
    ‘El origen de datos no contiene el formato correcto’
    validaciones: 
        - La lista contenga al menos un elemento
        - Todos los elementos de lista_heroes sean del tipo diccionario
        - Todos los elementos contengan la clave ‘nombre’
    parametros:
        - lista_heroes: la lista de personajes.
    retorno:
        - lista_nombres: lista con todos los nombres.


        nombre_heroe = re.sub(r'-', ' ', nombre_heroe)  # Reemplaza '-' por espacio utilizando una expresión regular
        palabras = re.findall(r'\b\w+\b', nombre_heroe.lower())  # Divide el nombre en palabras
    '''
    if not isinstance(lista_heroes, list) or len(lista_heroes) == 0: #verifca que exista la lista y sea list
        print("El origen de datos no contiene el formato correcto: la lista está vacía o no es una lista.")
        return []

    for elemento in lista_heroes:
        if not isinstance(elemento, dict) or not "nombre" in elemento: #que no exista y sea dict o que no exista nombre en el dict
            print("El origen de datos no contiene el formato correcto: uno o más elementos no son diccionarios.")
            return []

    #todo lo de arriba son validaciones.

    lista_nombres=[]
    for heroe in lista_heroes:
        nombre_heroe = heroe["nombre"]
        if "-" in nombre_heroe:
            nombre_heroe = nombre_heroe.replace("-"," ") #replace() reemplaza una cadena por otra
        nombres = nombre_heroe.split(" ")
        lista_nombres.extend(nombres) #extend() agrega múltiples elementos a una lista. 
    return lista_nombres
'''    for elemento in lista_nombres:
        print(elemento)'''

def stark_imprimir_indice_nombre(lista_heroes: list):
    '''
    Muestra por pantalla el índice generado por la función generar_indice_nombres()
    con todos los nombres separados con un guión.
    Parámetros:
        - lista_heroes: la lista de personajes.
    '''
    lista_nombres = generar_indice_nombres(lista_heroes)
    indice_nombre = "-".join(lista_nombres)
    print(f"\n{indice_nombre}")



##########              PUNTO 6             ##########

def convertir_cm_a_mtrs(valor_cm:float)->float:
    '''
    Retorna el número recibido, pero convertido a la unidad metros.
    Valida que el número recibido sea un número flotante positivo, si no retorna -1
    parámetros:
        -valor_cm: número que representa una medida en centímetros.
    Retorno:
        -valor_mtrs: número que representa una medida en metros.
    '''
    #Verifica que valor_cm sea un número flotante positivo
    if isinstance(valor_cm, float) and valor_cm >= 0:
        # Convertir centímetros a metros y acortar a 2 decimales
        valor_mtrs = round(valor_cm / 100, 2)
        return valor_mtrs
    else:
        return -1

def generar_separador(patron:str, largo:int, imprimir:bool=True)->str:
    '''
    Genera un string que contenga el patrón especificado repitiendo tantas veces 
    como la cantidad recibida como parámetro (uno junto al otro, sin salto de línea).
    Si el parámetro booleano recibido se encuentra en False solo retorna el separador generado. 
    Si se encuentra en True antes de retornarlo, lo imprime por pantalla.
    parámetro
        -patron: carácter que se utilizado como patrón para generar el separador
        -largo: número que representa la cantidad de caracteres que ocupa el separador.
        -imprimir: un parámetro opcional del tipo booleano (por default definido en True)
    Validaciones:
        -Que el parámetro patrón tenga al menos un carácter y como máximo dos
        -Que el parámetro largo sea un entero entre 1 y 235 inclusive
    En caso de no verificarse las validaciones devuelve ‘N/A’
    Retorno:
        -separador: string con el patrón especificado repetido segun la cantidad recibida

    '''

    if not (1 <= len(patron) <= 2):# validación entre uno o dos caracteres
        return 'N/A'

    if not (isinstance(largo, int) and 1 <= largo <= 235):# Validación entre 1 y 235 inclusive
        return 'N/A'
    separador = patron * largo
    if imprimir:
        print (separador)
    return separador


def generar_encabezado(titulo:str)->str:
    '''
    Devuelve un string que contenga el título envuelto entre dos separadores.
    Convierte el titulo recibido en todas letras mayúsculas.
    parámetro:
        -titulo: un string que representa el título de una sección de la ficha
    retorno:
        -encabezado: str con el titulo y los separadores
    '''
    titulo = titulo.upper()
    separador = generar_separador("-",25,False)#FALSE PARA QUE NO SE REPITA
    encabezado = f"{separador}\n* {titulo} *\n{separador}"
    return encabezado


def imrpimir_ficha_heroe(heroe:dict):
    '''
    Genera un string con un formato en particular y lo imprime por pantalla.
    Parametros:
        -heroe: un diccionario con los datos del héroe.
    '''
    # Generar encabezado "PRINCIPAL"
    encabezado_principal = generar_encabezado("PRINCIPAL")


    # Generar sección "PRINCIPAL"
    seccion_principal = f"NOMBRE DEL HÉROE:  {heroe['nombre']}. ({heroe['iniciales']}) \n" # creo cadenas de texto
    seccion_principal += f"IDENTIDAD SECRETA: {heroe['identidad']}\n" #uno (concateno) con + la cadena
    seccion_principal += f"CONSULTORA:        {heroe['empresa']}\n"
    seccion_principal += f"CÓDIGO DE HÉROE:   {heroe['codigo_heroe']}\n"


    # Generar encabezado "FISICO"
    encabezado_fisico = generar_encabezado("FISICO")
    altura_mtrs = convertir_cm_a_mtrs(heroe['altura'])
    # Generar sección "FISICO"
    seccion_fisico = f"ALTURA:  {altura_mtrs} Mtrs.\n"
    seccion_fisico += f"PESO:    {round(heroe['peso'],2)} Kg.\n"
    seccion_fisico += f"FUERZA:  {heroe['fuerza']}.\n"

        # Generar encabezado "SEÑAS PARTICULARES"
    encabezado_senas = generar_encabezado("SEÑAS PARTICULARES")


    # Generar sección "SEÑAS PARTICULARES"
    seccion_senas = f"COLOR DE OJOS:  {heroe['color_ojos']}\n"
    seccion_senas += f"COLOR DE PELO:  {heroe['color_pelo']}\n"
    seccion_senas += f"INTELIGENCIA:   {heroe['inteligencia']}\n"    



    # Imprimir la ficha del héroe
    ficha_heroe =   (
                        f"\n{encabezado_principal}\n"
                        f"{seccion_principal}\n"
                        f"{encabezado_fisico}\n"
                        f"{seccion_fisico}\n"
                        f"{encabezado_senas}\n"
                        f"{seccion_senas}"
                    )

    print(ficha_heroe)



def stark_navegar_fichas(lista_heroes:list):
    '''
    Comienza imprimiendo la ficha del primer personaje de la lista y luego 
    solicita que se ingrese alguna de las siguientes opciones:
        [ 1 ] Ir a la izquierda [ 2 ] Ir a la derecha [ S ] Salir
        - ‘1’: se muestra el héroe que se encuentra en la posición 
        anterior en la lista (en caso de estar en el primero, muestra el último)
        - ‘2’: se muestra el héroe que se encuentra en la posición 
        siguiente en la lista (en caso de estar en el último, muestra el primero)
        -Si ingresa ‘S’: vuelve al menú principal.
    Si ingresa cualquier otro valor, volver a mostrar las opciones hasta que 
    ingrese un valor válido.
    Parámetros:
        - lista_heroes: la listas personajes
    
    '''
    posicion_actual = 0
    total_personajes = len(lista_heroes) #total de heroes - 1 (de 0 a 23)

    while True:
        # Imprimir la ficha del héroe actual
        imrpimir_ficha_heroe(lista_heroes[posicion_actual])

        # Solicitar al usuario que ingrese una opción
        print("\n[ 1 ] Ir a la izquierda."
              "\n[ 2 ] Ir a la derecha."
              "\n[ S ] Volver al menú principal.")
        
        opcion = input("Ingrese su elección: ")
        if opcion == "1":
            posicion_actual = (posicion_actual - 1) % total_personajes # Ir a la izquierda ## el % hace que quede 
        elif opcion =="2":
            posicion_actual = (posicion_actual + 1) % total_personajes # Ir a la derecha   ## entre los limites del tamaño de la lista resultado = dividendo % divisor
        elif opcion.upper() == 'S':
            break # Salir
        else:
            print("Opción no válida. Por favor, ingrese '1', '2' o 'S'.")
    pass





##########              PUNTO 6             ##########

def imprimir_menu():
    '''
    Muestra al usuario diferentes opciones.
    Mediante la funcion pedir_opcion_menu(), pide un valor.
    y lo devuelve.
    retorno:
        -opcion: int con la opcion seleccionada.
    '''
    print(  "\n"
            "1) Imprimir la lista de nombres junto con sus iniciales.\n"#1.4
            "2) Generar códigos de héroes.\n" #1.2 y 2
            "3) Normalizar datos.\n" #3.3 3.4
            "4) Imprimir índice de nombres.\n"#4.4
            "5) Navegar fichas.\n"
            "6) Salir.\n"
        )

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
        valor =  sanitizar_entero(valor)
        if valor in range(1, 7):
            return valor
        else:
            print("Opción no válida. Por favor, ingrese un número válido del 1 al 6.")
            return False
        

def stark_marvel_app_3(lista:list):
    '''
    Presenta un menú interactivo al usuario. 
    Dependiendo de la opción seleccionada por el usuario, realiza diversas
    acciones como normalizar datos, mostrar información de héroes, calcular promedios, etc.
    Parámetros:
        - lista (list): La lista de héroes que se utilizará en la aplicación.
    '''
    iniciales_generadas = False
    codigos_generados = False
    datos_normalizados = False
    while True:
        opcion = stark_menu_principal()

        match opcion:
            case 1:
                stark_imprimir_nombres_con_iniciales(lista)
                iniciales_generadas= True

            case 2:
                respuesta = input("\nCódigos asignados, desea verlos?: si o no:  ")
                if respuesta == "si":
                    imprimir = True
                else:
                    imprimir = False
                stark_generar_codigos_heroes(lista,imprimir)
                codigos_generados = True

            case 3:
                stark_normalizar_datos(lista)
                datos_normalizados = True

            case 4:
                stark_imprimir_indice_nombre(lista)
            case 5:
                if iniciales_generadas and datos_normalizados and codigos_generados:
                    stark_navegar_fichas(lista)
                    '''for heroe in lista:
                        generar_separador("*",50)
                        imrpimir_ficha_heroe(heroe)'''
                else:
                    if not iniciales_generadas and not codigos_generados and not datos_normalizados:
                        print("\n•Generar iniciales y codigos, y normalizar datos primero.")
                    elif not iniciales_generadas:
                        print("\n•No se generaron las iniciales, entrar a la opcion 1.\n")
                    elif not codigos_generados:
                        print("\n•No se generaron los codigos, entrar a la opcion 2.\n")
                    elif not datos_normalizados:
                        print("\n•No se normalizaron los datos, entrar a la opcion 3.\n")
            case 6:
                print("\nHasta luego.\n")
                break

stark_marvel_app_3(lista_personajes)

