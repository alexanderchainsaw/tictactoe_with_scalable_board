from random import getrandbits

from class_tictactoe import TicTacToe
from class_paint import Paint

x: Paint = Paint('X')
o: Paint = Paint('O')


def main():
    TicTacToe.Display.greeting()
    game: TicTacToe = TicTacToe(size=TicTacToe.collect_size(), grow=True)
    flag: bool = bool(getrandbits(1))
    game.start(flag)
    while True:
        if flag:
            x_move = input(f"{x.red()}, enter your move: ")
            if x_move not in game.cells:
                print("Invalid move. Try again.")
                continue
            game.move(x_move, player='X')
            flag = False
        else:
            o_move = input(f"{o.green()}, enter your move: ")
            if o_move not in game.cells:
                print("Invalid move. Try again.")
                continue
            game.move(o_move, player='O')
            flag = True


if __name__ == '__main__':
    main()
