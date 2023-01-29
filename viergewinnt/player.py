from viergewinnt.board import Board

class Player:
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
            column = int(input('Please enter a column for your next move: '))
            if column in range(1, board.columns + 1):
                #print('OK!')
                break
            else:
                print('Please try again')
        return column - 1

if __name__ == '__main__':
    board = Board(6, 7)
    print(board)
    p = Player("X")
    print(p)
    print(p.opponent())
    #p.move(board)

    while True:
        board.place_piece(p.move(board), p.piece)
        print(board)
        if board.win(p.piece):
            break