import os # si yo importo desde aca el os lo puedo usar en todas las demas carpetas sin problema, usando esta forma menu.os.system() y asi no hace falta importarlo en todas
def MenuPrincipal():
    os.system("cls")
    operaciones = ["+. suma\n-. resta\n*. multiplicacion\n/. division"]
    for item in operaciones:
        print(item)
    return input(":)_")