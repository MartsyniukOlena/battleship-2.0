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


def print_game_board(player_board, computer_board):
    """
    Prints the game board for both the player and the computer.
    """
    print("    Your Board            Computer's Board")
    print("    1 2 3 4 5             1 2 3 4 5")
    for i, (player_row, computer_row) in enumerate(zip(player_board, computer_board), start=1):
        print(f"{i} | {' '.join(player_row)}    |    {i} | {' '.join(computer_row)}")


def create_random_ship(used_positions):
    """
    Creates a random ship position that is not used.
    It keeps track of ship positions already generated on the game board,
    and creates a random ship position that hasn't been used before.
    """
    while True:
        ship_position = (random.randint(0, 4), random.randint(0, 4))
        if ship_position not in used_positions:
            used_positions.add(ship_position)
            return ship_position


def computer_move(used_positions):
    """
    Generates a random move for the computer.
    """
    while True:
        move = (random.randint(0, 4), random.randint(0, 4))
        if move not in used_positions:
            used_positions.add(move)
            return move


def play_game():
    """
    Plays the battleship game.
    """
    clear_screen()
    print("Welcome to the BATTLESHIP GAME!")
    player_name = input("Enter your name: ")
    print(f"Greetings, {player_name}! Let's start the BATTLESHIP GAME!"
          "\nSink all of the ships before the oponent sinks them.\n")
    print("Missed ships are marked with '-', hit ships are marked with'X'")
    input("Press Enter to start the game...")

    # Placing player's ships randomly on the board
    ship1 = create_random_ship(used_ship_positions)
    ship2 = create_random_ship(used_ship_positions)
    ship3 = create_random_ship(used_ship_positions)

    # Placing computer's ships randomly on the board
    computer_ship1 = create_random_ship(used_computer_positions)
    computer_ship2 = create_random_ship(used_computer_positions)
    computer_ship3 = create_random_ship(used_computer_positions)


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