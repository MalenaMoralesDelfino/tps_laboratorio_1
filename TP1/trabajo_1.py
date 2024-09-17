'''
Luego de analizar el set de datos correspondiente resolver el Desafío #01:

A. Recorrer la lista imprimiendo por consola todos los datos de cada superhéroe
B. Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayor
fuerza (MÁXIMO)
C. Recorrer la lista y mostrar nombre e identidad del superhéroe más bajo
(MÍNIMO)
D. Recorrer la lista y determinar el peso promedio de los superhéroes
masculinos (PROMEDIO)
E. Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier
género) los cuales su fuerza supere a la fuerza promedio de todas las
superhéroes de género femenino
'''

from data_stark_1 import lista_personajes



while True:
    print(  "\nA. Datos de cada superhéroe.\n"
            "B. Superhéroe/s mas fuerte (nombre y peso).\n"
            "C. Superhéroe/s de menor estatura (nombre y identidad).\n"
            "D. Promedio del peso de los superhéroes masculinos.\n"
            "E. Superhéroes mas fuerte que el promedio del genero femenino.\n"
            "F. Salir.")
    opcion = input("Que desea hacer?(por favor igresar una opción en mayúscula)-> \n")
    while opcion not in ['A', 'B', 'C', 'D', 'E', 'F']:
            opcion = input("Error, ingrese una opcion valida (A, B, C, D, E, F)->  \n")

    match opcion:

        case 'A':
                #A. Recorrer la lista imprimiendo por consola todos los datos de cada superhéroe
            for heroe in lista_personajes:
                print("\n{")
                for key in heroe:
                    value = heroe[key]
                    print(f"{key} : {value}")
                print("}\n")
        

        case 'B':
                #B. Recorrer la lista y mostrar la identidad y el peso del superhéroe con mayor fuerza (MÁXIMO)
            mayor_fuerza = None
            heroes_mas_fuertes = []
            contador = 0 #USO un contador para vereficar si la lista tiene mas de un elemento, no puedo usar LEN 
            for heroe in lista_personajes:
                if mayor_fuerza is None or mayor_fuerza < float(heroe["fuerza"]):
                    mayor_fuerza=float(heroe["fuerza"])
                    heroes_mas_fuertes = [heroe]
                elif mayor_fuerza == float(heroe["fuerza"]):
                    heroes_mas_fuertes = heroes_mas_fuertes + [heroe] #Se puede usar append
                    contador += 1

            if contador == 0: #Aca se puede usar len(heroes_mayor_fuerza) == 1:
                heroe_mas_fuerte = heroes_mas_fuertes[0]
                identidad = heroe_mas_fuerte["identidad"]
                peso = heroe_mas_fuerte["peso"]
                print("\nEl héroe más fuerte es:", identidad, "con", mayor_fuerza, "de fuerza y pesa:", peso, "kg.\n")
            else:
                print("\nLos héroes más fuertes con", mayor_fuerza, "de fuerza son:")
                for heroe in heroes_mas_fuertes:
                    identidad = heroe["identidad"]
                    peso = heroe["peso"]
                    print(f"\n{identidad} con {mayor_fuerza} de fuerza y pesa {peso} kg.\n")


        case 'C':
                #C. Recorrer la lista y mostrar nombre e identidad del superhéroe más bajo (MÍNIMO)
            menor_altura = None
            heroes_mas_bajos = []
            contador = 0 #USO un contador para vereficar si la lista tiene mas de un elemento, no puedo usar LEN 
            for heroe in lista_personajes:
                if menor_altura is None or menor_altura > float(heroe["altura"]):
                    menor_altura=float(heroe["altura"])
                    heroes_mas_bajos = [heroe]
                elif menor_altura == float(heroe["altura"]):
                    heroes_mas_bajos = heroes_mas_bajos + [heroe] #Se puede usar append
                    contador += 1

            if contador == 0: #Aca se puede usar len(heroes_mayor_fuerza) == 1:
                heroes_mas_bajos = heroes_mas_bajos[0]
                nombre = heroes_mas_bajos["nombre"]
                identidad = heroes_mas_bajos["identidad"]
                print(f"\nEl héroe de menor estatura es: {nombre} ({identidad}) con {menor_altura} cm\n")
            else:
                print("Los héroes más fuertes con", menor_altura, "de fuerza son:")
                for heroe in heroes_mas_bajos:
                    nombre = heroe["nombre"]
                    identidad = heroe["identidad"]
                    print(f"\n{nombre} ({identidad}) con {menor_altura} cm de estatura.\n")



        case 'D':
            #D. Recorrer la lista y determinar el peso promedio de los superhéroes masculinos (PROMEDIO)
            acumulador = 0
            contador = 0
            for heroe in lista_personajes:
                if heroe["genero"] == "M":
                    acumulador += float(heroe["peso"])
                    contador += 1
            promedio_peso = acumulador / contador
            promedio_peso = float(promedio_peso)
            print(f"\nEl promedio del peso de los superheroes masculinos es de: {promedio_peso}\n")
        


        case 'E':
            #E. Recorrer la lista y mostrar nombre y peso de los superhéroes (cualquier género) 
            #   los cuales su fuerza supere a la fuerza promedio de todas las superhéroes de género femenino
            acumulador = 0
            contador = 0
            heroes_mayor_peso= []
            for heroe in lista_personajes:
                if heroe["genero"] == "F":
                    acumulador += float(heroe["fuerza"])
                    contador += 1
            promedio_fuerza = acumulador / contador
            promedio_fuerza = float(promedio_fuerza)
            print("\nEl promedio de fuerza femenina es de: ",promedio_fuerza,"\n")

            for heroe in lista_personajes:
                if promedio_fuerza < float(heroe["fuerza"]): 
                    heroes_mayor_peso = heroes_mayor_peso + [heroe]
            print("\nLos héroes más pesados por arriba del promedio de fuerza femenina son:\n")
            for heroe in heroes_mayor_peso:
                nombre = heroe["nombre"]
                peso = heroe["peso"]
                fuerza = heroe["fuerza"]
                print(f"{nombre} con {fuerza} de fuerza y {peso} kg.")

        case 'F':
            print("Hasta luego")
            break