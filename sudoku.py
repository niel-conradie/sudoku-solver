def find_next_empty(puzzle):
    """ Verify next empty space. """
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == 0:
                return r, c
    return None, None


def validate(puzzle, guess, row, column):
    """ Verify a valid guess. """
    # Verifying the row.
    row_values = puzzle[row]
    if guess in row_values:
        return False

    # Verifying the column.
    column_values = [puzzle[i][column] for i in range(9)]
    if guess in column_values:
        return False

    # Verifying the the square.
    row_start = (row // 3) * 3
    column_start = (column // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(column_start, column_start + 3):
            if puzzle[r][c] == guess:
                return False
    return True


def sudoku_solver(puzzle):
    """ Solve the sudoku puzzle. """
    row, column = find_next_empty(puzzle)

    # Return True when solved.
    if row is None:
        return True

    for guess in range(1, 10):
        # Verify a valid guess.
        if validate(puzzle, guess, row, column):
            puzzle[row][column] = guess
            # Recursively call solver.
            if sudoku_solver(puzzle):
                return True
        # Backtrack and try new number.
        puzzle[row][column] = 0
    return False


if __name__ == '__main__':
    sudoku = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],

        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],

        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    print(sudoku_solver(sudoku))
    print(sudoku)
