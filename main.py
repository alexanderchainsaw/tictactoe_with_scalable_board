from random import getrandbits
from time import sleep

from class_tictactoe import TicTacToe
from class_paint import Paint

x = Paint('X')
o = Paint('O')


def main():
    start_size = 3  # becomes very slow around ~4k
    game = TicTacToe(size=start_size, ai=False, grow=True)
    game.display_greeting()
    sleep(1.5)
    flag = bool(getrandbits(1))
    game.display_first_move(flag=flag)
    game.display_board()

    while True:
        if flag:
            x_move = input(f"{x.red()}, enter your move: ")
            if x_move not in game.cells:
                continue
            game.move(x_move, player='X', opponent='O')
            game.display_board()
            if not game.check_win('X') and not game.moves:
                game.draw()

            flag = False
        else:
            x_move = input(f"{o.green()}, enter your move: ")
            if x_move not in game.cells:
                continue
            game.move(x_move, player='O', opponent='X')
            game.display_board()
            if not game.check_win('O') and not game.moves:
                game.draw()
            flag = True


if __name__ == '__main__':
    main()
