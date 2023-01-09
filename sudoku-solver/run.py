from sudoku import SudokuSolver


if __name__ == "__main__":
    run = SudokuSolver()

    try:
        # Starting the application.
        run.start_app()
    except KeyboardInterrupt:
        # Stopping the application.
        quit("\n\nProgram Terminated")
