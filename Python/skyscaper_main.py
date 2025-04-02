from game_board import GameBoard
from utilities import clear



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


