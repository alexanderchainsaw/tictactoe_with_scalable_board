import unittest
from tictactoe_with_scalable_board.class_tictactoe import TicTacToe

a = TicTacToe


class TestTicTacToe(unittest.TestCase):
    """Testing the main usage cycle of the TicTacToe class:
    collect or reject proper size
    generate proper cells and rows
    assert proper amount of wins at different sized boards"""
    def test_win(self):
        pass
