# este es el programa principal donde llamaremos tadas las funcione
# para traer una funcion de otro subprograma tenemos que importar
import matematicas as math # "as math" es como un alias que usamos para escribir mas rapidamente la funcion cuando la llamemos
# las funciones son estrictas con el tipado y el dato debe ser el que pide la funcion 
# si el modulo esta en una carpeta, antes de escribir el nombre del modulo ponemos el nombre de la carptea segudi de "." y seguido del nombre del modulo
import menu as menu
import os
isRunning = True
while isRunning:
    op = menu.MenuPrincipal()
    if (op == "+"):
        num1 = int(input("ingrese nro 1: "))
        num2 = int(input("ingrese nro 2: "))
        print(f"la suma de {num1} + {num2} = {math.Operaciones(num1, num2, op)}")
        os.system("pause")
    if (op == "-"):
        num1 = int(input("ingrese nro 1: "))
        num2 = int(input("ingrese nro 2: "))
        print(f"la resta de {num1} + {num2} = {math.Operaciones(num1, num2, op)}")
        os.system("pause")
    if (op == "*"):
        num1 = int(input("ingrese nro 1: "))
        num2 = int(input("ingrese nro 2: "))
        print(f"la multiplicacion de {num1} + {num2} = {math.Operaciones(num1, num2, op)}")
        os.system("pause")
    if (op == "/"):
        num1 = int(input("ingrese nro 1: "))
        num2 = int(input("ingrese nro 2: "))
        print(f"la division de {num1} + {num2} = {math.Operaciones(num1, num2, op)}")
        os.system("pause")