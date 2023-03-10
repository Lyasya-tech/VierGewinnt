import unittest
from unittest.mock import patch
import random

from viergewinnt.board import Board
from viergewinnt.player import Player
from viergewinnt.player import PCPlayer
from viergewinnt.player import AI

class TestCommon(unittest.TestCase):
    def setUp(self) -> None:
        self.board = Board(6, 7)
        self.player = Player('X')
        self.pcplayer = PCPlayer('X')
        self.aiplayer = AI('X')

    def test_init_board(self):
        self.assertEqual(6, self.board.rows)
        self.assertEqual(7, self.board.columns)

    def test_init_player(self):
        self.assertEqual('X', self.player.piece)

    def test_valid_column(self):
        for i in range(self.board.rows):
            self.board.slots[i][6] = 'X'
        self.assertEqual(True, self.board.valid_column(0))
        self.assertEqual(True, self.board.valid_column(1))
        self.assertEqual(True, self.board.valid_column(2))
        self.assertEqual(True, self.board.valid_column(3))
        self.assertEqual(True, self.board.valid_column(4))
        self.assertEqual(True, self.board.valid_column(5))
        self.assertEqual(False, self.board.valid_column(6))

    def test_get_free_row(self):
        # this method is only executed if valid_column() has the value True

        self.board.slots = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         [' ', ' ', ' ', 'X', ' ', ' ', ' '],
                         [' ', ' ', 'X', 'X', 'X', ' ', ' '],
                         [' ', 'X', 'X', 'X', 'X', 'X', ' '],
                         ['X', 'X', 'X', 'X', 'X', 'X', 'X']]
        self.assertEqual(4, self.board.get_free_row(0))
        self.assertEqual(3, self.board.get_free_row(1))
        self.assertEqual(2, self.board.get_free_row(2))
        self.assertEqual(1, self.board.get_free_row(3))
        self.assertEqual(2, self.board.get_free_row(4))
        self.assertEqual(3, self.board.get_free_row(5))
        self.assertEqual(4, self.board.get_free_row(6))

    def test_is_full(self):
        self.assertEqual(False, self.board.is_full())
        for i in range(self.board.rows):
            for j in range(self.board.columns):
                self.board.slots[i][j] = 'X'
        self.assertEqual(True, self.board.is_full())

    def test_place_piece(self):
        expected_list = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         [' ', ' ', ' ', 'X', ' ', ' ', ' '],
                         [' ', ' ', 'X', 'X', 'X', ' ', ' '],
                         [' ', 'X', 'X', 'X', 'X', 'X', ' '],
                         ['X', 'X', 'X', 'X', 'X', 'X', 'X']]
        self.board.place_piece(0, 'X')
        self.board.place_piece(1, 'X')
        self.board.place_piece(1, 'X')
        self.board.place_piece(2, 'X')
        self.board.place_piece(2, 'X')
        self.board.place_piece(2, 'X')
        self.board.place_piece(3, 'X')
        self.board.place_piece(3, 'X')
        self.board.place_piece(3, 'X')
        self.board.place_piece(3, 'X')
        self.board.place_piece(4, 'X')
        self.board.place_piece(4, 'X')
        self.board.place_piece(4, 'X')
        self.board.place_piece(5, 'X')
        self.board.place_piece(5, 'X')
        self.board.place_piece(6, 'X')
        self.assertEqual(expected_list, self.board.slots)

    def test_win_horizontal(self):
        self.board.slots = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         ['X', 'X', 'X', 'X', ' ', ' ', ' ']]
        self.assertEqual(True, self.board.win('X'))
        self.board.slots = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         ['X', 'O', 'X', 'X', ' ', ' ', ' ']]
        self.assertEqual(None, self.board.win('X'))

    def test_win_vertical(self):
        self.board.slots = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         ['X', ' ', ' ', ' ', ' ', ' ', ' '],
                         ['X', ' ', ' ', ' ', ' ', ' ', ' '],
                         ['X', ' ', ' ', ' ', ' ', ' ', ' '],
                         ['X', ' ', ' ', ' ', ' ', ' ', ' ']]
        self.assertEqual(True, self.board.win('X'))
        self.board.slots = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         ['X', ' ', ' ', ' ', ' ', ' ', ' '],
                         ['X', ' ', ' ', ' ', ' ', ' ', ' '],
                         ['O', ' ', ' ', ' ', ' ', ' ', ' '],
                         ['X', ' ', ' ', ' ', ' ', ' ', ' ']]

        self.assertEqual(None, self.board.win('X'))

    def test_win_positive_diagonal(self):
        self.board.slots = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         [' ', ' ', ' ', 'X', ' ', ' ', ' '],
                         [' ', ' ', 'X', ' ', ' ', ' ', ' '],
                         [' ', 'X', ' ', ' ', ' ', ' ', ' '],
                         ['X', ' ', ' ', ' ', ' ', ' ', ' ']]
        self.assertEqual(True, self.board.win('X'))
        self.board.slots = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         [' ', ' ', ' ', ' ', 'X', ' ', ' '],
                         [' ', ' ', ' ', 'X', ' ', ' ', ' '],
                         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         [' ', 'X', ' ', ' ', ' ', ' ', ' '],
                         ['X', ' ', ' ', ' ', ' ', ' ', ' ']]
        self.assertEqual(None, self.board.win('X'))

    def test_win_negative_diagonal(self):
        self.board.slots = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         [' ', ' ', ' ', 'X', ' ', ' ', ' '],
                         [' ', ' ', ' ', ' ', 'X', ' ', ' '],
                         [' ', ' ', ' ', ' ', ' ', 'X', ' '],
                         [' ', ' ', ' ', ' ', ' ', ' ', 'X']]
        self.assertEqual(True, self.board.win('X'))
        self.board.slots = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         [' ', ' ', ' ', 'X', ' ', ' ', ' '],
                         [' ', ' ', ' ', ' ', 'X', ' ', ' '],
                         [' ', 'X', ' ', ' ', ' ', 'O', ' '],
                         ['X', ' ', ' ', ' ', ' ', ' ', 'X']]
        self.assertEqual(None, self.board.win('X'))

    def test_score_zero(self):
        self.board.slots = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         [' ', ' ', ' ', ' ', ' ', ' ', ' ']]
        self.assertEqual(0, self.board.score(self.player.piece))

    def test_score_1_piece(self):
        self.board.slots = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         ['X', ' ', ' ', ' ', ' ', ' ', ' ']]
        self.assertEqual(6, self.board.score(self.player.piece))

    def test_score_2_piece(self):
        self.board.slots = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         ['X', ' ', ' ', ' ', ' ', ' ', 'X']]
        self.assertEqual(12, self.board.score(self.player.piece))

    def test_score_2_piece_X_1_piece_O(self):
        self.board.slots = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         [' ', ' ', ' ', 'O', ' ', ' ', ' '],
                         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         ['X', ' ', ' ', ' ', ' ', ' ', 'X']]
        self.assertEqual(12, self.board.score(self.player.piece))

    # Test Player

    def test_player_opponent(self):
        self.assertEqual("O", self.player.opponent())

    @patch('builtins.input', return_value='1')
    def test_player_move(self, input):
        self.assertEqual(0, self.player.move(self.board))

    @patch('builtins.input', return_value='2')
    def test_player_move_2(self, input):
        self.assertEqual(1, self.player.move(self.board))

    @patch('builtins.input', return_value='7')
    def test_player_move_3(self, input):
        self.assertEqual(6, self.player.move(self.board))

    # in this case we would get into an infinite loop as the player's input is simulated
    # @patch('builtins.input', return_value='8')
    # def test_player_move_error(self, input):
    #     self.assertEqual(6, self.player.move(self.board))

    def test_pcplayer_move(self):
        random.seed(900) # results: 4, 1, 2
        self.assertEqual(self.pcplayer.move(self.board), 4)
        self.assertEqual(self.pcplayer.move(self.board), 1)
        self.assertEqual(self.pcplayer.move(self.board), 2)

    def test_AI_valid_move(self):
        self.board.slots = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         ['X', ' ', ' ', ' ', ' ', ' ', 'X']]
        expected_list = [0, 1, 2, 3, 4, 5, 6]
        self.assertEqual(expected_list, self.aiplayer.valid_move(self.board))

    def test_AI_valid_move_2_columns_full(self):
        self.board.slots = [['X', ' ', ' ', ' ', ' ', ' ', 'X'],
                            ['X', ' ', ' ', ' ', ' ', ' ', 'X'],
                            ['X', ' ', ' ', ' ', ' ', ' ', 'X'],
                            ['X', ' ', ' ', ' ', ' ', ' ', 'X'],
                            ['X', ' ', ' ', ' ', ' ', ' ', 'X'],
                            ['X', ' ', ' ', ' ', ' ', ' ', 'X']]
        expected_list = [1, 2, 3, 4, 5]
        self.assertEqual(expected_list, self.aiplayer.valid_move(self.board))

    def test_move_middle(self):
        self.board.slots = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         ['X', ' ', ' ', ' ', ' ', ' ', 'X']]
        self.assertEqual(3, self.aiplayer.move(self.board))

    def test_move_three_in_row(self):
        self.board.slots = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         ['X', 'X', 'X', ' ', ' ', ' ', ' ']]
        self.assertEqual(3, self.aiplayer.move(self.board))

    def test_move_three_in_column(self):
        self.board.slots = [[' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         [' ', ' ', ' ', ' ', ' ', ' ', ' '],
                         ['X', ' ', ' ', ' ', ' ', ' ', ' '],
                         ['X', ' ', ' ', ' ', ' ', ' ', ' '],
                         ['X', ' ', ' ', ' ', ' ', ' ', ' ']]
        self.assertEqual(0, self.aiplayer.move(self.board))

