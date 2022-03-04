"""
Author: Luke Laurie
Date: 2/19/2022
DESCRIPTION: This will guide the player through game getting their inputs
    as they play. And this file will continue updating the board and checking
    if a player has won.
"""
import connect_n_state

def main():
    # Gets all of the starting inputs from the player
    players = []
    player_one = input("Choose the name for player 1: ")
    player_two = input("Choose the name for player 2: ")
    players.append(player_one)
    players.append(player_two)
    while True:
        target_length = input("Choose the target length to win: ")
        width = input("Enter the game board width: ")
        height = input("Enter the game board height: ")
        if not (target_length.isdigit() and width.isdigit() and height.isdigit()):
            print("Please enter an integer")
        else:
            break
    target_length, width, height = int(target_length), int(width), int(height)
    # Creates the game board with the given information
    game = connect_n_state.Connect_N_State(width, height, target_length, players)
    game.print()
    print()
    while True:
        # Runs the game until a player wins or until the board is filled
        current_player = game.get_cur_player()
        move_location = input(f"'{current_player}' to move\n")
        if not move_location.isdigit():
            print("Please input a number")
        else:
            move_location = int(move_location) - 1
            if move_location >= width or move_location < 0 or game.is_column_full(move_location):
                print("Choose a valid collumn")
                game.print()
            else:
                game.move(move_location)
                game.print()
                if game.is_board_full():
                    print("It's a tie!")
                    break
                elif game.is_game_over():
                    print(f'{current_player} is the winner!')
                    break
            print()

if __name__ == "__main__":
    main()