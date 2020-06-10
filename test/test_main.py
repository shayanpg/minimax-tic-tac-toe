import unittest
import copy
from src import main


class MainTests(unittest.TestCase):
    def test_setup(self):
        board = main.setup_board("XXO___XOX")
        t_board = [['X', 'X', 'O'],
                  ['_', '_', '_'],
                  ['X', 'O', 'X']]
        self.assertEqual(board, t_board)
        main.print_board(board)

        board2 = main.setup_board("     XXO___XOX ")
        self.assertEqual(board2, t_board)
        main.print_board(board2)

    def test_move(self):
        board = main.setup_board("_________")
        board_old = copy.deepcopy(board)
        main.move(board, [1, 1])
        board_new = main.setup_board("______X__")
        self.assertEqual(board, board_new)
        self.assertNotEqual(board, board_old)

    def test_state(self):
        x_win = main.setup_board("XO_OXOO_X")
        x_win2 = main.setup_board("XXXXXXXXX")
        o_win = main.setup_board("O__OXXOX_")
        draw = main.setup_board("XOOOXXOXO")
        not_finished = main.setup_board("XOXOXO___")
        self.assertEqual(main.game_state(x_win), "X wins")
        self.assertEqual(main.game_state(x_win2), "X wins")
        self.assertEqual(main.game_state(o_win), "O wins")
        self.assertEqual(main.game_state(draw), "Draw")
        self.assertFalse(main.game_state(not_finished))


if __name__ == '__main__':
    unittest.main()
