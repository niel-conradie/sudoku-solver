class SudokuSolver:
    """A class to represent a Sudoku solver."""

    @staticmethod
    def user_input_location():
        """Requesting user input and validating choice."""
        while True:
            user_input = input("\nType 'done' to solve sudoku.\n" +
                               "\nEnter location: ").lower()
            choices = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9',
                       'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8', 'b9',
                       'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8', 'c9',
                       'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8', 'd9',
                       'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8', 'e9',
                       'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
                       'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8', 'g9',
                       'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8', 'h9',
                       'i1', 'i2', 'i3', 'i4', 'i5', 'i6', 'i7', 'i8', 'i9',
                       'done']
            if user_input not in choices:
                print(f"\n{user_input} is not an valid choice!")
                continue
            else:
                return user_input

    @staticmethod
    def user_input_number():
        """Requesting user input and validating choice."""
        while True:
            try:
                user_input = int(input("\nEnter number: "))
            except ValueError:
                print("\nThat is not a number.")
                continue

            choices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            if user_input not in choices:
                print(f"\n{user_input} is not an valid choice!")
                continue
            else:
                return user_input

    def user_input_allocation(self, puzzle, user_input_location):
        """Return sudoku with updated values."""
        sudoku = puzzle
        if user_input_location == "a1":
            sudoku[0][0] = self.user_input_number()
        if user_input_location == "a2":
            sudoku[0][1] = self.user_input_number()
        if user_input_location == "a3":
            sudoku[0][2] = self.user_input_number()
        if user_input_location == "a4":
            sudoku[0][3] = self.user_input_number()
        if user_input_location == "a5":
            sudoku[0][4] = self.user_input_number()
        if user_input_location == "a6":
            sudoku[0][5] = self.user_input_number()
        if user_input_location == "a7":
            sudoku[0][6] = self.user_input_number()
        if user_input_location == "a8":
            sudoku[0][7] = self.user_input_number()
        if user_input_location == "a9":
            sudoku[0][8] = self.user_input_number()
        if user_input_location == "b1":
            sudoku[1][0] = self.user_input_number()
        if user_input_location == "b2":
            sudoku[1][1] = self.user_input_number()
        if user_input_location == "b3":
            sudoku[1][2] = self.user_input_number()
        if user_input_location == "b4":
            sudoku[1][3] = self.user_input_number()
        if user_input_location == "b5":
            sudoku[1][4] = self.user_input_number()
        if user_input_location == "b6":
            sudoku[1][5] = self.user_input_number()
        if user_input_location == "b7":
            sudoku[1][6] = self.user_input_number()
        if user_input_location == "b8":
            sudoku[1][7] = self.user_input_number()
        if user_input_location == "b9":
            sudoku[1][8] = self.user_input_number()
        if user_input_location == "c1":
            sudoku[2][0] = self.user_input_number()
        if user_input_location == "c2":
            sudoku[2][1] = self.user_input_number()
        if user_input_location == "c3":
            sudoku[2][2] = self.user_input_number()
        if user_input_location == "c4":
            sudoku[2][3] = self.user_input_number()
        if user_input_location == "c5":
            sudoku[2][4] = self.user_input_number()
        if user_input_location == "c6":
            sudoku[2][5] = self.user_input_number()
        if user_input_location == "c7":
            sudoku[2][6] = self.user_input_number()
        if user_input_location == "c8":
            sudoku[2][7] = self.user_input_number()
        if user_input_location == "c9":
            sudoku[2][8] = self.user_input_number()
        if user_input_location == "d1":
            sudoku[3][0] = self.user_input_number()
        if user_input_location == "d2":
            sudoku[3][1] = self.user_input_number()
        if user_input_location == "d3":
            sudoku[3][2] = self.user_input_number()
        if user_input_location == "d4":
            sudoku[3][3] = self.user_input_number()
        if user_input_location == "d5":
            sudoku[3][4] = self.user_input_number()
        if user_input_location == "d6":
            sudoku[3][5] = self.user_input_number()
        if user_input_location == "d7":
            sudoku[3][6] = self.user_input_number()
        if user_input_location == "d8":
            sudoku[3][7] = self.user_input_number()
        if user_input_location == "d9":
            sudoku[3][8] = self.user_input_number()
        if user_input_location == "e1":
            sudoku[4][0] = self.user_input_number()
        if user_input_location == "e2":
            sudoku[4][1] = self.user_input_number()
        if user_input_location == "e3":
            sudoku[4][2] = self.user_input_number()
        if user_input_location == "e4":
            sudoku[4][3] = self.user_input_number()
        if user_input_location == "e5":
            sudoku[4][4] = self.user_input_number()
        if user_input_location == "e6":
            sudoku[4][5] = self.user_input_number()
        if user_input_location == "e7":
            sudoku[4][6] = self.user_input_number()
        if user_input_location == "e8":
            sudoku[4][7] = self.user_input_number()
        if user_input_location == "e9":
            sudoku[4][8] = self.user_input_number()
        if user_input_location == "f1":
            sudoku[5][0] = self.user_input_number()
        if user_input_location == "f2":
            sudoku[5][1] = self.user_input_number()
        if user_input_location == "f3":
            sudoku[5][2] = self.user_input_number()
        if user_input_location == "f4":
            sudoku[5][3] = self.user_input_number()
        if user_input_location == "f5":
            sudoku[5][4] = self.user_input_number()
        if user_input_location == "f6":
            sudoku[5][5] = self.user_input_number()
        if user_input_location == "f7":
            sudoku[5][6] = self.user_input_number()
        if user_input_location == "f8":
            sudoku[5][7] = self.user_input_number()
        if user_input_location == "f9":
            sudoku[5][8] = self.user_input_number()
        if user_input_location == "g1":
            sudoku[6][0] = self.user_input_number()
        if user_input_location == "g2":
            sudoku[6][1] = self.user_input_number()
        if user_input_location == "g3":
            sudoku[6][2] = self.user_input_number()
        if user_input_location == "g4":
            sudoku[6][3] = self.user_input_number()
        if user_input_location == "g5":
            sudoku[6][4] = self.user_input_number()
        if user_input_location == "g6":
            sudoku[6][5] = self.user_input_number()
        if user_input_location == "g7":
            sudoku[6][6] = self.user_input_number()
        if user_input_location == "g8":
            sudoku[6][7] = self.user_input_number()
        if user_input_location == "g9":
            sudoku[6][8] = self.user_input_number()
        if user_input_location == "h1":
            sudoku[7][0] = self.user_input_number()
        if user_input_location == "h2":
            sudoku[7][1] = self.user_input_number()
        if user_input_location == "h3":
            sudoku[7][2] = self.user_input_number()
        if user_input_location == "h4":
            sudoku[7][3] = self.user_input_number()
        if user_input_location == "h5":
            sudoku[7][4] = self.user_input_number()
        if user_input_location == "h6":
            sudoku[7][5] = self.user_input_number()
        if user_input_location == "h7":
            sudoku[7][6] = self.user_input_number()
        if user_input_location == "h8":
            sudoku[7][7] = self.user_input_number()
        if user_input_location == "h9":
            sudoku[7][8] = self.user_input_number()
        if user_input_location == "i1":
            sudoku[8][0] = self.user_input_number()
        if user_input_location == "i2":
            sudoku[8][1] = self.user_input_number()
        if user_input_location == "i3":
            sudoku[8][2] = self.user_input_number()
        if user_input_location == "i4":
            sudoku[8][3] = self.user_input_number()
        if user_input_location == "i5":
            sudoku[8][4] = self.user_input_number()
        if user_input_location == "i6":
            sudoku[8][5] = self.user_input_number()
        if user_input_location == "i7":
            sudoku[8][6] = self.user_input_number()
        if user_input_location == "i8":
            sudoku[8][7] = self.user_input_number()
        if user_input_location == "i9":
            sudoku[8][8] = self.user_input_number()
        return sudoku

    @staticmethod
    def empty_sudoku():
        """Starting empty sudoku board."""
        sudoku = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
        ]
        return sudoku

    @staticmethod
    def display_sudoku(puzzle):
        """Display sudoku board locations and values."""
        sudoku = puzzle
        print(f"\n| A1 {sudoku[0][0]} | A2 {sudoku[0][1]} | A3 {sudoku[0][2]} |   "
              f"| A4 {sudoku[0][3]} | A5 {sudoku[0][4]} | A6 {sudoku[0][5]} |   "
              f"| A7 {sudoku[0][6]} | A8 {sudoku[0][7]} | A9 {sudoku[0][8]} |"
              f"\n| B1 {sudoku[1][0]} | B2 {sudoku[1][1]} | B3 {sudoku[1][2]} |   "
              f"| B4 {sudoku[1][3]} | B5 {sudoku[1][4]} | B6 {sudoku[1][5]} |   "
              f"| B7 {sudoku[1][6]} | B8 {sudoku[1][7]} | B9 {sudoku[1][8]} |"
              f"\n| C1 {sudoku[2][0]} | C2 {sudoku[2][1]} | C3 {sudoku[2][2]} |   "
              f"| C4 {sudoku[2][3]} | C5 {sudoku[2][4]} | C6 {sudoku[2][5]} |   "
              f"| C7 {sudoku[2][6]} | C8 {sudoku[2][7]} | C9 {sudoku[2][8]} |\n"
              f"\n| D1 {sudoku[3][0]} | D2 {sudoku[3][1]} | D3 {sudoku[3][2]} |   "
              f"| D4 {sudoku[3][3]} | D5 {sudoku[3][4]} | D6 {sudoku[3][5]} |   "
              f"| D7 {sudoku[3][6]} | D8 {sudoku[3][7]} | D9 {sudoku[3][8]} |"
              f"\n| E1 {sudoku[4][0]} | E2 {sudoku[4][1]} | E3 {sudoku[4][2]} |   "
              f"| E4 {sudoku[4][3]} | E5 {sudoku[4][4]} | E6 {sudoku[4][5]} |   "
              f"| E7 {sudoku[4][6]} | E8 {sudoku[4][7]} | E9 {sudoku[4][8]} |"
              f"\n| F1 {sudoku[5][0]} | F2 {sudoku[5][1]} | F3 {sudoku[5][2]} |   "
              f"| F4 {sudoku[5][3]} | F5 {sudoku[5][4]} | F6 {sudoku[5][5]} |   "
              f"| F7 {sudoku[5][6]} | F8 {sudoku[5][7]} | F9 {sudoku[5][8]} |\n"
              f"\n| G1 {sudoku[6][0]} | G2 {sudoku[6][1]} | G3 {sudoku[6][2]} |   "
              f"| G4 {sudoku[6][3]} | G5 {sudoku[6][4]} | G6 {sudoku[6][5]} |   "
              f"| G7 {sudoku[6][6]} | G8 {sudoku[6][7]} | G9 {sudoku[6][8]} |"
              f"\n| H1 {sudoku[7][0]} | H2 {sudoku[7][1]} | H3 {sudoku[7][2]} |   "
              f"| H4 {sudoku[7][3]} | H5 {sudoku[7][4]} | H6 {sudoku[7][5]} |   "
              f"| H7 {sudoku[7][6]} | H8 {sudoku[7][7]} | H9 {sudoku[7][8]} |"
              f"\n| I1 {sudoku[8][0]} | I2 {sudoku[8][1]} | I3 {sudoku[8][2]} |   "
              f"| I4 {sudoku[8][3]} | I5 {sudoku[8][4]} | I6 {sudoku[8][5]} |   "
              f"| I7 {sudoku[8][6]} | I8 {sudoku[8][7]} | I9 {sudoku[8][8]} |"
              )

    @staticmethod
    def find_next_empty(puzzle):
        """Verify next empty space."""
        for r in range(9):
            for c in range(9):
                if puzzle[r][c] == 0:
                    return r, c
        return None, None

    @staticmethod
    def validate(puzzle, guess, row, column):
        """Verify a valid guess."""
        # Verifying the row.
        row_values = puzzle[row]
        if guess in row_values:
            return False

        # Verifying the column.
        column_values = [puzzle[i][column] for i in range(9)]
        if guess in column_values:
            return False

        # Verifying the square.
        row_start = (row // 3) * 3
        column_start = (column // 3) * 3

        for r in range(row_start, row_start + 3):
            for c in range(column_start, column_start + 3):
                if puzzle[r][c] == guess:
                    return False
        return True

    def solver(self, puzzle):
        """Solve the sudoku puzzle."""
        row, column = self.find_next_empty(puzzle)

        # Return True when solved.
        if row is None:
            return True

        for guess in range(1, 10):
            # Verify a valid guess.
            if self.validate(puzzle, guess, row, column):
                puzzle[row][column] = guess
                # Recursively call solver.
                if self.solver(puzzle):
                    return True
            # Backtrack and try new number.
            puzzle[row][column] = 0
        return False
    
    def start_app(self):
        """Starting sudoku solver application."""
        while True:
            # Starting empty sudoku.
            sudoku = self.empty_sudoku()

            while True:
                # Display sudoku board locations.
                self.display_sudoku(sudoku)
                # Requesting user input.
                user_input = self.user_input_location()
                # User input continue condition.
                if user_input == 'done':
                    break
                # Assign user input to appropriate location.
                self.user_input_allocation(sudoku, user_input)

                continue

            # Solve sudoku.
            self.solver(sudoku)
            # Display solved sudoku.
            self.display_sudoku(sudoku)
            # Requesting user input.
            self.restart()

            continue
    
    @staticmethod
    def restart():
        """Requesting user input and validating choice."""
        while True:
            print("\nTry Again?")
            print("\nYes: Type '1'")
            print("No: Type '2'")

            try:
                user_input = int(input("\nEnter: "))
            except ValueError:
                print("\nThat is not a number.")
                continue

            # User input validation conditions.
            choices = [1, 2]
            if user_input not in choices:
                print(f"\n{user_input} is not an valid choice!")
                continue
            elif user_input == 1:
                return
            elif user_input == 2:
                print("\nThank you!")
                quit()
