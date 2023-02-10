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

    def print_board(self):
        print(self.slots)

    def get_free_row(self, column: int):
        row = 0
        for r in range(self.rows):
            if self.slots[r][column] == ' ':
                row = r
        return row

    def place_piece(self, column: int, piece: str):
        # row = 0
        # for r in range(self.rows):
        #     if self.slots[r][column] == ' ':
        #         row = r
        self.slots[self.get_free_row(column)][column] = piece

    def valid_column(self, column: int):
        return self.slots[0][column] == ' '

    def is_piece(self, row: int, column: int, piece: str):
        return self.slots[row][column] == piece

    def is_full(self):
        for row in range(self.rows):
            for column in range(self.columns):
                if self.slots[row][column] == " ":
                    return False
        return True

    def win(self, piece: str):
        for column in range(self.columns - 3):
            for row in range(self.rows):
                if self.slots[row][column] == self.slots[row][column+1] == self.slots[row][column+2] ==\
                        self.slots[row][column+3] == piece:
                    # print('horizontal win')
                    return True

        for column in range(self.columns):
            for row in range(self.rows - 3):
                if self.slots[row][column] == self.slots[row+1][column] == self.slots[row+2][column] ==\
                        self.slots[row+3][column] == piece:
                    # print('vertical win')
                    return True

        for column in range(self.columns - 3):
            for row in range(3, self.rows):
                if self.slots[row][column] == self.slots[row-1][column+1] == self.slots[row-2][column+2] ==\
                        self.slots[row-3][column+3] == piece:
                    # print('positive diagonal win')
                    return True

        for column in range(self.columns - 3):
            for row in range(self.rows - 3):
                if self.slots[row][column] == self.slots[row+1][column+1] == self.slots[row+2][column+2] ==\
                        self.slots[row+3][column+3] == piece:
                    # print('negative diagonal win')
                    return True

    def score(self, piece: str):
        score = 0

        # horizontal score
        for row in range(self.rows - 1, -1, -1):
            row_list = self.slots[row]

            for column in range(self.columns - 3):
                score_check = row_list[column:column+4]

                if score_check.count(piece) == 4:
                    score += 100
                elif score_check.count(piece) == 3 and score_check.count(' ') == 1:
                    score += 10
                elif score_check.count(piece) == 2 and score_check.count(' ') == 2:
                    score += 5
                elif score_check.count(piece) == 1 and score_check.count(' ') == 3:
                    score += 2

        # vertical score
        for column in range(self.columns):
            column_list = [row[column] for row in self.slots]

            for r in range(self.rows - 3):
                score_check = column_list[r:r+4]

                if score_check.count(piece) == 4:
                    score += 100
                elif score_check.count(piece) == 3 and score_check.count(' ') == 1:
                    score += 10
                elif score_check.count(piece) == 2 and score_check.count(' ') == 2:
                    score += 5
                elif score_check.count(piece) == 1 and score_check.count(' ') == 3:
                    score += 2

        # positive diagonal score
        for column in range(self.columns - 3):
            for row in range(3, self.rows):

                score_check = [self.slots[row - i][column + i] for i in range(4)]
                # print(score_check)
                if score_check.count(piece) == 4:
                    score += 100
                elif score_check.count(piece) == 3 and score_check.count(' ') == 1:
                    score += 10
                elif score_check.count(piece) == 2 and score_check.count(' ') == 2:
                    score += 5
                elif score_check.count(piece) == 1 and score_check.count(' ') == 3:
                    score += 2

        # negative diagonal score
        for column in range(self.columns - 3):
            for row in range(self.rows - 3):

                score_check = [self.slots[row + i][column + i] for i in range(4)]
                # print(score_check)
                if score_check.count(piece) == 4:
                    score += 100
                elif score_check.count(piece) == 3 and score_check.count(' ') == 1:
                    score += 10
                elif score_check.count(piece) == 2 and score_check.count(' ') == 2:
                    score += 5
                elif score_check.count(piece) == 1 and score_check.count(' ') == 3:
                    score += 2

        return score


if __name__ == '__main__':
    board = Board(6, 7)
    # print(board)
    # board.print_board()
    board.place_piece(0, "X")
    # board.place_piece(0, "X")
    # board.place_piece(0, "X")
    # board.place_piece(0, "X")
    # board.place_piece(0, "X")
    # board.place_piece(0, "X")

    # board.place_piece(1, "X")
    # board.place_piece(1, "X")
    # board.place_piece(1, "X")
    # board.place_piece(1, "X")
    # board.place_piece(1, "X")
    # board.place_piece(1, "X")

    # board.place_piece(2, "X")
    # board.place_piece(2, "X")
    # board.place_piece(2, "X")
    # board.place_piece(2, "X")
    # board.place_piece(2, "X")
    # board.place_piece(2, "X")

    # board.place_piece(3, "X")
    # board.place_piece(3, "X")
    # board.place_piece(3, "X")
    # board.place_piece(3, "X")
    # board.place_piece(3, "X")
    # board.place_piece(3, "X")

    # board.place_piece(4, "X")
    # board.place_piece(4, "X")
    # board.place_piece(4, "X")
    # board.place_piece(4, "X")
    # board.place_piece(4, "X")
    # board.place_piece(4, "X")

    # board.place_piece(5, "X")
    # board.place_piece(5, "X")
    # board.place_piece(5, "X")
    # board.place_piece(5, "X")
    # board.place_piece(5, "X")
    # board.place_piece(5, "X")

    # board.place_piece(6, "X")
    # board.place_piece(6, "X")
    # board.place_piece(6, "X")
    # board.place_piece(6, "X")
    # board.place_piece(6, "X")
    # board.place_piece(6, "X")

    # print(board.win("X"))
    print(board)
    print(board.score("X"))
    # print(board.valid_column(1))

    # print(board.get_free_row(1))
    # print(board.is_full())
    # print(board.slots)
