altura = int(input("Ingrese la altura del triangulo -> "))
base = int(input("Ingrese la base del triangulo -> "))

area = (base * altura) / 2

if (area > 1000):
    print("DATOS NO VALIDOS")
else:
    print("El area del triangulo equilatero es -> ", area)
    
