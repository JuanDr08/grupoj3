def Operaciones(numero1:int, numero2:int, operador:str): # entre parentesis van los datos que vamos a utilizar, y en los dos puntos el tipo de dato
    if (operador == "+"):
        return numero1 + numero2
    elif (operador == "-"):
        return numero1 - numero2
    elif (operador == "*"):
        return numero1 * numero2
    elif (operador == "/"):
        return numero1 / numero2