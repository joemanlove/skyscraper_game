from utilities import list_equality_check, validate_integer_input
from game_pieces import Piece
from game_labels import Label

class GameBoard:
    def __init__(self, size):
        """
        A game board initially filled with pieces of size 0 and labels of size 0. The pieces and labels are never removed, their sizes and values are only updated.
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
        # adding all Pieces by reference allows for keeping them in multiple structures without having to set them multiple times
        for i in range(self.size):
            column = []
            for j in range(self.size):
                column.append(self.rows[j][i])
            self.columns.append(column)

        # rows with the labels included used for display
        # all Pieces are included by reference, so the display is the same as the data in the rows and columns
        self.rows_with_labels = [[Label(0, "top", self.size, column=j) for j in range(self.size+2)]]
        for i in range(self.size):
            row_with_labels = [Label(0, "left", self.size, row=i)]
            row_with_labels += self.rows[i]
            row_with_labels += [Label(0, "right", self.size, row=i)]
            self.rows_with_labels.append(row_with_labels)
        self.rows_with_labels.append([Label(0, "bottom", self.size, column=j) for j in range(self.size+2)])

        # put all the labels in a list of their own by reference
        self.labels = []
        for row in self.rows_with_labels:
            for item in row:
                if isinstance(item, Label):
                    self.labels.append(item)


    def place_piece(self, row_number, column_number, piece_size):
        """
        Places a new piece on the board. (Actually updates the size of an existing piece.)
        """
        # updating size rather than replacing the piece because the columns and rows_with_labels all reference the piece objects
        piece_to_adjust = self.rows[row_number][column_number]
        piece_to_adjust.size = piece_size

    def place_label(self, value, side, row=None, column=None):
        """
        Places a new label on the board. (Actually updates the value of an existing label.)
        """
        # updating value rather than replacing the label because labels and rows_with_labels all reference the label objects
        for label in self.labels:
            if label.side == side and label.row == row and label.column == column:
                label.value = value


    def construct_game_board_ascii_without_labels(self):
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

        display_string = horizontal_rule.join(rows)
        return display_string.split('\n')
    
    def construct_game_board_ascii_with_labels(self):
        """
        Returns a list of strings that compose the ascii representation of the gameboard including labels.
        """
        # list storage of rows so we can join with horizontal lines
        rows =[]
        # for each row of the game board
        for row_number in range(self.size+2):
            # string storage for every console row
            row_string = ''
            # for every console row (a game board row is made of multiple console rows)
            for console_row in range(self.size):
                # list storage of sub_rows so we can join with pipes for the vertical lines
                console_row_strings = []
                # for each column
                for column_number in range(self.size+2):
                    console_row_strings.append(self.rows_with_labels[row_number][column_number].display(console_row))
                # separate each column with vertical lines
                row_string += '|'.join(console_row_strings) + '\n'
            # add the completed console rows (which is a game board row) to the rows list
            rows.append(row_string)
        
        # Put horizontal lines between the game board rows
        separators = [f"{'-'*self.size}" for _ in range(self.size+2)]
        horizontal_rule = '+'.join(separators) + '\n'
        
        display_string = horizontal_rule.join(rows)
        return display_string.split('\n')

    def display(self):
        for line in self.construct_game_board_ascii_with_labels():
            print(line)

    # def number_display(self):
    #     """
    #     Number only display for console.
    #     """
    #     # TODO update this for boards larger than 3x3
    #     print(f"{self.rows[0][0].number_display()}|{self.rows[0][1].number_display()}|{self.rows[0][2].number_display()}")
    #     print("-+-+-")
    #     print(f"{self.rows[1][0].number_display()}|{self.rows[1][1].number_display()}|{self.rows[1][2].number_display()}")
    #     print("-+-+-")
    #     print(f"{self.rows[2][0].number_display()}|{self.rows[2][1].number_display()}|{self.rows[2][2].number_display()}")
    
    def valid_board(self):
        """
        Returns either true or false for if the board is valid.
        """
        valid = [i+1 for i in range(self.size)]
        
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
