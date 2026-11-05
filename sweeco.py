matVentas = [
    [100,88,92,94,85,110,118],
    [30,42,31,32,38,40,37],
    [23,35,39,45,55,60,61],
    [45,50,56,65,47,57,68],
    [18,25,33,21,22,28,32]
]

lstPrecios = [1500,5000,6500,2500,22500]

def lstTotalesProdxSem(Ventas, Precios):
    fils = len(Ventas)
    cols = len(Ventas[0])
    lstTotales = []
    for f in range(fils):
        suma = 0
        for c in range(cols):
            suma += Ventas[f][c] * Precios[f]
        lstTotales.append(suma)

    return lstTotales

lstTotales = lstTotalesProdxSem(matVentas, lstPrecios)

maxTotal = max(lstTotales)
ProdVentMax = lstTotales.index(maxTotal) + 1

print(f"El producto {ProdVentMax} es el que más vende a la semana con ventas de ${maxTotal:,}")