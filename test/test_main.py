import unittest
import copy
from src.main import *
from src.board import *


class MainTests(unittest.TestCase):
    def test_setup(self):
        board = Board("XXO___XOX")
        t_board = [['X', 'X', 'O'],
                  ['_', '_', '_'],
                  ['X', 'O', 'X']]
        self.assertEqual(board.get_board(), t_board)
        board.print_board()

        board2 = Board("     XXO___XOX ")
        self.assertEqual(board2.get_board(), t_board)
        board2.print_board()

    def test_move(self):
        board = Board("_________")
        board_old = copy.deepcopy(board.get_board())
        p = Player()
        p.make_move(board, [1, 1])
        board_new = [['_', '_', '_'],
                   ['_', '_', '_'],
                   ['X', '_', '_']]
        self.assertEqual(board.get_board(), board_new)
        self.assertNotEqual(board.get_board(), board_old)

    def test_state(self):
        x_win = Board("XO_OXOO_X")
        x_win2 = Board("XXXXXXXXX")
        o_win = Board("O__OXXOX_")
        draw = Board("XOOOXXOXO")
        not_finished = Board("XOXOXO___")
        self.assertEqual(game_state(x_win), "X wins")
        self.assertEqual(game_state(x_win2), "X wins")
        self.assertEqual(game_state(o_win), "O wins")
        self.assertEqual(game_state(draw), "Draw")
        self.assertFalse(game_state(not_finished))

    def test_check_win(self):
        b = Board("XXXOO_XO_")
        self.assertTrue(check_win(b, 'X'))
        b = Board("X___X___X")
        self.assertTrue(check_win(b, 'X'))
        b = Board("__O_O_O__")
        self.assertTrue(check_win(b, 'O'))
        b = Board("_O__O__O_")
        self.assertTrue(check_win(b, 'O'))
        b = Board("X__X____X")
        self.assertFalse(check_win(b, 'X'))

    def test_medium(self):
        b = Board("XX_OXOXOO")
        m = Medium()
        m.make_move(b)
        self.assertEqual(game_state(b), "X wins")

        b = Board("_XOOX__OX")
        m.make_move(b)
        self.assertEqual(game_state(b), "X wins")


if __name__ == '__main__':
    unittest.main()
