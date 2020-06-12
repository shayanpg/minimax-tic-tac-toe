import random
from src.main import game_state

BOARD_RANGE = range(1, 4)


def turn(board):
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
    return 'X' if turn(board) == 'O' else 'O'


def two(board, t):
    def check(lst):
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
    return [[i, j] for i in BOARD_RANGE
            for j in BOARD_RANGE
            if board.get(i, j) == '_']


def minimax(board, depth=1, sense=1):
    if game_state(board) == "Draw":
        return [[], 0]
    elif game_state(board) == turn(board):
        return [[], (1000 - depth) * sense]
    elif game_state(board) == opp(board):
        return [[], (-1000 - depth) * sense]
    elif depth == 3:
        score = 0
        if two(board, turn(board)):
            score += 100 * sense
        if two(board, opp(board)):
            score -= 100 * sense
        return [[], score]
    scores = []
    for move in find_moves(board):
        b = board.copy_board()
        Player().make_move(b, move)
        scores.append([move, minimax(b, depth + 1, -sense)])
    return max(scores, key=lambda x: x[1] * sense)


def randmove(board):
    return random.choice(find_moves(board))


class Player:
    def move(self, board):
        return randmove(board)

    def make_move(self, board, mv=None):
        try:
            if mv:
                x, y = mv
            else:
                x, y = self.move(board)
            if x not in range(1, 4) or y not in range(1, 4):
                print("Coordinates should be from 1 to 3!")
                self.make_move(board)
            elif not board.set(x, y, turn(board)):
                print("This cell is occupied! Choose another one!")
                self.make_move(board)
        except ValueError:
            print("You should enter numbers!")
            self.make_move(board)
        except IndexError:
            print("Please enter valid coordinates.")
            self.make_move(board)


class User(Player):
    def move(self, board):
        x, y = input("Enter the coordinates: ").split()
        return [int(x), int(y)]


class Easy(Player):
    def move(self, board):
        print('Making move level "easy"')
        return super().move(board)


class Medium(Player):
    def move(self, board):
        print('Making move level "medium"')
        us = two(board, turn(board))
        if us:
            return us
        them = two(board, opp(board))
        if them:
            return them
        else:
            return super().move(board)


class Hard(Player):
    def move(self, board):
        print('Making move level "hard"')
        return minimax(board)[0]
