from sudoku import SudokuSolver


def run():
    """Sudoku Solver."""
    run = SudokuSolver()

    while True:
        # Starting empty sudoku.
        sudoku = run.empty_sudoku()

        while True:
            # Display sudoku board locations.
            run.display_sudoku(sudoku)
            # Requesting user input.
            user_input = run.user_input_location()
            # User input continue condition.
            if user_input == 'done':
                break
            # Assign user input to appropriate location.
            run.user_input_allocation(sudoku, user_input)

            continue

        # Solve sudoku.
        run.solver(sudoku)
        # Display solved sudoku.
        run.display_sudoku(sudoku)
        # Requesting user input.
        run.restart()

        continue


if __name__ == '__main__':
    run()
