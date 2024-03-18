# TikTakToe AI Algorithms
The **Minimax algorithm** is a technique used in strategy games to make optimal decisions; it operates on a search tree, where each node represents a game state and the branches are possible moves. The strategy of the algorithm is to minimize the maximum possible loss or maximize the minimum possible gain, recursively exploring the tree until reaching terminal game states and evaluating the utility of those states. **Alpha-beta pruning** is an enhancement of the Minimax algorithm that reduces unnecessary exploration of the game tree, using two parameters (alpha and beta) to represent the best-known values of maximizing and minimizing options, respectively.

This code implements the classic game of "*TicTacToe*", where a human player competes against an artificial intelligence (AI) that makes strategic decisions using the Minimax algorithm with alpha-beta pruning. The code also *includes functions to print the board, check available moves, evaluate the board state, and allow the human player to make their moves*. The AI makes strategic moves based on the Minimax algorithm with alpha-beta pruning, ensuring that the game is challenging and efficient.

# Included Codes
-  *MiniMax.py*: Demonstrates MiniMax search tree development and exploration, taking the entry vector "scores" as ending nodes.
-  *TikTakToeEvalFunc.py*: Asigns a value to a given board (+10 if 'x' wins, 0 if it is a tie and -10 if 'o' wins).
-  *MiniMaxTikTakToe.py*: Evaluates a given entry board, and calculates once the following optimal movement using MiniMax algorithm.
-  *TikTakToe.py*: Simple useable human vs AI TikTakToe game using MiniMax Algorithm.
-  *TikTakToeOptimizadoAB.py*: Human vs AI TikTakToe game using MiniMax Algorithm, enhanced with Alpha-Beta Prunning Method to diminish response time.
-  *TikTakToeOptimizadoABinfalible.py*: Human vs AI TikTakToe game using MiniMax Algorithm, enhanced with Alpha-Beta Prunning Method to diminish response time. The code analyses 2-level possibilities depth, aking it impossible to defeat the algorithm (whenever the first move, which is aleatory, takes place on a corner).
