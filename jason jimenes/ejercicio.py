"""
Desarrolle en python un juego de Triqui para dos personas.
Los jugadores se turnan para marcar una casilla: una usaX y la otra usa O.

El tablero es de 3x3. En cada turno, el programa debe mostrar 
el tablero y pedir al jugador que elija una casilla vacia.
Si esta ocupada o la opcion no es valida, debe pedir que lo intente de nuevi.

El juego termina cuando un jugador complete una fila, una columna o una diagonal.
o cuando se tienen todas las casillas sin que haya un ganador.

Al final el programa debe anunciar quien gano o si hubo empate.

Organiza el codigo con estos modulos:
*triqui.py : es el programa que inicia el juego
*tablero.py : muestra y actualiza el tablero
*juego.py : controla los turnos, valida la jugada y determina el resultado

"""
