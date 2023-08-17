import unittest
import timeout_decorator
from tictactoe_with_scalable_board.class_tictactoe import TicTacToe
import cells

a = TicTacToe()


class TestTicTacToe(unittest.TestCase):
    """Testing TicTacToe class' functionality and efficiency"""
    @timeout_decorator.timeout(5)
    def test_win_5sec_size3(self):
        a.cells = cells.size3

    @timeout_decorator.timeout(5)
    def test_win_5sec_size10(self):
        a.cells = cells.size10

    @timeout_decorator.timeout(5)
    def test_win_5sec_size10(self):
        a.cells = cells.size100



