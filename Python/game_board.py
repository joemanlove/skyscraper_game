from utilities import list_equality_check, validate_integer_input
from game_pieces import Piece

class GameBoard:
    def __init__(self, size = 3):
        """
        A game board initially filled with pieces of size 0.
        """
        self.size = size

        # storage for rows, accessed by row number, column number
        self.rows = []
        for _ in range(self.size):
            row = [Piece(0, self.size) for __ in range(self.size)]
            self.rows.append(row)
        
        # seems redundant, but keeping track of columns makes checking board validity much easier 
        # storage for columns, accessed by column number, row number
        self.columns = []
        for _ in range(self.size):
            col = [Piece(0, self.size) for __ in range(self.size)]
            self.columns.append(col)

    def place_piece(self, row_number, column_number, piece_size):
        """
        Places a new piece on the board.
        """
        # Updating both rows and columns to keep them consistent
        self.rows[row_number][column_number] = Piece(piece_size, self.size)
        self.columns[column_number][row_number] = Piece(piece_size, self.size)

    def construct_game_board_ascii(self):
        """
        Returns a list of strings that compose the ascii representation of the gameboard.
        """
        # list storage of rows so we can join with horizontal lines
        rows =[]
        # for each row of the game board
        for row_number in range(self.size):
            # string storage for every console row
            row_string = ''
            # for every console row (a game board row is made of multiple console rows)
            for console_row in range(self.size):
                # list storage of sub_rows so we can join with pipes for the vertical lines
                console_row_strings = []
                # for each column
                for column_number in range(self.size):
                    console_row_strings.append(self.rows[row_number][column_number].display(console_row))
                # separate each column with vertical lines
                row_string += '|'.join(console_row_strings) + '\n'
            # add the completed console rows (which is a game board row) to the rows list
            rows.append(row_string)
        
        # Put horizontal lines between the game board rows
        separators = [f"{'-'*self.size}" for _ in range(self.size)]
        horizontal_rule = '+'.join(separators) + '\n'

        # display_string = f"{'-'*self.size}+{'-'*self.size}+{'-'*self.size}\n".join(rows)
        display_string = horizontal_rule.join(rows)
        return display_string.split('\n')

    def display(self):
        # print(self.construct_game_board_ascii())
        for line in self.construct_game_board_ascii():
            print(line)

    def number_display(self):
        """
        Number only display for console.
        """
        # TODO update this for boards larger than 3x3
        print(f"{self.rows[0][0].number_display()}|{self.rows[0][1].number_display()}|{self.rows[0][2].number_display()}")
        print("-+-+-")
        print(f"{self.rows[1][0].number_display()}|{self.rows[1][1].number_display()}|{self.rows[1][2].number_display()}")
        print("-+-+-")
        print(f"{self.rows[2][0].number_display()}|{self.rows[2][1].number_display()}|{self.rows[2][2].number_display()}")
    
    def valid_board(self):
        """
        Returns either true or false for if the board is valid.
        """
        valid = [i for i in range(self.size)]
        
        # check that each row is valid
        for row in self.rows:
            values =[]
            for piece in row:
                values.append(piece.size)
            if not list_equality_check(values, valid):
                return False
        
        # check that each column is valid
        for column in self.columns:
            values =[]
            for piece in column:
                values.append(piece.size)
            if not list_equality_check(values, valid):
                return False

        return True
    
    def collect_user_move(self):
        """Collect the user's move."""
        row_index = validate_integer_input("Which row would you like to place in?\n", max=self.size) - 1
        column_index = validate_integer_input("Which column would you like to place in?\n", max=self.size) - 1
        piece_size = validate_integer_input("What size piece would you like to place?\n", max=self.size)
        self.place_piece(row_index, column_index, piece_size)
