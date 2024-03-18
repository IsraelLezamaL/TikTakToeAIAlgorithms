import random #El primer tiro IA de la partida será aleatorio.

# IMPRESIÓN DE TABLERO
def print_board(board):
    print('-------------')
    print('|', board[0], '|', board[1], '|', board[2], '|')
    print('-------------')
    print('|', board[3], '|', board[4], '|', board[5], '|')
    print('-------------')
    print('|', board[6], '|', board[7], '|', board[8], '|')
    print('-------------')
  
#CONFIRMACIÓN DE TABLERO INCOMPLETO 
def isMovesLeft(board) :
    #Busca celdas vacías.
    return ' ' in board
  
#FUNCIÓN DE EVALUACIÓN DE TIK TAK TOE
def evaluate(board): #X = +10, O=-10
    # Filas
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2] == 'x':
            return 10
        elif board[i] == board[i + 1] == board[i + 2] == 'o':
            return -10

    # Columnas
    for i in range(3):
        if board[i] == board[i + 3] == board[i + 6] == 'x':
            return 10
        elif board[i] == board[i + 3] == board[i + 6] == 'o':
            return -10

    # Diagonales \ y / respectivamente.
    if board[0] == board[4] == board[8] == 'x' or board[2] == board[4] == board[6] == 'x':
        return 10
    elif board[0] == board[4] == board[8] == 'o' or board[2] == board[4] == board[6] == 'o':
        return -10

    # EMPATE
    return 0

  
# ALGORITMO MINIMAX
def minimax(board, depth, isMax, ur, user):
    # BUSCA GANADOR: Calcula el valor del tablero actual y lo almacena en score. Si es diferente de cero, hay un ganador, la función retorna +10 (X) o -10 (0) sin explorar más el árbol.
    score = evaluate(board)
    if score != 0:
        return score
    # BUSCA EMPATE O JUEGO EN PROCESO: Verifica si no hay movimientos disponibles en el tablero. Si no, el juego está empatado y la función retorna 0 (TIED).
    if not isMovesLeft(board):
        return 0
    
    # Inicializa la variable best con un valor muy bajo es turno maximizador y muy alto si es turno minimizador.
    best = float('-inf') if isMax else float('inf')
    # HALLA MOVIMIENTO ÓPTIMO: Itera todo el tablero, realizando un movimiento en cada celda vacía.
    for i in range(9):
        if board[i] == ' ':
            board[i] = ur if isMax else user  # Coloca una X si UR u O si user.
            # Llama minimax recursivamente para el siguiente nivel del árbol de juego, tras realizar su movimiento en celda actual.
            # El valor retornado actualiza la variable best. Maximizador utiliza el valor máximo entre best y el resultado de la llamada recursiva. Minimizador usa el valor mínimo.
            best = max(best, minimax(board, depth + 1, not isMax, ur, user)) if isMax else min(best, minimax(board, depth + 1, isMax, ur, user))
            board[i] = ' '  # Revierte el movimiento realizado.
    return best  # Generará en cada celda vacía un resultado [10, 0, -10] y seleccionará el valor óptimo.

# MOVIMIENTO AI  
def findBestMove(board, ur, user):
    # INICIALIZACIÓN DE VARIABLES
    bestVal = float('-inf')  # Mejor valor (infinitamente bajo).
    bestMove = None  # Mejor movimiento (no existente en tablero).
    for i in range(9):
        if board[i] == ' ':
            board[i] = ur
            moveVal = minimax(board, 0, False, ur, user)
            board[i] = ' '
            if moveVal > bestVal:  # El mejor valor toma el puesto del movimiento por realizar; similar al algoritmo best fit.               
                bestMove = i 
                bestVal = moveVal
    if bestMove is not None:     # Realiza el movimiento en el tablero después de encontrar la mejor jugada.
        board[bestMove] = ur

    print(f"PC´s AI has chosen: {bestMove + 1} \n")  
    print_board(board)

# MOVIMIENTO HUMANO
def make_move(board, user):
    while True:
        move = int(input(f"Player {user}, enter your move (1-9): "))
        if 1 <= move <= 9 and board[move - 1] == ' ': #Marca en la selección del usuario si es válida y la celda está vacía.
            board[move - 1] = user
            break
        else:
            print("Invalid move. Try again.")
    print_board(board)
    
#LÓGICA DE JUEGO
def TicTacToe():
    board = [' '] * 9  # TABLERO
    ur, user = 'x', 'o'  # MAXIMIZADOR, MINIMIZADOR
    
    print("Let's Start!")
    print_board(board)

    current_player = ur  # Initialize the current player (empieza la PC).

    while True:
        if evaluate(board) == 10:
            print("Player UR5 wins!")
            break
        elif evaluate(board) == -10:
            print("Player USER wins!")
            break
        elif not isMovesLeft(board):
            print("It's a tie!")
            break

        if current_player == user:
            make_move(board, current_player)
        else:
            if sum(cell == ' ' for cell in board) >= 8: #Verifica si 2 o más celdas están vacias.
                empty_cells = [i for i in range(9) if board[i] == ' '] #Crea listado de celdas vacias.
                random_move = random.choice(empty_cells) #Elige aleatoriamente la posición del primer tiro de la PC.
                board[random_move] = ur
                print(f"PC has RANDOMLY chosen: {random_move + 1} \n")
                print_board(board)
            else:
                findBestMove(board, ur, user) #Genera movimientos de PC con IA.

        current_player = user if current_player == ur else ur            

#MAIN
TicTacToe()
  
#######################################################################################
#######################################################################################

# Based on algorithms by:
#Rituraj Jain - https://www.geeksforgeeks.org/introduction-to-evaluation-function-of-minimax-algorithm-in-game-theory/
#divyesh072019 - https://www.geeksforgeeks.org/finding-optimal-move-in-tic-tac-toe-using-minimax-algorithm-in-game-theory/
#Noble Biru - https://github.com/noble-ch/Complete-Python-And-Artificial-Intelligence-tik-tak_toe_AI/blob/main/game_logic.py
