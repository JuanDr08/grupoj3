import os
titulo = """
    +++++++++++++++++++++++++++
    +   Ingrese 5 voltajes    +
    +++++++++++++++++++++++++++
"""
Activo = True
suma = 0
total = 0
while Activo:
    os.system("cls")
    print(titulo)
    if(total < 5):
        numero = int(input("ingrese un voltaje -> "))
        suma = suma + numero
        total += 1
        
    else:
        print("Ya ha ingresado los voltajes requeridos, acontinuacion vera el resultado de la informacion recaudada")
        os.system("pause")
        Activo = False
if ((suma/total) > 220):
    print("ALTO VOLTAJE")
else:
    print("VOLTAJE CORRECTO")
        