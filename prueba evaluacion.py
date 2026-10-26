def consultartinv(inventario):
    print("Hay ",inventario,"unidades en inventario")
    input("Presione enter para continuar")
    return inventario

def agregar(inventario,agreg):
    if agreg<=0:
        print("No puedes agregar cantidades menores o iguales a cero ")
        input("Presione enter para continuar")
        return inventario
    else:
        inventario=inventario+agreg
        print("Se agregaron las unidades al inventario, ahora hay ",inventario,"unidades en inventario")
        input("Presione enter para continuar")
    return inventario

def vender(inventario,vend):
    if vend<=0:
        print("No puedes vender cantidades menores o iguales a cero ")
        input("Presione enter para continuar")
        return inventario
    elif vend>inventario:
        print("inventario insuficiente")
        input("Presione enter para continuar ")
    else:
        inventario=inventario-vend
        print("Se vendieron ",vend,"unidades del producto. \n Quedan ",inventario,"Unidades en inventario.")
        input("Presione enter para continuar")
    return inventario

inventario=50
opcion=""

while opcion!=0:
    print("""===== INVENTARIO DE TIENDA =====

1. CONSULTAR INVENTARIO
2. VENDER PRODUCTOS
3. AGREGAR PRODUCTOS
0. SALIR

""")

    opcion=int(input("Seleccione una opción:"))
    match opcion:
        case 1:
            inventario=consultartinv(inventario)
        case 2:
            vend=int(input("Cuantas unidades desea vender? "))
            inventario=vender(inventario,vend)
        case 3:
            agreg=int(input("Cuantas unidades desea agregar al inventario? "))
            inventario=agregar(inventario,agreg)
        case 0 :
            print("Gracias por usar el Sistema de inventarios cotiles")
        case _:
            print("Opcion invalida")
            input("Presione enter para volver al menu")