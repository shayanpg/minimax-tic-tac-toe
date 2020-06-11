from src.player import *
from src.board import *

BOARD_RANGE = range(1, 4)


def setup_commands(*args):
    diff = ["user", "easy"]
    if len(args) == 1 and args[0] == "exit":
        exit(0)
    elif (
            len(args) == 3
            and args[0] == "start"
            and args[1].lower() in diff
            and args[2].lower() in diff
    ):
        return args[1:]
    else:
        print("Bad parameters!")
        return setup_commands(*input("Input command: ").split())


def dfclt(x):
    d = {"user": User, "easy": Easy, "medium": Medium, "hard": Hard}
    return d.get(x)()


def check_win(board, t):
    for i in BOARD_RANGE:
        across = all([board.get(i, j) == t for j in BOARD_RANGE])
        down = all([board.get(j, i) == t for j in BOARD_RANGE])
        if across or down:
            return True
    diag_p = all([board.get(i, i) == t for i in BOARD_RANGE])
    diag_n = all([board.get(i, 4-i) == t for i in BOARD_RANGE])
    return diag_n or diag_p


def game_state(board):
    if check_win(board, 'X'):
        return "X wins"
    elif check_win(board, 'O'):
        return "O wins"
    elif len([i for row in board.get_board() for i in row if i == "_"]) == 0:
        return "Draw"


def main():
    while True:
        x, o = setup_commands(*input("Input command: ").split())
        x, o = dfclt(x), dfclt(o)
        b = Board("_________")
        b.print_board()
        winner = None
        while not winner:
            x.make_move(b)
            b.print_board()
            winner = game_state(b)
            if winner:
                break
            else:
                o.make_move(b)
                b.print_board()
                winner = game_state(b)
        print(winner)


if __name__ == "__main__":
    main()
