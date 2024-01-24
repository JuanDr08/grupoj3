import os
titulo = """
    +++++++++++++++++++++++++++++++++++++
    +   Ingrese 3 voltajes distintos    +
    +++++++++++++++++++++++++++++++++++++
"""
Activo = True
numero = 0
suma = 0
total = 0
while Activo:
    os.system("cls")
    print(titulo)
    if(total < 3):
        numeroNuevo = int(input("ingrese un voltaje -> "))
        if (numeroNuevo != numero):
            numero = numeroNuevo
            suma = suma + numeroNuevo
            total += 1
        else:
            print("Ingrese un voltaje distinto")
            os.system("pause")        
    else:
        print("Ya ha ingresado los voltajes requeridos, acontinuacion vera el resultado de la informacion recaudada")
        os.system("pause")
        Activo = False
if ((suma/total) < 115):
    print("VOLTAJE CORRECTO")
elif (((suma/total) > 115) and ((suma/total)) < 220):
    print("ALTO VOLTAJE")
else:
    print("PELIGRO")