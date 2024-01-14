from Knight import Knight
from Board import Board
import random

# Backtracing algorithm
def backtrack(board, success_threshold):
    if board.trace >= (board.size ** 2) * success_threshold:
        return True
    for nextPos in board.getPossibleCells():
        board.moveKnight(nextPos[0], nextPos[1])
        if backtrack(board, success_threshold):
            return True
        board.rollback()
    return False

def run(args):
    n = args[0]
    run_count = args[1]
    p = args[2]
    k = args[3]
    success_count = 0
    for i in range(run_count):
        board = Board(n, Knight(random.randint(0, n-1), random.randint(0, n-1)))
        for j in range(k):
            board.moveKnightRandomly()
        if backtrack(board, p):
            success_count += 1
    print(f"LasVegas Algorithm With p = {p}, k = {k}")
    print(f"Number of successful tours: {success_count}")
    print(f"Number of trials: {run_count}")
    print(f"Probability of a successful tour: {success_count/run_count}\n")
    return success_count
