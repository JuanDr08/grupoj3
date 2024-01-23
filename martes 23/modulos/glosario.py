import os
def AddWord(origen : dict):
   
    word = input("ingrese la palabra -> ").upper()
    if (word[0:1]) != " ":
        if (origen.get(word[0:1], -1)):
            data.update({word : {}})
        # key = str(word).replace(" ", "")
        data = origen.get(word[0:1])
        significado = input("ingrese el significado -> ")
        wordAdd = {
            "palabra" : word,
            "significado" : significado
        }
        data.update({word : wordAdd})
    else:
        print("El primer caracter no puede ser en blanco")
        os.system("pause")

def DelWord(origen : dict):
    palabra = input("ingrese la palabra que va a eliminar -> ").upper()
    origen.get(palabra[0:1]).pop(palabra)
    

def SearchWord(origen : dict):
    palabra = input("ingrese la palabra que desea buscar -> ").upper()
    print(origen.get(palabra[0:1]).get(palabra)["significado"])
    os.system("pause")