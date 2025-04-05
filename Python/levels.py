from game_board import GameBoard
from utilities import clear

class Level:
    def __init__(self, size, label_information):
        self.board = GameBoard(size)

        for value, side, number in label_information:
            # print(f"Value: {value}, Side: {side}, Number: {number}")
            if side in ["left", "right"]:
                self.board.place_label(value, side, row = number)
            if side in ["top", "bottom"]:
                self.board.place_label(value, side, column = number)
        self.next_level = None
        self.solved = False

    def set_next(self, next_level):
        self.next_level = next_level

    def play(self):
        while True:
            clear()
            self.board.display()
            print(self.board.valid_board())
            self.board.collect_user_move()
            if self.board.valid_board():
                self.solved = True
                break



level_1 = Level(3, [(3, "left", 1), (1, "left", 2), (1, "bottom", 2), (3, "bottom", 3)])
level_2 = Level(3, [(3, "left", 2), (1, "bottom", 1), (3, "bottom", 2)])
level_1.set_next(level_2)