while True:
    try:
        num = int(input("Ingrese el numerador: "))
        den = int(input("Ingrese el denominador: "))

        res = num//den
        #cadena f string, deja hcolocar variables dentro de un string(texto)
        print(f"El resultado de la division es: {res}" )
        break
    except ValueError, ZeroDivisionError:
        print("Error. Ingrese un entero valido")

    finally: #Se ejecuta siempre, sin importar si hay o no una excepcion
        print("Fin de todo")

print("Fin de la division")