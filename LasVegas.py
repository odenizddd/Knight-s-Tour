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

# Define board size
n = 8

# Define success threshold
success_threshold = 0.7
# Clear the output file
with open(f"results_{success_threshold}.txt", "w") as file:
    pass
# Run the actual simulation
number_of_runs = 100000
successful_runs = 0
for i in range(number_of_runs):
    if run(n, success_threshold, i+1):
        successful_runs += 1
print(f"LasVegas Algorithm With p = {success_threshold}")
print(f"Number of successful tours: {successful_runs}")
print(f"Number of trials: {number_of_runs}")
print(f"Probability of a successful tour: {successful_runs/number_of_runs}")
