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


def print_game_board(player_board, computer_board):
    """
    Prints the game board for both the player and the computer.
    """
    print("    Your Board            Computer's Board")
    print("    1 2 3 4 5             1 2 3 4 5")
    for i, (player_row, computer_row) in enumerate(zip(player_board, computer_board), start=1):
        print(f"{i} | {' '.join(player_row)}    |    {i} | {' '.join(computer_row)}")


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