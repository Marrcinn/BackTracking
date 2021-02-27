class Board():
    def __init__(self, puzzle):
        self.puzzle = puzzle

    def __str__(self):
        # Returns a nicely formatted sudoku
        s= ""
        for row in self.puzzle:
            for val in row:
                s=s+ str(val)+" | "
            s = s + "\n" + "----------------------------------\n"

        return s
    def solve(self):
        # Finds next empty value in puzzle
        row, col = self.find_empty()

        # If no empty left
        if row is None:
            return True

        # Make a valid guess
        for guess in range(1, 10):
            if self.guess_valid(guess, row, col):
                self.puzzle[row][col] = guess

                # If sudoku will get solved
                if self.solve():
                    return True
            #If the guess won't allow to get valid board further, reset the cell
            self.puzzle[row][col] = -1
        #If no solution was found, returns False
        return False

    def find_empty(self):
        # Finds a next empty piece in the puzzle
        for i in range(9):
            for j in range(9):
                if self.puzzle[i][j] == -1:
                    return i, j
        #If there are no more pieces empty, returns None
        return None, None

    def guess_valid(self, guess, row, col):
        # Checks if in the same row
        if guess in self.puzzle[row]:
            return False

        # Checks if in the same column
        col_vals = []
        for i in range(len(self.puzzle)):
            col_vals.append(self.puzzle[i][col])
        if guess in col_vals:
            return False

        # Checks if in the same square
        row_start = row // 3 * 3
        col_start = col // 3 * 3
        for i in range(row_start, row_start + 3):
            for j in range(col_start, col_start + 3):
                if guess == self.puzzle[i][j]:
                    return False

        # If passed all, it is valid
        return True

example = Board([
    [3, 9, -1, -1, 5, -1, -1, -1, -1],
    [-1, -1, -1, 2, -1, -1, -1, -1, 5],
    [-1, -1, -1, 7, 1, 9, -1, 8, -1],

    [-1, 5, -1, -1, 6, 8, -1, -1, -1],
    [2, -1, 6, -1, -1, 3, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, 4],

    [5, -1, -1, -1, -1, -1, -1, -1, -1],
    [6, 7, -1, 1, -1, 5, -1, 4, -1],
    [1, -1, 9, -1, -1, -1, 2, -1, -1]
])
print(example)
example.solve()
print(example)
