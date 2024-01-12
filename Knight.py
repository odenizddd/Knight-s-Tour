class Knight:
    def __init__(self, row, col):
        # Vertical position of the knight
        self.row = row
        # Horizontal position of the knight
        self.col = col

    # Move the knight to a new position
    def move(self, row, col):
        self.row = row
        self.col = col