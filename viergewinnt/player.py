from viergewinnt.board import Board
import random
import copy

class Player:
    @property
    def piece(self):
        return self.__piece

    @piece.setter
    def piece(self, value):
        if value == "X" or value == "O":
            self.__piece = value
        else:
            self.__piece = "X"
            print("OK! X it is!")


    def __init__(self, piece: str):
        """Assigns parameter to attribute.

        Parameters
        ----------
        piece : str
            string which represents the piece
        """
        self.piece = piece

    def __repr__(self):
        """Returns a representation of a Player object."""
        return f'Player {self.piece}'

    def opponent(self):
        """Returns a string containing the chosen piece.

        Returns
        -------
        string
            chosen piece
        """
        if self.piece == 'X':
            return 'O'
        else:
            return 'X'

    def move(self, board):
        """Returns an integer entered by the user, re-prompting on invalid input.

        Parameters
        ----------
        board : Board
            object which represents the board

        Returns
        -------
        int
            chosen column
        """
        while True:
            try:
                column = int(input('Please enter a column: '))
                if 1 <= column <= board.columns and board.valid_column(column-1):
                    return column - 1
                else:
                    print('Please enter a valid number')
            except ValueError:
                print('input a valid choice please')


class PCPlayer(Player):
    def __init__(self, piece: str):
        """Assigns parameter to attribute.

        Parameters
        ----------
        piece : str
            string which represents the piece
        """
        super().__init__(piece)

    def move(self, board):
        """Returns a random integer in range from 0 to 6.

        Parameters
        ----------
        board : Board
            object which represents the board

        Returns
        -------
        int
            chosen column
        """
        column = random.randint(0, board.columns-1)
        if board.valid_column(column):
            return column
        else:
            self.move(board)


class AI(Player):
    def __init__(self, piece: str):
        """Assigns parameter to attribute.

        Parameters
        ----------
        piece : str
            string which represents the piece
        """
        super().__init__(piece)


    def valid_move(self, board):
        """Returns a list of available columns.

        Parameters
        ----------
        board : Board
            object which represents the board

        Returns
        -------
        list of int
            valid moves
        """
        valid_move = []
        for column in range(board.columns):
            if board.valid_column(column):
                valid_move.append(column)
        return valid_move

    def move(self, board):
        """Returns an integer, which is calculated as best according to board score.

        Parameters
        ----------
        board : Board
            object which represents the board

        Returns
        -------
        int
            best column
        """
        best_score = 0
        valid_move = self.valid_move(board)
        best_column = random.choice(valid_move)
        for column in valid_move:
            #row = board.get_free_row(column)
            temp_board = copy.deepcopy(board)
            temp_board.place_piece(column, self.piece)
            score = temp_board.score(self.piece)
            if score > best_score:
                best_score = score
                best_column = column
        return best_column


if __name__ == '__main__':
    pass
