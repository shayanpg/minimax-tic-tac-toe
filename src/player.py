import random
from src.main import game_state

BOARD_RANGE = range(1, 4)


def turn(board):
    """
    Find whose turn it is.
    :param board: current board state
    :return: next piece to be played
    """
    num_x, num_o = 0, 0
    for row in board.get_board():
        for i in row:
            if i == 'X':
                num_x += 1
            elif i == 'O':
                num_o += 1
    if num_x == num_o:
        return 'X'
    else:
        return 'O'


def opp(board):
    """
    Find whose turn it isn't.
    :param board: current board state
    :return: opposite piece of turn(board)
    """
    return 'X' if turn(board) == 'O' else 'O'


def two(board, t):
    """
    Check if T has the opportunity to win if they're next
    (available two in a row).
    :param board: current board state
    :param t: piece to check for available wins
    :return: position T can take for a win
    """
    def check(lst):
        """
        Verify a row represents a win opportunity.
        :param lst: board row
        :return: whether lst represents a win opportunity
        """
        return sum([k == t for k in lst]) == 2 and '_' in lst
    for i in BOARD_RANGE:
        down = [board.get(i, j) for j in BOARD_RANGE]
        if check(down):
            for j in range(len(down)):
                if down[j] == '_':
                    return [i, j+1]
        across = [board.get(j, i) for j in BOARD_RANGE]
        if check(across):
            for j in range(len(across)):
                if across[j] == '_':
                    return [j+1, i]
    diag_p = [board.get(i, i) for i in BOARD_RANGE]
    if check(diag_p):
        for i in range(len(diag_p)):
            if diag_p[i] == '_':
                return [i+1, i+1]
    diag_n = [board.get(i, 4 - i) for i in BOARD_RANGE]
    if check(diag_n):
        for i in range(len(diag_n)):
            if diag_n[i] == '_':
                return [i+1, 3-i]


def find_moves(board):
    """
    Find all open positions on the board.
    :param board: current board state
    :return: collection of available moves
    """
    return [[i, j] for i in BOARD_RANGE
            for j in BOARD_RANGE
            if board.get(i, j) == '_']


def minimax(board, depth=4, sense=1, alpha=float("-inf"), beta=float("inf")):
    """
    Minimax algorithm looking multiple moves ahead to determine optimal moves.
    Uses alpha-beta pruning.
    :param board: current board state
    :param depth: number of turns ahead to look
    :param sense: determines whether player is minimizing or maximizing score
    :param alpha: lower bound for maximum score
    :param beta: upper bound for minimum score
    :return: optimal move
    """
    if game_state(board) == "draw":
        return [[], 0]
    elif game_state(board) == turn(board):
        return [[], (1000 + depth) * sense]
    elif game_state(board) == opp(board):
        return [[], (-1000 + depth) * sense]
    elif depth == 0:
        score = 0
        if two(board, turn(board)):
            score += 100 * sense
        if two(board, opp(board)):
            score -= 100 * sense
        return [[], score]
    best_move = []
    result = float('inf') * -sense
    for move in find_moves(board):
        b = board.copy_board()
        Player().make_move(b, move)
        curr = minimax(b, depth - 1, -sense, alpha, beta)[1]
        if curr > result and sense == 1 or curr < result and sense == -1:
            best_move, result = move, curr
        if sense == 1:
            alpha = max(alpha, curr)
        else:
            beta = min(beta, curr)
        if alpha >= beta:
            break
    return [best_move, result]


def randmove(board):
    """
    Creates a random valid move.
    :param board: current board state
    :return: random move
    """
    return random.choice(find_moves(board))


class Player:
    """Generic player interface."""

    def move(self, board):
        """
        Move generation method.
        :param board: current board state
        :return: coordinates
        """
        return randmove(board)

    def make_move(self, board, mv=None):
        """
        Process a move (given or generated).
        :param board: current board state
        :param mv: optional given move. used for testing
        """
        try:
            if mv:
                x, y = mv
            else:
                x, y = self.move(board)
            if x not in range(1, 4) or y not in range(1, 4):
                print("coordinates should be from 1 to 3")
                self.make_move(board)
            elif not board.set(x, y, turn(board)):
                print("cell occupied")
                self.make_move(board)
        except ValueError:
            print("invalid symbols")
            self.make_move(board)
        except IndexError:
            print("invalid coordinates")
            self.make_move(board)


class User(Player):
    """Human player"""

    def move(self, board):
        """
        Override.
        :param board: current board state
        :return: coordinates
        """
        x, y = input("player move (coordinates): ").split()
        return [int(x), int(y)]


class Easy(Player):
    """Easy difficulty"""

    def move(self, board):
        """
        Override.
        :param board: current board state
        :return: coordinates
        """
        print('computer move (easy)')
        return super().move(board)


class Medium(Player):
    """Medium difficulty"""

    def move(self, board):
        """
        Override.
        :param board: current board state
        :return: coordinates
        """
        print('computer move (medium)')
        us = two(board, turn(board))
        if us:
            return us
        them = two(board, opp(board))
        if them:
            return them
        else:
            return super().move(board)


class Hard(Player):
    """Hard difficulty"""

    def move(self, board):
        """
        Override.
        :param board: current board state
        :return: coordinates
        """
        print('computer move (hard)')
        return minimax(board)[0]
