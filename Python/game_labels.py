
class Label:
    def __init__(self, value, side, board_size, row=None, column=None):
        """Label for the side of the game. Use a value of 0 for a placeholder."""
        if value in range(10):
            self.value = value
        else:
            raise ValueError("Values for a label must be between 0 and 10")
        if side in ["left", "right", "top", "bottom"]:
            self.side = side
        else:
            raise ValueError("Side must be 'left', 'right', 'top', or 'bottom'.")
        self.board_size = board_size
        if row == None and column == None:
            raise ValueError("You must set either row or column when creating a Label.")
        self.row = row
        self.column = column

    def display(self, console_row_number):
        """Returns the ascii for a label given which row. Note: labels should be limited to sizes 0-9."""
        # calculate the index of the middle character based on board_size
        middle = (self.board_size+1)//2-1
        # if the value of the label is 0, just fill in spaces
        if self.value == 0:
            return f"{' '*self.board_size}"
        # label on the left left side
        elif self.side == "left":
            # only the middle row has characters other than spaces
            if console_row_number == middle:
                return f"{' '*(self.board_size-3)}{self.value}->"
            else:
                return f"{' '*self.board_size}"
        # label on the right side
        elif self.side == "right":
            # only the middle row has characters other than spaces
            if console_row_number == middle:
                return f"<-{self.value}{' '*(self.board_size-3)}"
            else:
                return f"{' '*self.board_size}"
        elif self.side == "top":
            # calculate the number of spaces to the left
            number_of_spaces_to_left = middle
            # the number of spaces to the right is all the rest of the characters but 1
            number_of_spaces_to_right = self.board_size-number_of_spaces_to_left-1
            # draw the arrow with the value on top of it
            if console_row_number == self.board_size-1:
                return f"{' '*number_of_spaces_to_left}⌄{' '*number_of_spaces_to_right}"
            elif console_row_number == self.board_size-2:
                return f"{' '*number_of_spaces_to_left}|{' '*number_of_spaces_to_right}"
            elif console_row_number == self.board_size-3:
                return f"{' '*number_of_spaces_to_left}{self.value}{' '*number_of_spaces_to_right}"
            # fill out spaces for all other rows
            else:
                return f"{' '*self.board_size}"
        elif self.side == "bottom":
            number_of_spaces_to_left = middle
            number_of_spaces_to_right = self.board_size-number_of_spaces_to_left-1
            #  draw the arrow with the value below it
            if console_row_number == 0:
                return f"{' '*number_of_spaces_to_left}^{' '*number_of_spaces_to_right}"
            elif console_row_number == 1:
                return f"{' '*number_of_spaces_to_left}|{' '*number_of_spaces_to_right}"
            elif console_row_number == 2:
                return f"{' '*number_of_spaces_to_left}{self.value}{' '*number_of_spaces_to_right}"
            # fill out spaces for all other rows
            else:
                return f"{' '*self.board_size}"
