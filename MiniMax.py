# Importa librería MATH para cálculos con logaritmos.
import math

# Función MiniMax: Halla el valor óptimo dentro de un árbol de juego.
def minimax(cur_depth, node_index, is_maximizing, scores, target_depth): #Profundidad Actual, Índice de Nodo, Indicador de Turno, Scores, Profundidad Deseada.
    # Caso Base: Se alcanza la profundidad deseada, devuelve el score del nodo actual.
    if cur_depth == target_depth: #Si se ha llegado a un nodo hoja, devuelve el valor del nodo. Inician cálculos de propagación inversa del árbol y finaliza exploración recursiva del árbol.
        return scores[node_index]

    # TURNO MAXIMIZADOR
    if is_maximizing:
        # Devuelve el valor MÁXIMO entre los scores de 2 nodos hijos.
        return max(
            minimax(cur_depth + 1, node_index * 2, False, scores, target_depth), #Representa el cálculo del valor del nodo hijo izquierdo en el árbol del juego (cur_depth + 1 => estamos descendiendo un nivel en el árbol, node_index * 2 => calcula el índice del nodo hijo izquierdo, False => ahora es turno del jugador minimizador.)
            minimax(cur_depth + 1, node_index * 2 + 1, False, scores, target_depth) #Similar a la primera llamada recursiva, esta parte representa el cálculo del valor del nodo hijo derecho.
        )
    # TURNO MINIMIZADOR
    else:
        # Devuelve el valor MÍNIMO entre los scores de 2 nodos hijos.
        return min(
            minimax(cur_depth + 1, node_index * 2, True, scores, target_depth),
            minimax(cur_depth + 1, node_index * 2 + 1, True, scores, target_depth)
        )

# Función de Obtención de Valores Óptimos usando algoritmo MiniMax.
def optimal_value(scores):
    tree_depth = int(math.log2(len(scores))) #Cálculo de profundidd del árbol dada su estructura con 2 nodos en cada ramificación.
    # Return the optimal value by calling the minimax function
    return minimax(0, 0, True, scores, tree_depth) #La profundidad deseada, será la profundidad del árbol; a fin de recorrerlo todo. Inicia turno el jugador Maximizador.

# Driver code
scores = [3, 5, 2, 9, 5, 6, 7, 8,11,12,13,1] #Valores de nodos hoja.Si no hay nodo comparativo, se coloca 0 en nodo hijo derecho.
print("Valor Óptimo:", optimal_value(scores)) #RESULTADO

#######################################################################################
#######################################################################################

# En el algoritmo MiniMax, la multiplicación de node_index * 2 en la llamada recursiva minimax se utiliza para calcular el índice del nodo hijo izquierdo en el árbol del juego. Esto está relacionado con la forma en que se estructura el árbol de juego en la representación binaria.
#En un árbol de juego típico, cada nodo tiene dos hijos: uno a la izquierda y otro a la derecha. Para representar esta estructura de árbol en un arreglo (como en el caso de la lista scores), se utiliza la siguiente fórmula:
#El hijo izquierdo de un nodo en la posición i se encuentra en la posición 2 * i.
#El hijo derecho de un nodo en la posición i se encuentra en la posición 2 * i + 1.

# Based on MiniMax Algorithm by rootshadow: https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-1-introduction/
# https://www.javatpoint.com/mini-max-algorithm-in-ai
