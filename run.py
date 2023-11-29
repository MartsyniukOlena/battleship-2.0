# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import os
import random

def clear_screen():
    """
    Clears the terminal screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()

def play_game():
    """
    Plays the battleship game.
    """

    # Creating game boards for the player and computer
    player_board = [["O", "O", "O", "O", "O"],
                    ["O", "O", "O", "O", "O"],
                    ["O", "O", "O", "O", "O"],
                    ["O", "O", "O", "O", "O"],
                    ["O", "O", "O", "O", "O"]]

    computer_board = [["O", "O", "O", "O", "O"],
                      ["O", "O", "O", "O", "O"],
                      ["O", "O", "O", "O", "O"],
                      ["O", "O", "O", "O", "O"],
                      ["O", "O", "O", "O", "O"]]

play_game()