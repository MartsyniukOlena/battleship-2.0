# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import os
import random
from colorama import Fore, Back, Style, init

def clear_screen():
    """
    Clears the terminal screen.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def colorize_cell(cell):
    """Colorizes the cell based on its content."""
    colors = {
        '-': '\033[91m',  # Red for missed shots
        'X': '\033[92m',  # Green for hit ships

    }
    return f"{colors.get(cell, '')}{cell}\033[0m"

def print_game_board(player_board, computer_board):
    """Prints the game board for both the player and the computer with colors."""
    print("    Your Board            Computer's Board")
    print("    1 2 3 4 5             1 2 3 4 5")
    for i, (player_row, computer_row) in enumerate(zip(player_board, computer_board), start=1):
        print(f"{i} | {' '.join(colorize_cell(cell) for cell in player_row)}    |    {i} | {' '.join(colorize_cell(cell) for cell in computer_row)}")


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


def play_again():
    """Asks the user if they want to play again."""
    try_again = input("Do you want to play again? (Y)es or (N)o?:\n").lower()
    return try_again == "y"


def play_game():
    """
    Plays the battleship game.
    """
    clear_screen()
    print(Fore.CYAN + "Welcome to the BATTLESHIP GAME!" + Style.RESET_ALL)
    player_name = input("Enter your name:\n")
    print("--------------------------------------------------------------")
    print(f"Greetings, {Fore.CYAN}{player_name}{Style.RESET_ALL}! Let's start the BATTLESHIP GAME!"
          "\nSink all of the ships before the oponent sinks them.\n")
    print("Missed ships are marked with '-', hit ships are marked with'X'")
    input(Fore.YELLOW +"Press Enter to start the game...\n" + Style.RESET_ALL)

    # Initializing sets to store used positions for player and computer ships
    used_ship_positions = set()
    used_computer_positions = set()

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

    # Initializing ship counts for player and computer
    ships_left = 3
    computer_ships_left = 3


    while True:
        try:
            print_game_board(player_board, computer_board)
            row = int(input(Fore.YELLOW +"\nEnter a row 1 to 5:\n" + Style.RESET_ALL))
            column = int(input(Fore.YELLOW + "Enter a column 1 to 5:\n" + Style.RESET_ALL))
        except ValueError:
            print(Fore.CYAN + "Only enter numbers!\n" + Style.RESET_ALL)
            continue

        # Validating user input for row and column
        if row not in range(1, 6) or column not in range(1, 6):
            print(Fore.CYAN + "Invalid input. Please enter valid numbers.\nThe numbers must be between 1-5!\n" + Style.RESET_ALL)
            continue

        row -= 1  # Reducing number to the desired index.
        column -= 1  # Reducing number to the desired index.


        # Handling player's moves and checking for hits or misses
        if player_board[row][column] == "-" or player_board[row][column] == "X":
            print(Fore.CYAN + "You have already made a move in this position. Try again.\n" + Style.RESET_ALL)
            continue
        elif (row, column) == computer_ship1 or (row, column) == computer_ship2 or (row, column) == computer_ship3:
            print(Fore.GREEN + "\nBoom! You hit! A ship has exploded!" + Style.RESET_ALL)
            player_board[row][column] = "X"
            ships_left -= 1
            if ships_left == 0:
                print(f"Your ships left: {ships_left}")
                print(f"Computer's ships left: {computer_ships_left}\n")
                print(Fore.MAGENTA + "Congratulations, you won!\n" + Style.RESET_ALL)
                break
        else:
            print(Fore.RED + "\nYou missed!" + Style.RESET_ALL)
            player_board[row][column] = "-"

        print(f"Your ships left: {ships_left}")

        # Computer's move
        computer_row, computer_column = computer_move(used_computer_positions)
        if computer_board[computer_row][computer_column] == "-" or computer_board[computer_row][computer_column] == "X":
            continue
        elif (computer_row, computer_column) == ship1 or (computer_row, computer_column) == ship2 or (computer_row, computer_column) == ship3:
            print(Fore.GREEN + f"\nThe computer hit the ship at {computer_row+1}, {computer_column+1}!\n" + Style.RESET_ALL)
            print(f"Computer's ships left: {computer_ships_left}\n")
            computer_board[computer_row][computer_column] = "X"
            computer_ships_left -= 1
            if computer_ships_left == 0:
                print(f"Computer's ships left: {computer_ships_left}\n")
                print(Fore.MAGENTA + "The computer won!\n" + Style.RESET_ALL)
                break
        else:
            print(Fore.RED + f"\nThe computer missed at {computer_row+1}, {computer_column+1}!" + Style.RESET_ALL)
            print(f"Computer's ships left: {computer_ships_left}\n")
            computer_board[computer_row][computer_column] = "-"

    if computer_ships_left == 0 and ships_left == 0:
                print("It's a tie!")

    print_game_board(player_board, computer_board)

    print("Thank you for playing, {}.".format(player_name))

if __name__ == "__main__":
    # Initiating the game and prompting the user to play again if desired
    while True:
        play_game()
        if not play_again():
            break
