while True:
    try:
        num = int(input("Ingresa un numero entero: "))
        break
    except ValueError:
        print("Error. Entero invalido... \n")