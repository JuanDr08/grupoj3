import os

titulo = """
    +++++++++++++++++++++++++++++++++++++
    +  Federacion De Futbol Colombiano  +
    +++++++++++++++++++++++++++++++++++++
"""

opciones = "1- Registrar un equipo\n2- Registrar una fecha\n3- Tabla de posiciones\n4- Reporte"

Encendido = True
Equipos = []
while Encendido:
    os.system('cls')
    print(titulo)
    print(opciones)
    opcion = int(input("-"))
    if (opcion == 1):
        os.system("cls")
        nombreEquip = str(input("Ingrese el nombre del equipo: "))             # pedir nombre
        Equipos.append([nombreEquip.upper(), 0, 0, 0, 0, 0, 0, 0])      # registrar equipo con datos en 0
    elif(opcion == 2):
        os.system("cls")
        for i, item in enumerate(Equipos): # Disponibilidad
            print("Equipos disponibles: ", item[0])
        vsLocal = str(input("Ingrese el equipo que jugara de Local: "))             # Ingreso contrincantes
        vsVisitante = str(input("Ingrese el equipo que jugara de visitante: "))     # Ingreso contrincantes
        for i, item in enumerate(Equipos):                           
            if (vsLocal.upper() in item):                                # verificacion de existencia
                item[1] += 1                                             # Aumento partidos jugados
                print("equipo registrado correctamente")
            elif (vsVisitante.upper() in item):                                # verificacion de existencia
                item[1] += 1                                             # Aumento partidos jugados
                print("equipo registrado correctamente")
                os.system("pause")
        os.system("cls")
        marcadorLocal = int(input(f"Ingrese el marcador del equipo {vsLocal}"))
        marcadorVisitante = int(input(f"Ingrese el marcador del equipo {vsVisitante}")) 
        for i, item in enumerate(Equipos):                              
            if ((vsLocal.upper() in item) or (vsVisitante.upper() in item)):
                if (item == vsLocal.upper()):
                    item[5] += marcadorLocal
                    item[6] += marcadorVisitante
                elif (item == vsVisitante.upper()):
                    item[6] += marcadorLocal
                    item[5] += marcadorVisitante
                if (marcadorLocal > marcadorVisitante):
                    item[2] += 1
                    item[7] += 3
                elif (marcadorLocal < marcadorVisitante):
                    item[3] += 1
                    item[7] += 3
                elif (marcadorLocal == marcadorVisitante):
                    item[4] += 1
                    item[7] += 1                        
    elif(opcion == 3):
        pass
    elif(opcion == 4):
        pass
    else:
        print("Escoja una opcion valida")
        os.system('pause')