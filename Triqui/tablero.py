# funcion crear tablero
# devuelve una matriz 3x3 numerada de 1 a 9
def crear_tablero():
    tablero = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"]
    ]
    return tablero

# funcion muestra el tablero en su estado actual
def mostrar_tablero(tablero):
    print()
    for f in range(3):
        for c in range(3):
            print(f" {tablero[f][c]}", end=" | ")
        print("\n---+----+----")

# coloca una ficha en el tablero y duelve True o False si se hizo
def colocar_ficha(tablero, posicion, ficha):
    if posicion < 1 or posicion > 9:
        return False # no se pudo colocar la ficha
    fila = (posicion - 1) // 3
    col = (posicion - 1) % 3

    if tablero[fila][col] != str(posicion): # esa posicion esta ocupada
        return False

    tablero[fila][col] = ficha
    return True

#tab = crear_tablero()
#mostrar_tablero(tab)
#pos = int(input("Elija una posicion"))
#colocar_ficha(tab, pos, "X")
#mostrar_tablero(tab)