from Knight import Knight
from Board import Board

import random

# Run the algorithm on a nxn board with a certain success threshold
def run(n, success_threshold, run_count):
    # Create a new Board object and put a new Knight object in it
    board = Board(n, Knight(random.randint(0, n-1), random.randint(0, n-1)))
    # Move the knight randomly until it gets stuck
    while board.moveKnightRandomly():
        pass
    # Write the result for the run
    board.writeResults(success_threshold, run_count)
    # Return if the run was successful
    return board.trace / (board.size ** 2) > success_threshold
