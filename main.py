from random import getrandbits
from time import sleep

from class_tictactoe import TicTacToe
from class_paint import Paint

x = Paint('X')
o = Paint('O')


def main():
    starting_size = 3
    game = TicTacToe(size=starting_size, ai=False, grow=True)
    flag = bool(getrandbits(1))
    print(f'Starting...')
    sleep(1.5)
    game.display_first_move(flag=flag)
    game.display_board()

    while True:
        if flag:
            x_move = input(f"{x.red()}, enter your move: ")
            if x_move not in game.cells:
                continue
            game.move(x_move, player='X', opponent='O')
            game.display_board()
            game.check_win('X')
            flag = False
        else:
            x_move = input(f"{o.green()}, enter your move: ")
            if x_move not in game.cells:
                continue
            game.move(x_move, player='O', opponent='X')
            game.display_board()
            game.check_win('O')
            flag = True


if __name__ == '__main__':
    main()