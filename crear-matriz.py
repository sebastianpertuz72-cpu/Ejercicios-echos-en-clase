def crearmatriz(filas, colums, valor=0):
    mat = []
    for f in range(filas):
        mat.append([valor] * colums)
    return mat

def imprimirmatriz (matriz):
    filas = len(matriz)
    colums = len(matriz[0])
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            print(matriz[i][j], end= " ")
        print("\n")

filas = int(input("Cantidad de filas? "))
columnas = int(input("Cantidad de columnas? "))

matriz = crearmatriz(filas, columnas)
imprimirmatriz(matriz)