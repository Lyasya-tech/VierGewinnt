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
        self.piece = piece

    def __repr__(self):
        return f'Player {self.piece}'

    def opponent(self):
        if self.piece == 'X':
            return 'O'
        else:
            return 'X'

    def move(self, board):
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
        super().__init__(piece)

    def move(self, board):
        column = random.randint(0, board.columns-1)
        if board.valid_column(column):
            return column
        else:
            self.move(board)


class AI(Player):
    def __init__(self, piece: str):
        super().__init__(piece)

    # def move(self, board):
    #     column = self.best_move(board)
    #     # if board.valid_column(column):
    #     return column
        # else:
        #     self.move(board)

    def valid_move(self, board):
        valid_move = []
        for column in range(board.columns):
            if board.valid_column(column):
                valid_move.append(column)
        return valid_move

    def move(self, board):
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
    board = Board(6, 7)
    print(board)
    p = Player(input('Choose X or O '))
    print(p)
    #p.move(board)

    while True:
        board.place_piece(p.move(board), p.piece)
        print(board)
        if board.win(p.piece):
            break