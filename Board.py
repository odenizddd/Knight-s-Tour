import random

class Board:
    # Initialize the board
    def __init__(self, n, knight):
        # Side length of the board
        self.size = n
        # Two dimensional array that represents the chessboard
        self.grid = [[-1 for i in range(self.size)] for j in range(self.size)]
        # The single knight on the board
        self.knight = knight
        # Mark the initial position of the knight
        self.grid[self.knight.row][self.knight.col] = 0
        # The number of the next move
        # Notice how it also equal the number of cells visited by the knight so far
        self.trace = 1
        # The list of all the cells the knight visits
        self.history = [[self.knight.row, self.knight.col]]

    # Display the board
    def print(self):
        for i in range(self.size):
            print(self.grid[i])

    # Move the knight to its new position and mark it on the board
    def moveKnight(self, row, col):
        self.knight.move(row, col)
        self.grid[row][col] = self.trace
        self.trace += 1
        self.history.append([row, col])

    # Discover and return a list of possible cells that the knight can move next
    # Also sort the list according to the number of neighbours of each cell
    # Cells with less neighbours are visited first
    # Warnsdorff's Algorithm
    def getPossibleCells(self):
        return sorted(list(filter(
            lambda pos: (0 <= pos[0] < self.size) and (0 <= pos[1] < self.size) and (self.grid[pos[0]][pos[1]] == -1),
        [
            [self.knight.row-2, self.knight.col+1], [self.knight.row-1, self.knight.col+2],
            [self.knight.row+1, self.knight.col+2], [self.knight.row+2, self.knight.col+1],
            [self.knight.row+2, self.knight.col-1], [self.knight.row+1, self.knight.col-2],
            [self.knight.row-1, self.knight.col-2], [self.knight.row-2, self.knight.col-1]
        ]
        )), key=self.getNeighbourCount)
    
    # Move the knight randomly to one of the available positions
    # Return false if no position is available
    def moveKnightRandomly(self):
        possibleCells = self.getPossibleCells()
        if not possibleCells:
            return False
        nextPos = random.choice(possibleCells)
        self.moveKnight(nextPos[0], nextPos[1])
        return True
    
    # Write the results into the output file
    def writeResults(self, success_threshold, run_count):
        filename = f"results_{success_threshold}.txt"
        with open(filename, "a") as file:
            file.write(f"Run {run_count}: starting from ({self.history[0][0]},{self.history[0][1]})\n")
            for i in range(1, len(self.history)):
                file.write(f"Stepping into ({self.history[i][0]},{self.history[i][1]})\n")
            file.write(("Successful" if self.trace / (self.size ** 2) > success_threshold else "Unsuccessful") + f" - Tour length: {self.trace}\n")
            for i in range(self.size):
                file.write(" ".join([str(el).rjust(2) for el in self.grid[i]]) + "\n")
            file.write("\n")

    # Take one step back
    def rollback(self):
        lastPos = self.history.pop()
        self.grid[lastPos[0]][lastPos[1]] = -1
        self.trace -= 1
        self.knight.move(lastPos[0], lastPos[1])

    # Find the number of adjacent available cells of a cell
    def getNeighbourCount(self, pos):
        row, col = pos
        return len(list(filter(
            lambda pos: (0 <= pos[0] < self.size) and (0 <= pos[1] < self.size) and (self.grid[pos[0]][pos[1]] == -1),
        [
            [row-2, col+1], [row-1, col+2],
            [row+1, col+2], [row+2, col+1],
            [row+2, col-1], [row+1, col-2],
            [row-1, col-2], [row-2, col-1]
        ]
        )))
