#El código busca asignar un valor [10,0,-10] a un N tablero dado.

def evaluate(tab):
    # Busca ganador X (+10) o O (-10) en filas y columnas respectivamente: tab [fila] [columna]
    for i in range(3):
        if tab[i][0] == tab[i][1] == tab[i][2] or tab[0][i] == tab[1][i] == tab[2][i]:
            if tab[i][i] == 'x':
                return 10
            elif tab[i][i] == 'o':
                return -10

    # Busca ganador X (+10) o O (-10) en diagonales derecha e izquierda respectivamente.
    if tab[0][0] == tab[1][1] == tab[2][2] or tab[0][2] == tab[1][1] == tab[2][0]:
        if tab[1][1] == 'x':
            return 10
        elif tab[1][1] == 'o':
            return -10

    # En caso de no existir un ganador.
    return 0

# Driver code
if __name__ == "__main__":
    tab = [['x', '_', 'o'],
           ['_', 'x', 'o'],
           ['_', '_', '_']]
      
    value = evaluate(tab) #Valor del tablero.
    print("Valor: ", value)


#######################################################################################
#######################################################################################

# El valor de acciones se calcula de acuerdo a posibles posiciones de las piezas en el tablero (función heurística).
#Se considera X MAX y O MIN.
# Se asignan valores a posibles tableros ||| X gana = +10, O gana = -10, tie = 0.
#Se representa tablero en matriz 3X3.
#X y O sólo pueden ganar en vertical(3 col), horizintal (3 fil) o diagonal (2 diag).

# Based on algorithms by:
#Rituraj Jain - https://www.geeksforgeeks.org/introduction-to-evaluation-function-of-minimax-algorithm-in-game-theory/
