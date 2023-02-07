class Board:
    def __init__(self, rows: int, columns: int):
        self.rows = rows
        self.columns = columns
        self.slots = [[' ' for i in range(columns)] for j in range(rows)]

    def __repr__(self):
        board = ''
        for row in self.slots:
            board += '|' + '|'.join(row) + '|' + '\n'
        return board

    def place_piece(self, column: int, piece: str):
        row = 0
        for r in range(self.rows):
            if self.slots[r][column] == ' ':
                row = r
        self.slots[row][column] = piece

    def valid_column(self, column: int):
        return self.slots[0][column] == ' '

    def is_piece(self, row: int, column: int, piece: str):
        return self.slots[row][column] == piece

    def win(self, piece):
        for column in range(self.columns - 3):
            for row in range(self.rows):
                if self.slots[row][column] == self.slots[row][column+1] == self.slots[row][column+2] == self.slots[row][column+3] == piece:
                    print('horizontal win')
                    return True

        for column in range(self.columns):
            for row in range(self.rows - 3):
                if self.slots[row][column] == self.slots[row+1][column] == self.slots[row+2][column] == self.slots[row+3][column] == piece:
                    print('vertical win')
                    return True

        for column in range(self.columns - 3):
            for row in range(self.rows - 3):
                if self.slots[row][column] == self.slots[row+1][column+1] == self.slots[row+2][column+2] == self.slots[row+3][column+3] == piece:
                    print('diagonal win')
                    return True


if __name__ == '__main__':
    board = Board(6, 7)
    #print(board)

    board.place_piece(1, 'X')
    board.place_piece(1, 'X')
    board.place_piece(1, 'X')
    board.place_piece(1, 'X')
    board.place_piece(1, 'X')
    board.place_piece(3, 'X')
    #board.place_piece(1, 'X')
    print(board)
    #print(board.valid_column(1))
    print(board.is_piece(5, 3, 'X'))