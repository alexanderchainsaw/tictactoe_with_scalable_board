from random import getrandbits

from class_tictactoe import TicTacToe
from class_paint import Paint

x = Paint('X')
o = Paint('O')


def main():
    start_size = 3  # becomes very slow at around ~4k
    grow_by = 1  # board growth rate (the size of the board will be incremented by this amount)
    game = TicTacToe(size=start_size, grow=True, increment=grow_by)
    flag = bool(getrandbits(1))
    game.start(flag)
    while True:
        if flag:
            x_move = input(f"{x.red()}, enter your move: ")
            if x_move not in game.cells:
                continue
            game.move(x_move, player='X')
            if not game.check_win('X') and not game.moves:
                game.draw()
            flag = False
        else:
            o_move = input(f"{o.green()}, enter your move: ")
            if o_move not in game.cells:
                continue
            game.move(o_move, player='O')
            if not game.check_win('O') and not game.moves:
                game.draw()
            flag = True


if __name__ == '__main__':
    main()
