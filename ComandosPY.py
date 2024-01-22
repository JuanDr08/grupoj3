import os
import json # una libreria que hace que al imprimir el diccionario se vea mas bonito
# declarar un diccionario
alumnos = {}
# declarar un dicicionario con informacion
# que sera luego agregado al diccionario anterior
alumno = {
    "codigo" : "123",   # si hay mas llaves por agregar nos toca poner ","
    "nombre" : "juan",
    "edad" : 13,
    "notas" : {
        "parciales" : [3.0, 4.5],
        "quices" : [],
        "trabajos" : []
    }
}
# imprime el diccionario principal, deberia estar vacio si no tiene nada
print(alumnos)
# imprimir todo el diccionario de notas que esta dentro del diccionario de alumno
print(alumno["notas"])
# imprimir una llave fija dentro de un diccionario que esta dentro de otro diccionario
print(alumno["notas"]["parciales"])
# recorrer una lista observando lo que en listas era la posicion o la u
for item in alumno:
    print(item) # imprime solo las llaves, no sus valores
# imprimir las llaves y alfrente sus valores correspondientes, accediendo al valor de las 
# llaves y a su nombre en un mismo for
for key in alumno:
    print(f"{key.capitalize()} : {alumno[key]}") # nos permite decir que agarremos el diccionario
                                                 # y accedamos al valor en el que esta key
# el .items de los diccionarios es como el enumerate de las listas, desestructura el diccionario
for key, valor in alumno.items():
    if ((type(valor) == str) or (type(valor) == int)): # si el tipo de valor de la llave en la que estemos es str o entero entonces lo va a imprimir
        print(f"{key.capitalize()} : {valor}")

# .update() nos permite agregar o modificar informacion en un diccionario
print(alumno.keys()) #forma de acceder solamente a las llaves del diccionario
print(alumno.get("telefono", "no se encuentra el valor")) # si la llave telefono no existe, nos dira que no se encuentra o lo quye pongamos despues de la ","
