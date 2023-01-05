from sudoku import SudokuSolver


def run():
    """Sudoku Solver."""
    run = SudokuSolver()

    try:
        # Starting the application.
        run.start_app()
    except KeyboardInterrupt:
        # Stopping the application.
        quit("\n\nProgram Terminated")


if __name__ == "__main__":
    run()
