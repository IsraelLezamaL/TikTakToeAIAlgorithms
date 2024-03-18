player, opponent = 'x', 'o' #MAXIMIZADOR, MINIMIZADOR
  
#CONFIRMACIÓN DE TABLERO INCOMPLETO 
def isMovesLeft(board) : #tab [fila] [columna]
    #Busca celdas vacías.
    for i in range(3) : 
        for j in range(3) : 
            if (board[i][j] == '_') : 
                return True 
    return False
    # Añternativo: 
  
#FUNCIÓN DE EVALUACIÓN DE TIK TAK TOE
def evaluate(tab):
    # Busca ganador X (+10) o O (-10) en filas y columnas respectivamente: tab [fila] [columna]
    # Busca ganador X (+10) o O (-10) en diagonales derecha e izquierda respectivamente.
    for i in range(3):
        if tab[i][0] == tab[i][1] == tab[i][2] or tab[0][i] == tab[1][i] == tab[2][i] or tab[0][0] == tab[1][1] == tab[2][2] or tab[0][2] == tab[1][1] == tab[2][0]:
            if tab[i][i] == 'x' or tab[1][1] == 'x':
                return 10
            elif tab[i][i] == 'o' or tab[1][1] == 'o':
                return -10

    # En caso de no existir un ganador.
    return 0
  
# MINI MAX ALGORITHM
def minimax(board, depth, isMax):
    #BUSCA GANADOR: Calcula el valor del tablero actual y lo almacena en score. Si es diferente de cero, hay un ganador, la función retorna +10 (X) o -10 (0) sin explorar más el árbol.
    score = evaluate(board)
    if score != 0:
        return score
    #BUSCA EMPATE O JUEGO EN PROCESO: Verifica si no hay movimientos disponibles en el tablero. Si no, el juego está empatado y la función retorna 0 (TIED).
    if not isMovesLeft(board):
        return 0
    #Inicializa la variable best con un valor muy bajo es turno maximizador y muy alto si es turno minimizador.
    best = float('-inf') if isMax else float('inf')
    #HALLA MOVIMIENTO ÓPTIMO: Itera todo el tablero, realizando un movimiento en cada celda vacía.
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                board[i][j] = player if isMax else opponent #Coloca una X si player u O si oponent.
                #Llama minimax recursivamente para el siguiente nivel del árbol de juego, tras realizar su movimiento en celda actual.
                #El valor retornado actualiza la variable best. Maximizador utiliza el valor máximo entre best y el resultado de la llamada recursiva. Minimizador usa el valor mínimo.
                best = max(best, minimax(board, depth + 1, not isMax)) if isMax else min(best, minimax(board, depth + 1, isMax))
                board[i][j] = '_' #Revierte el movimiento realizado.
    return best #Generará en cada celda vacía un resultado [10, 0, -10] y seleccionará el valor óptimo.

#MOVIMIENTO ÓPTIMO  
def findBestMove(board):
    #INICIALIZACIÓN DE VARIABLES
    bestVal = float('-inf') #Mejor valor (infinitamente bajo).
    bestMove = (-1, -1) #Mejor movimiento (no existente en tablero).
    for i in range(3):
        for j in range(3):
            if board[i][j] == '_':
                board[i][j] = player
                moveVal = minimax(board, 0, False)
                board[i][j] = '_'
                if (moveVal > bestVal) :  #El mejor valor toma el puesto del movimiento por realizar; similar al algoritmo best fit.               
                    bestMove = (i, j) 
                    bestVal = moveVal
    print("The Optimal Move is :", bestVal, "\n")  

    return bestMove


board = [ 
    [ 'x', 'o', 'x' ],  
    [ 'o', '_', 'o' ],  
    [ 'x', '_', '_' ]  
] 
  
bestMove = findBestMove(board)  
  
print("ROW:", bestMove[0], " COL:", bestMove[1])
  
#######################################################################################
#######################################################################################

# Based on algorithms by:
#Rituraj Jain - https://www.geeksforgeeks.org/introduction-to-evaluation-function-of-minimax-algorithm-in-game-theory/
#divyesh072019 - https://www.geeksforgeeks.org/finding-optimal-move-in-tic-tac-toe-using-minimax-algorithm-in-game-theory/
