mat = [
    [1,2,3], # fila1
    [4,5,6], # fila2
    [7,8,9]  # fila3

]

print("Cantidad de filas: ", len(mat))
print("Cantidad de colimnas: ", len(mat[0]))
print("La posicion fila 1, columna 2 es:", mat[1][2])

for i in range(len(mat)):
    for j in range(len(mat[0])):
        print(mat[i][j], end= " ")
    print("\n")

