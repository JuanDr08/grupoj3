import os
from tabulate import tabulate

titulo = """
    +++++++++++++++++++++++++++++++++++++
    +  Federacion De Futbol Colombiano  +
    +++++++++++++++++++++++++++++++++++++
"""

tabla = """
    +++++++++++++++++++++++++++++++++++++
    +        Tabla De Posiciones        +
    +++++++++++++++++++++++++++++++++++++
"""

opciones = "1- Registrar un equipo\n2- Registrar una fecha\n3- Tabla de posiciones\n4- Reporte"

Encendido = True
Equipos = []
while Encendido:
    os.system('cls')
    print(titulo)
    print(opciones)
    opcion = int(input("-(Entero): "))
    if (opcion == 1):
        os.system("cls")
        nombreEquip = str(input("Ingrese el nombre del equipo: ")).upper()             # pedir nombre
        Equipos.append([nombreEquip, 0, 0, 0, 0, 0, 0, 0])     # registrar equipo con datos en 0
        if (len(Equipos) > 1):
            for i, item in enumerate(Equipos):
                if (i >= 1):
                    if (Equipos[i-1][0] == Equipos[i][0]):
                        os.system("cls")
                        print("Debe registrar dos equipos diferentes, el segundo registrado sera eliminado")
                        Equipos.pop(i)
                        os.system("pause")
    elif(opcion == 2):
        if (len(Equipos) < 2):
            os.system("cls")
            print("No hay suficientes equipos registrados")
            print("Debe haber registrado al menos dos equipos, porfavor registrelos en la opcion 1")
            os.system("pause")
        else:            
            os.system("cls")
            for i, item in enumerate(Equipos): # Disponibilidad
                print("Equipos disponibles: ", item[0])
            vsLocal = str(input("Ingrese el equipo que jugara de Local: ")).upper()           # Ingreso contrincantes
            vsVisitante = str(input("Ingrese el equipo que jugara de visitante: ")).upper()      # Ingreso contrincantes
            localExist = False
            visitanteExist = False
            for item in Equipos:
                if (vsLocal in item):
                    localExist = True
                elif (vsVisitante in item):
                    visitanteExist = True
            if ((localExist == True) and (visitanteExist == True) and (vsLocal != vsVisitante)):
                marcadorLocal = int(input(f"Ingrese el marcador (Numeros) del equipo {vsLocal}: "))
                marcadorVisitante = int(input(f"Ingrese el marcador (Numeros) del equipo {vsVisitante}: ")) 
                if((marcadorLocal >= 0) and  (marcadorVisitante >= 0)):
                    for item in Equipos:                              
                        if ((vsLocal in item) or (vsVisitante in item)):
                            if (item[0] == vsLocal):
                                item[1] += 1
                                item[5] += marcadorLocal
                                item[6] += marcadorVisitante
                                if (marcadorLocal > marcadorVisitante):
                                    item[2] += 1
                                    item[7] += 3
                                elif (marcadorLocal < marcadorVisitante):
                                    item[3] += 1
                            elif (item[0] == vsVisitante):
                                item[1] += 1
                                item[6] += marcadorLocal
                                item[5] += marcadorVisitante
                                if (marcadorLocal < marcadorVisitante):
                                    item[2] += 1
                                    item[7] += 3
                                elif (marcadorLocal > marcadorVisitante):
                                    item[3] += 1
                            if (marcadorLocal == marcadorVisitante):
                                item[4] += 1
                                item[7] += 1
                else:
                    print("ingrese un valor correcto")
                    os.system("pause") 
            elif(vsLocal == vsVisitante):
                print("Registre dos equipos diferentes")
                os.system("pause")  
            else :
                print("Uno de los equipos ingresados no ha sido registrado, o ninguno lo ha sido, profavor vaya a la opcion 1\ny registrelo para poder enfrentrarlo")                    
                os.system("pause")
    elif(opcion == 3):
        os.system("cls")
        print(tabla)
        print(tabulate(Equipos,headers=["Equipo", "PJ", "PG", "PP", "PE", "GF", "GC", "TP"]))
        os.system("pause")
    elif(opcion == 4):
    # ORDEN SEGUN MAS GOLES ANOTADOS
        for i,item in enumerate(Equipos):
            for j in range(int(i+1), len(Equipos),1):
                if (Equipos[i][5] < Equipos[j][5]):
                    aux = Equipos[i]
                    Equipos[i] = Equipos[j]
                    Equipos[j] = aux
            if (i == ((len(Equipos))-1)):
                if (Equipos[i - ((len(Equipos))-1)][5] == Equipos[j - ((len(Equipos))-2)][5]):
                    os.system("cls")
                    print("HAY DOS EQUIPOS CON LA MISMA CANTIDAD DE GOLES ANOTADOS")
                    print(f"A. Los equipos que mas goles anotaron fueron el equipo: {Equipos[i-((len(Equipos))-1)][0]} con un total de {Equipos[i-((len(Equipos))-1)][5]} goles")
                    print(f" y el equipo: {Equipos[i-((len(Equipos))-2)][0]} con un total de {Equipos[i-((len(Equipos))-2)][5]} goles")
                    os.system("pause")
                else:
                    print("A. El equipo que mas goles anoto fue: ", Equipos[i-((len(Equipos))-1)][0], f"con un total de {Equipos[i-((len(Equipos))-1)][5]} goles")
                    os.system("pause")
    # ORDEN SEGUN MAS PUNTOS OBTENIDOS
        for i,item in enumerate(Equipos):
            for j in range(int(i+1), len(Equipos),1):
                if (Equipos[i][7] < Equipos[j][7]):
                    aux = Equipos[i]
                    Equipos[i] = Equipos[j]
                    Equipos[j] = aux
            if (i == ((len(Equipos))-1)):
                if (Equipos[i - ((len(Equipos))-1)][7] == Equipos[j - ((len(Equipos))-2)][7]):
                    os.system("cls")
                    print("HAY DOS EQUIPOS QUE COMPARTEN LA MISMA CANTIDAD DE PUNTOS")
                    print(f"B. Los equipos que mas puntos tienen son el equipo: {Equipos[i-((len(Equipos))-1)][0]} con un total de {Equipos[i-((len(Equipos))-1)][7]} puntos")
                    print(f" y el equipo: {Equipos[i-((len(Equipos))-2)][0]} con un total de {Equipos[i-((len(Equipos))-2)][7]} puntos")
                    os.system("pause")
                else:
                    print("B. El equipo con mas puntos fue: ", Equipos[i-((len(Equipos))-1)][0], f"con un total de {Equipos[i-((len(Equipos))-1)][7]} puntos")
                    os.system("pause")
    # ORDEN SEGUN PARTIDOS GANADOS
    # TOTAL DE GOLES DE LOS EQUIPOS
    # PROMEDIO DE GOLES ANOTADOS (SUMA DE GOLES / SUMA PARTIDOS TOTALES)
        totalGoles = 0
        totalPartidos = 0
        for i,item in enumerate(Equipos):
            totalGoles += item[5]
            totalPartidos += item[1]
            for j in range(int(i+1), len(Equipos),1):
                if (Equipos[i][2] < Equipos[j][2]):
                    aux = Equipos[i]
                    Equipos[i] = Equipos[j]
                    Equipos[j] = aux
            if (i == ((len(Equipos))-1)):
                if ((Equipos[i - ((len(Equipos))-1)][2]) == (Equipos[j - ((len(Equipos))-2)][2])):
                    os.system("cls")
                    print("HAY DOS EQUIPOS CON LOS MISMOS PARTIDOS GANADOS")
                    print("C. los equipos con mas partidos ganados fueron: ", Equipos[i-((len(Equipos))-1)][0], f" con un total de {Equipos[i-((len(Equipos))-1)][2]}  partidos ganados")
                    print(" y el equipo: ", Equipos[i-((len(Equipos))-2)][0], f" con un total de {Equipos[i-((len(Equipos))-2)][2]}  partidos ganados")
                    os.system("pause")
                else:
                    print("C. El equipo con mas partidos ganados fue: ", Equipos[i-((len(Equipos))-1)][0], f" con un total de {Equipos[i-((len(Equipos))-1)][2]} partidos ganados")
                    os.system("pause")
                os.system("cls")
                print("D. El total de goles anotados por todos los equipos fue: ", totalGoles)
                print("E. El promedio de goles por partido es: ", totalGoles/totalPartidos )
                os.system("pause")
    
    else:
        print("Escoja una opcion valida")
        os.system('pause')