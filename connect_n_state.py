"""
Author: Luke Laurie
Date: 2/19/2022
DESCRIPTION: This will recreate the popular game connect 4 but with
    some small changes. The players will be given the opportunity to
    play on custom board width/height, a custom target number along
    with a custom number of players.
"""
class Connect_N_State:
    '''
    This class recreates the Connect N game. It gives players the freedom
        to place their pieces where they choose while keeping track of
        the game board at all times. It also has the ability to print
        out its board and determine if a player has won or not.
    The constructor will takes in three parameters and it will set each
        them to be private variables. The width and height are integers
        representing the game board dimensions. The target is an integer
        representing the amount of pieces that need to be placed in order
        to win, and the players will be a list containing strings that
        represent all the player names.
    Methods:
        get_size(): Gets the width and height of the board.
        get_target(): Gets the number for the target.
        get_player_list(): Gets the list containing each player.
        is_game_over(): Checks if the game has ended.
        get_winner(): Gets which player was the winner.
        is_board_full(): Checks if the board is full.
        is_column_full(): Checks if a column is full to determine
            if more tokens can be added.
        get_cell(): Checks if a token is in a certain cell or not.
        get_cur_player(): Gets the player that will be moving next.
        move(): Determines if the player was able to place the token.
        print(): Prints out the current game board.
        get_direction(): Creates a dictionary containing the amount
            of times the piece appeared in each direction.
    '''
    def __init__(self, width, height, target, players):
        # Creates the variables as private variables
        self._width = width
        self._height = height
        self._target = target
        self._players = players
        self._player_index = 0
        # Creates the initial game board
        self._game_board = []
        for i in range(self._height):
            board_row = []
            # Adds each blank spot in as a .
            for j in range(self._width):
                board_row.append(".")
            self._game_board.append(board_row)

    def get_size(self):
        '''
        Gets the current width and height of the board
        Return Type:
            Returns a tuple containing two integers that represent
            the width and the height.
        '''
        # Stores the width/height in a tuple
        size = (self._width, self._height)
        return size

    def get_target(self):
        '''
        Gets the target length given by the user
        Return Type:
            Returns an integer representing the target length
        '''
        return self._target

    def get_player_list(self):
        '''
        Gets the names for each of the players.
        Return Type:
            Returns a list containing strings that represent the
            player names.
        '''
        return self._players

    def is_game_over(self):
        '''
        This will determine if the game is ended or not. It will check
            if either a player has won the game, or if the board has
            filled up. If either of those are true, it will determine
            that the game has ended.
        Return Type:
            Returns a Boolean representing weather the game is over or not.
        '''
        if self.is_board_full():
            return True
        # Iterates through each item starting at the bottom of the game board
        for j_value in range(len(self._game_board)-1,-1,-1):
            for index in range(len(self._game_board[j_value])):
                direction_dict = self.get_directions(index, j_value)
                # Checks if any of the counters is equal to the target
                for direction in direction_dict:
                    if direction_dict[direction] == self._target:
                        return True
        return False

    def get_directions(self, i, j):
        '''
        Creates a dictionary containing the five possible directions that
            the pieces can be traveling in. This function will add one to
            the value of the direction every time the piece is located in
            that direction.
        Parameters:
            i: An integer representing the index of the column.
            j: An integer representing the index of the row.
        Return Type:
            Returns a dictionary where the keys are strings representing
            the direction and the values are integers representing how many
            times the piece appeared in that direction.
        '''
        game_piece = self._game_board[j][i]
        # Sets the amount of times the piece appeared in each direction
        values = {"west": 0, "east": 0, "north": 0, "nw": 0, "ne": 0}
        if game_piece != ".":
            left_value, right_value, up_value = i, i, j
            for j in range(self._target):
                # Checks each direction and if the piece appears again
                # Adds one to the counter of that direction if so
                if left_value >= 0 and self._game_board[-1][left_value]\
                        == game_piece:
                    values["west"] += 1
                if right_value < len(self._game_board[-1]) and \
                        self._game_board[-1][right_value] == game_piece:
                    values["east"] += 1
                if up_value >= 0 and self._game_board[up_value][i]\
                        == game_piece:
                    values["north"] += 1
                if right_value < len(self._game_board[-1]) and up_value >= 0 \
                    and self._game_board[up_value][right_value] == game_piece:
                    values["ne"] += 1
                if left_value >= 0 and up_value >= 0 and \
                    self._game_board[up_value][left_value] == game_piece:
                    values["nw"] += 1
                # Changes the direction variables
                left_value -= 1
                right_value += 1
                up_value -= 1
        return values

    def get_winner(self):
        '''
        Determines which player is the winner of the game. It will also
            determine if the game has ended in a tie or not.
        Return Type:
            Returns None if the game was a tie and otherwise a string
            representing the name of the player that has won.
        '''
        if self.is_board_full():
            return None
        else:
            self._player_index -= 1
            winner = self.get_cur_player()
            return winner

    def is_board_full(self):
        '''
        Checks to see if there are any spaces left open for the players
            to be able to continue on playing.
        Return Type:
            Returns a Boolean representing if the board is full or not.
        '''
        # Iterates through each item on board and checks if any are a .
        for row in self._game_board:
            for item in row:
                if item == ".":
                    return False
        return True

    def is_column_full(self, col):
        '''
        Checks a single given column to see if it is full of pieces or not
            so that it can be determined if playing a piece in that column
            is a valid move or not.
        Parameters:
            col: An integer that is used to determine which column needs to
                be checked for.
        Return Type:
            Returns a Boolean representing if the column is full or not.
        '''
        # Checks the top element in the column to see if the column us full
        if self._game_board[0][col] != ".":
            return True
        # Returns False if the column is not full
        else:
            return False

    def get_cell(self, x, y):
        '''
        Checks a cell at a certain location that is given by the user, and
            it determines weather the cell contains a player piece or an
            empty piece.
        Parameters:
            x: An integer representing the x location for the cell.
            y: An integer representing the y location for the cell.
        Return Type:
            Returns either the player piece that was found in that cell
            or None if the cell was empty.
        '''
        # Sets the y position to be starting at the bottom of the board
        y = len(self._game_board) - y - 1
        cell_piece = self._game_board[y][x]
        # Checks if the cell piece is a player piece or not
        if cell_piece == ".":
            return None
        for player in self._players:
            if player[0]  == cell_piece:
                return player

    def get_cur_player(self):
        '''
        This will move through the list of players to determine
            which player will be moving next.
        Return Type:
            Returns a string representing the name of the player that
            is going to move next.
        '''
        # Changes to the first player if the end of the player list is reached
        if self._player_index == len(self._players):
            self._player_index = 0
        return self._players[self._player_index]

    def move(self, col):
        '''
        This will move the player piece int it's correct location on
            the board assuming the location given by the player is valid.
        Return Type:
            Returns a Boolean representing if the move was carried
            out or not.
        '''
        # Checks if the move is valid or not
        is_valid = self.is_column_full(col)
        if is_valid:
            return False
        # Iterates through each row from the bottom upwards
        for i in range(len(self._game_board)-1,-1,-1):
            if self._game_board[i][col] == ".":
                # Changes the . spot to the players icon
                player_piece = self.get_cur_player()[0]
                self._game_board[i][col] = player_piece
                # moves the player
                self._player_index += 1
                return True

    def print(self):
        '''
        This will iterate through each piece of the board and it will
            print out each of those pieces in their correct respective
            locations.
        '''
        # Prints each of the cells on the game board
        for row in self._game_board:
            for cell in row:
                print(cell, end="")
            print()