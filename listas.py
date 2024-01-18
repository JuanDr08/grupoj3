import os
os.system('cls')
titulo = """
    ++++++++++++++++++++++++++++
    +  OPERACIONES CON LISTAS  +
    ++++++++++++++++++++++++++++
"""
opciones = "1. Agregar camper\n2. Eliminar camper\n3. Buscar camper\n4. Salir"
isActivate = True
campers = []
while isActivate:
    os.system('cls')
    print(titulo)
    print(opciones)
    op = int(input("-"))
    if (op ==1) :
        id = str(len(campers)).zfill(5)
        nombre = input("Ingrese Nombre del camper: ")
        campers.append([id,nombre])
    elif (op == 2) :
        nombre = input("ingrese nombre del camper a eliminar: ")
        for i,item in enumerate(campers):
            if (nombre in item) :
                campers.pop(i)
                break
    elif (op == 3) :
        nombre = input("ingrese nombre del camper a buscar: ")
        for item in campers:
            if(nombre in item) :
                print(f"Codigo : {item[0]}")
                print(f"Nombre : {item[1]}")
                os.system('pause')
    elif (op == 4) :
        isActivate = False
        print("Gracias por usar mi programa...")
        os.system('pause')
    else: 
        os.system('cls')
        print("La opcion ingresada no es valida")
        os.system('pause')