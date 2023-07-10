import random
from class_paint import Paint

x = Paint('X')
o = Paint('O')


class TicTacToe:
    def __init__(self, size=3, ai=False, grow=False):
        self.grow = grow
        self.size = size

        cells = [str(i) for i in range(self.size ** 2)]
        maxlen = sorted((len(i) for i in cells), reverse=True)[0]
        self.cells = ['0' * (maxlen - len(i)) + i for i in cells]
        self.rows = [self.cells[i:i + size] for i in range(0, len(cells), size)]
        self.view = '\n'.join('-'.join(i) for i in self.rows)

        self.score_x, self.score_o = 0, 0
        self.ai = ai

    def __str__(self):
        return str(self.view)

    def _reset(self):
        if self.grow:
            self.size += 1
        size = self.size
        cells = [str(i) for i in range(self.size ** 2)]
        maxlen = sorted((len(i) for i in cells), reverse=True)[0]
        self.cells = ['0' * (maxlen - len(i)) + i for i in cells]
        self.rows = [self.cells[i:i + size] for i in range(0, len(cells), size)]
        self.view = '\n'.join('-'.join(i) for i in self.rows)

    def move(self, move, player, opponent):
        # if self.ai:
        #     ai_move = self._ai_move(playing_as=player, playing_vs=opponent)
        #     self.view = self.view.replace(ai_move, player)
        #     self.cells[self.cells.index(ai_move)] = player*len(ai_move)
        #     return True
        if move in self.cells:
            self.view = self.view.replace(move, player*len(move))
            self.cells[self.cells.index(move)] = player*len(move)
            return True
        return False

    def check_win(self, player: str):  # if win not 0 - upd score and display win and score, else False
        """ Determine whether the current board contains a win
            by converting winning board slices into a set
            If returned value is 2, then 2 win conditions reached == double win"""
        cells = self.cells
        size = self.size
        wins = [cells[i::size] for i in range(size)] + [cells[i*size:(i*size)+size] for i in range(size)]
        wins.append(cells[::size + 1])
        wins.append(cells[size - 1::size - 1][:-1])
        win = sum(1 for slce in wins if len(set(slce)) == 1)
        if player == 'X' and win:
            self._reset()
            self.score_x += win
            return self.display_victory('X'), self._display_score(), self.display_board()
        elif win:
            self._reset()
            self.score_o += win
            return self.display_victory('O'), self._display_score(), self.display_board()
        return False

    # def _ai_move(self, playing_as: str, playing_vs: str) -> str:  # returns a move (1-9)
    #     """ Priority in choice of moves:
    #         Win -> Disrupt enemy win ->
    #         -> Random secondary move (cell 5 is the priority) ->
    #         -> Random move from available (cell 5 is the priority)"""
    #     cells = self.cells
    #     size = self.size
    #     wins = [cells[i::size] for i in range(size)] + [cells[i * size:(i * size) + size] for i in range(size)]
    #     wins.append(cells[::size + 1])
    #     wins.append(cells[size - 1::size - 1][:-1])
    #     win_moves, break_moves = '', ''
    #     secondary_move = ''.join(''.join(i for i in j if i in '123456789')
    #                              for j in wins if playing_as in j and playing_vs not in j)
    #     for slce in wins:
    #         if slce.count(playing_as) == 2:
    #             win_moves += ''.join(i for i in slce if i in '123456789')
    #         if slce.count(playing_vs) == 2:
    #             break_moves += ''.join(i for i in slce if i in '123456789')
    #     if win_moves:
    #         return win_moves[0]
    #     elif break_moves:
    #         return break_moves[0]
    #     elif secondary_move:
    #         return '5' if '5' in secondary_move else random.choice(secondary_move)
    #     else:
    #         return '5' if '5' in self.cells else random.choice(self.cells)

    def display_board(self, draw=False):
        brd = self.view
        if not draw:
            return print('\n' + '\n'.join(row.replace('X', x.red()).replace('O', o.green())
                                   for row in brd.split('\n')) + '\n')
        else:
            return print('\n' + '\n'.join(row.replace('X', x.yellow()).replace('O', o.yellow())
                                   for row in brd.split('\n')) + '\n')

    def _display_score(self):
        """Display overall score"""
        return print(f'{" " * 15}Score:\n'
                     f'{" " * 15}{x.red()}: {self.score_x}\n'
                     f'{" " * 15}{o.green()}: {self.score_o}\n'
                     f'{"-" * 37}')

    @staticmethod
    def display_first_move(flag: bool):
        if flag:
            print(f'{x.red()} is first to make a move!')
        else:
            print(f'{o.green()} is first to make a move!')

    @staticmethod
    def display_victory(winner=None) -> print:
        if winner == 'X':
            print(f'{"-" * 37}\n', Paint(f'{"X Victory!" : ^37}').red() + f'\n{"-" * 37}')
        elif winner == 'O':
            print(f'{"-" * 37}\n',
                  Paint(f'{"O Victory!" : ^37}').green() + f'\n{"-" * 37}')
        else:
            print(f'{"-" * 37}\n',
                  Paint(f'{"Draw!" : ^37}').yellow() + f'\n{"-" * 37}')