import os
import json
os.system("cls")
federacion = {}
# dentro de federacion van a ir todos los equipos
# equipos, pj, pg, pp, pe, gf, gc, tp
AddAnotherOne = True
while AddAnotherOne:
    nombre = str(input("ingrese el nombre del equipo: "))
    equipo = {
        "nombre" : nombre,
        "pj" : 0,
        "pg" : 0,
        "pp" : 0,
        "pe" : 0,
        "gf" : 0,
        "gc" : 0,
        "tp" : 0
    }
    AddAnotherOne = bool(input("desea agregar otro equipo s(si) enter(no)")) # python toma las entradas de cadena por terminal como verdadero y si no se ingresa nada lo toma como falso
    # print(equipo)                # si yo hago esto esta bien, pero al ingresar otro equipo va a sobre escribir el anterior, entonces toca agregar ese equipo que se creo a una
    # federacion.update(equipo)   # llave en federacion para que se guarden
    # print(federacion)
    federacion.update({str(len(federacion)+1).zfill(4) : equipo}) # lo que hacemos es poner todo entre llaves para crear una nueva llave en federacion con valor equivo, y
    # el nombre de esa llave va a ser un codigo, que segun sea la longitud de federacion le va a agregar 0s y aumentando, asi obteniendo un codigo para cada equipo
    # y que cada codigo contenga la informacion de un equipo distinto
print(json.dump(federacion,indent = 4)) # la funcion json nos hara ver el diccionario como es en verdad y organizada, el indent usarlo con 4 como predeterminado