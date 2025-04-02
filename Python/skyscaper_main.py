import subprocess
import os
import collections

def clear():
    subprocess.Popen('cls' if os.name=='nt' else 'clear', shell=True).wait()


class Piece:
    def __init__(self, size):
        """Piece for the game."""
        self.size = size

    def display(self, console_row_number):
        """Display the pieces."""

        # TODO make this work for arbitrary numbers instead of 1,2,3
        # asciis = [
        #     ['X  ', '   ', '   '],
        #     ['XX ', 'XX ', '   '],
        #     ['XXX', 'XXX', 'XXX']
        # ]

        # if self.size in [1, 2, 3]:
        #     return asciis[self.size - 1][console_row_number]
        # else:
        #     return '   '
    
        asciis = [
            ['X   ', '    ', '    ', '    '],
            ['XX  ', 'XX  ', '    ', '    '],
            ['XXX ', 'XXX ', 'XXX ', '    ']
        ]
        if self.size in [1, 2, 3]:
            return asciis[self.size - 1][console_row_number]
        else:
            return '    '
    

        
    def number_display(self):
        """Display only the numbers of the piece, good for diagnostics."""
        return str(self.size)

    
    def __repr__(self):
        return f"Piece of size: {self.size}"


# class Label:



class GameBoard:
    def __init__(self, size = 3):
        """
        A game board initially filled with pieces of size 0.
        """
        self.size = size

        # storage for rows, accessed by row number, column number
        self.rows = []
        for _ in range(self.size):
            row = [Piece(0) for __ in range(self.size)]
            self.rows.append(row)
        
        # seems redundant, but keeping track of columns makes checking board validity much easier 
        # storage for columns, accessed by column number, row number
        self.columns = []
        for _ in range(self.size):
            col = [Piece(0) for __ in range(self.size)]
            self.columns.append(col)

    def place_piece(self, row_number, column_number, piece_size):
        """
        Places a new piece on the board.
        """
        # Updating both rows and columns to keep them consistent
        self.rows[row_number][column_number] = Piece(piece_size)
        self.columns[column_number][row_number] = Piece(piece_size)

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
        print(f"{self.rows[0][0].number_display()}|{self.rows[0][1].number_display()}|{self.rows[0][2].number_display()}")
        print("-+-+-")
        print(f"{self.rows[1][0].number_display()}|{self.rows[1][1].number_display()}|{self.rows[1][2].number_display()}")
        print("-+-+-")
        print(f"{self.rows[2][0].number_display()}|{self.rows[2][1].number_display()}|{self.rows[2][2].number_display()}")
    
    def valid_board(self):
        """
        Returns either true or false for if the board is valid.
        """
        valid = [1, 2, 3]
        
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


def validate_integer_input(prompt, min=0, max=3):
    """
    Ensure that the user has entered a valid integer between the min and max.
    Invalid input results in a reprompt.
    """
    while True:
        user_input = input(prompt)
        try:
            # is user input an integer?
            user_input_int = int(user_input)
            # is it in the proper range?
            if user_input_int < min or user_input_int > max:
                raise ValueError
            return user_input_int
        except ValueError:
            print("Invalid input, please try again.")




def list_equality_check(list_1, list_2):
    """Check if two lists are equal."""
    return collections.Counter(list_1) == collections.Counter(list_2)


if __name__ == "__main__":

    invalid_test_board = GameBoard(size = 4)
    invalid_test_board.place_piece(0, 0, 3)
    invalid_test_board.place_piece(0, 1, 2)
    invalid_test_board.place_piece(0, 2, 1)
    invalid_test_board.place_piece(1, 0, 3)
    invalid_test_board.place_piece(1, 1, 2)
    invalid_test_board.place_piece(1, 2, 1)
    invalid_test_board.place_piece(2, 0, 3)
    invalid_test_board.place_piece(2, 1, 2)
    invalid_test_board.place_piece(2, 2, 1)

    # invalid_test_board.display()

    # print(invalid_test_board.valid_board())


    while True:
        clear()
        invalid_test_board.display()
        print(invalid_test_board.valid_board())
        invalid_test_board.collect_user_move()


