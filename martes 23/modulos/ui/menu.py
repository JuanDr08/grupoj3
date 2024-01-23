opciones = ["1. Agregar palabra\n2. Buscar palabra\n3. Borrar palabra\n4. Salir"]
def MenuPrincipal()->int:
    titulo = """
        ++++++++++++++++++++++++++++++++++++++++++++
        +   DICCIONARIO TECNICO DE PROGRAMACION    +
        ++++++++++++++++++++++++++++++++++++++++++++ 
"""
    print(titulo)
    for item in opciones:
        print(item)
    op = int(input("-> "))
    return op