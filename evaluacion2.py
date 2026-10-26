def entrada(cupo):
    if cupo>=10:
        print("Parqueadero lleno")
        input("presione enter para continuar ")
    elif cupo<=10:
        print("Cupo disponible")
        input("presione enter para registar la entrada  ")
        cupo=cupo+1
        input("presione enter para continuar  ")
    return cupo

def salidacupo(cupo):
    if cupo>0:
        input("Presione enter para registrar la salida")
        cupo=cupo-1
        input("presione enter para continuar ")
    elif cupo<=0:
        input("Salida invalida, no hay vehiculos en el parqueadero ")
        input("presione enter para continuar  ")
    return cupo

def salidarecaudo(horas,recaudo):
    if horas>0:
        print("se deben pagar ",horas,"horas")
        recaudo=recaudo+(horas*3000)
        print("se deben pagar ",(horas*3000),"pesos")
        input("presione enter para continuar ")
    elif horas<=0:
        print("Tiempo invalido, debe ser positivo!!")
        input("presione enter para continuar  ")
    return recaudo

def consultaroparq(cupo):
    print("Hay ",cupo,"carros parqueados, quedan",10-cupo,"cupos ")
    input("Presione enter para continuar")
    return cupo

def consultarrecaudo(recaudo):
    print("Hay un recaudo de ",recaudo,"pesos")
    input("Presione enter para continuar")
    return recaudo

cupo=0
recaudo=0
opcion=-1

while opcion!=0:
    print("""
    ===== PARQUEADERO CENTRAL =====

1. REGISTRAR ENTRADA
2. REGISTRAR SALIDA
3. CONSULTAR PARQUEADERO
4. CONSULTAR RECAUDO
5. SALIR
    """)
    opcion=int(input("Seleccione una opción: "))

    match opcion:
        case 1:
            cupo=entrada(cupo)
        case 2:
            if cupo <=0:
                print("Salida invalida, no hay vehiculos en el parqueadero ")
                input("Presione enter para continuar")
            elif cupo >0:
                horas=int(input("Cuantas horas estuvo el vehiculo? "))
                if horas>0:
                    recaudo=salidarecaudo(horas,recaudo)
                    cupo=salidacupo(cupo)
                elif horas<=0:
                    print("Tiempo invalido, debe ser positivo!!")
                    input("presione enter para continuar  ")
        case 3:
            cupo=consultaroparq(cupo)
        case 4:
            recaudo=consultarrecaudo(recaudo)
        case 0:
            print("Gracias por parqueaderos el COTO")
        case _:
            print("Opcion invalida")
            input("Presione enter para volver al menu")