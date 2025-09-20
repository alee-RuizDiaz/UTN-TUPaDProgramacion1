#9) Representar un tablero de Ta-Te-Ti como una lista de listas (3x3).
#• Inicializarlo con guiones "-" representando casillas vacías.
#• Permitir que dos jugadores ingresen posiciones (fila, columna) para colocar "X" o "O".
#• Mostrar el tablero después de cada jugada.

tablero = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

print("Tablero inicial:")
print(tablero[0])
print(tablero[1])
print(tablero[2])
print()

#Turnos de jugador X
for turno in range(9):
    print("Turno del jugador X")
    fila = int(input("Ingrese fila (0-1-2): "))
    col = int(input("Ingrese columna (0-1-2): "))
    if tablero[fila][col] == "-":
        tablero[fila][col] = "X"
    else:
        print("Casilla ocupada.")

    print(tablero[0])
    print(tablero[1])
    print(tablero[2])
    print()

    # Turno jugador O
    print("Turno del jugador O")
    fila = int(input("Ingrese fila (0-1-2): "))
    col = int(input("Ingrese columna (0-1-2): "))
    if tablero[fila][col] == "-":
        tablero[fila][col] = "O"
    else:
        print("Casilla ocupada.")
    
    print(tablero[0])
    print(tablero[1])
    print(tablero[2])
    print()

print("Juego terminado")