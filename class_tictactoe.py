from class_paint import Paint
from time import sleep

x = Paint('X')
o = Paint('O')


class TicTacToe:
    def __init__(self, size=3, grow=False, increment=1):
        """Initialisation using size variable as dimensions for the generated board such as:
        size=N will create a board of N-by-N size

        grow: bool variable for determining the mode of the game:
        if true, the size will be incremented by a set amount each cycle of the game (each win or draw)

        increment: int by which amount the size will increase if grow=True

        maxlen: int variable is the maximum length of a str cell number, needed for proper board display of any size,
        used in cells generation: if current cell is shorter than maxlen, additional zeroes are added at the beginning:
        if the longest cell is 100, the 1 cell becomes 001, 2 becomes 002 and so on

        rows: two-dim array, generated to be joined into the view, which will be used by the display_board() method
        to display the board into the terminal

        moves: integer count of all possible moves to be made on current board. Used for determining a draw:
        if no moves are available and neither player won - it's a draw"""
        self.size: int = size
        self.grow: bool = grow
        self.increment = increment
        maxlen: int = len(str((size ** 2) - 1))
        self.cells: [str] = ['0' * (maxlen - len(str(i))) + str(i) for i in range(self.size ** 2)]
        self.rows: [[str]] = (self.cells[i:i + size] for i in range(0, len(self.cells), size))
        self.view: str = '\n'.join('-'.join(i) for i in self.rows)
        self.moves: int = len(self.cells)

        self.score_x, self.score_o = 0, 0

    def start(self, flag):
        """For first launch of the game, execute associated methods"""
        self._display_greeting()
        self._display_first_move(flag=flag)
        self._display_board()

    def _reset(self):
        """Resetting the board and associated variables, if grow=True - increment size with a set amount"""
        if self.grow:
            self.size += self.increment
        size = self.size
        maxlen = len(str((size ** 2) - 1))
        self.cells = ['0' * (maxlen - len(str(i))) + str(i) for i in range(self.size ** 2)]
        self.rows = [self.cells[i:i + size] for i in range(0, len(self.cells), size)]
        self.view = '\n'.join('-'.join(i) for i in self.rows)
        self.moves = len(self.cells)

    def move(self, move: str, player: str):
        """move: str number of the cell

        player: which player is making a move (X or O)

        Replace cell with player move both in the view and in the cells, update moves and then display updated view

        Check for win and draw conditions"""
        self.view = self.view.replace(move, player*len(move))
        self.cells[self.cells.index(move)] = player*len(move)
        self.moves -= 1
        self._display_board()
        if not self._check_win(player) and not self.moves:
            self._draw()

    def _check_win(self, player: str):
        """Determine whether the current board contains a win
        by converting winning board slices into a set() - if the length of the resulted set equals 1,
        then it consists only of one element - O or X, which means the game is over.
        To trigger the victory scenario, win variable needs to be >= 1, but there are possible scenarios
        when the player can reach 2 or even 3 victories at once with one move. For this purpose,
        there is a match case statement to trigger corresponding victory scenarios

        If any of the players won, no matter the case, the following set of commands is executed:
        reset the board, increment winner score, display winner and score,
        then after a short pause display fresh board"""
        cells = self.cells
        size = self.size
        # gathering winning slices for any size of the board:
        wins = [cells[i::size] for i in range(size)] + [cells[i*size:(i*size)+size] for i in range(size)]
        wins.append(cells[::size + 1])
        wins.append(cells[size - 1::size - 1][:-1])
        # counting wins by set() conversion:
        win = sum(1 for slce in wins if len(set(slce)) == 1)
        if win:
            self._reset()
            if player == 'X':
                self.score_x += win
                match win:
                    case 1:
                        return self._display_victory('X'), self._display_score(), \
                            sleep(1.5), self._display_board()
                    case 2:
                        return self._display_victory('X', double=True), \
                            self._display_score(), sleep(1.5), self._display_board()
                    case 3:
                        return self._display_victory('X', triple=True), \
                            self._display_score(), sleep(1.5), self._display_board()
            elif player == 'O':
                self.score_o += win
                match win:
                    case 1:
                        return self._display_victory('O'), self._display_score(), \
                            sleep(1.5), self._display_board()
                    case 2:
                        return self._display_victory('O', double=True), \
                            self._display_score(), sleep(1.5), self._display_board()
                    case 3:
                        return self._display_victory('O', triple=True), \
                            self._display_score(), sleep(1.5), self._display_board()
        return False

    def _draw(self):
        """Draw scenario, increment both scores by half a point, call _reset(), print the board painted in yellow"""
        brd = self.view
        self.score_o += 0.5
        self.score_x += 0.5
        self._reset()
        return print('\n\t' + '\n\t'.join(row.replace('X', x.yellow()).replace('O', o.yellow())
                                          for row in brd.split('\n')) + '\n'), \
            self._display_victory(), self._display_score(), sleep(1.5), self._display_board()

    def _display_board(self):
        """For displaying the board, replaces player-placed X's and O's with painted objects"""
        brd = self.view
        print('\n\t' + '\n\t'.join(row.replace('X', x.red()).replace('O', o.green())
                                   for row in brd.split('\n')) + '\n')

    def _update_score(self, player, points):
        """Update score of a player."""
        match player:
            case 'X':
                self.score_x += points
            case 'O':
                self.score_o += points

    def _display_score(self):
        """Display overall score"""
        print('\tScore:\n'
              f'\t{x.red()}: {self.score_x}\n'
              f'\t{o.green()}: {self.score_o}\n')

    @staticmethod
    def _display_greeting():
        """Display pretty greeting"""
        print('Welcome to...\n')
        sleep(1)
        print(f'\t{Paint("Tic").red()}{Paint("Tac").green()}{Paint("Toe").cyan()}\n')
        sleep(1)

    @staticmethod
    def _display_first_move(flag: bool):
        """Announce who is the first to make a move"""
        if flag:
            print(f'{x.red()} is first to make a move!')
        else:
            print(f'{o.green()} is first to make a move!')

    @staticmethod
    def _display_victory(winner=None, double=False, triple=False):
        """Announce winner if such exists, if not - announce draw"""
        if winner == 'X':
            print('\n\t', Paint("X Victory!").red(), '\n')
        elif winner == 'O':
            print('\n\t', Paint("O Victory!").green(), '\n')
        else:
            print('\n\t', Paint("Draw!").yellow(), '\n')
        if double:
            print('\n\t', Paint("DOUBLE WIN!").cyan(), '\n')
        if triple:
            print('\n\t', Paint("TRIPLE WIN!!!").magenta(), '\n')
