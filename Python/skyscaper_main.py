from game_board import GameBoard
from levels import level_1

current_level = level_1
level_count = 0

if __name__ == "__main__":
    
    while True:
        current_level.play()
        answer = input("Proceed to next level?\n")
        if answer.lower() in ["y", "yes", "yeah", "yup"] and current_level.next_level:
            current_level = current_level.next_level
            level_count += 1
            answer = ""
        else:
            print(f"Thanks for playing! You successfully solved {level_count} levels.")
            break



