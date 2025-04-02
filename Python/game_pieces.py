
class Piece:
    def __init__(self, size, board_size):
        """Piece for the game."""
        self.size = size
        self.board_size = board_size

    def display(self, console_row_number):
        """returns the ascii for a the piece given which row ."""
        if console_row_number in range(self.size):
            return f"{'X'*self.size}{' '*(self.board_size-self.size)}"
        else:
            return f'{' '*self.board_size}'
    

        
    def number_display(self):
        """Display only the numbers of the piece, good for diagnostics."""
        return str(self.size)

    
    def __repr__(self):
        return f"Piece of size: {self.size}"
