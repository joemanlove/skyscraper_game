
# used for clear
import subprocess
import os
# used for list_equality_check
import collections 




def clear():

    subprocess.Popen('cls' if os.name=='nt' else 'clear', shell=True).wait()



def validate_integer_input(prompt, min=0, max=3):
    """
    Ensure that the user has entered a valid integer between the min and max.
    Invalid input results in a re-prompt.
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