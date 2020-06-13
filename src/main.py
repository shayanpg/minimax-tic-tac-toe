from player import *
from board import *

BOARD_RANGE = range(1, 4)


def setup_commands(*args):
    """
    Preliminary operations to determine game difficulty, player types, and exit.
    :param args: player-given commands
    :return: difficulties/player types or new prompt
    """
    diff = ["user", "easy", "medium", "hard"]
    processed = []
    for i in range(len(args)):
        processed.append(args[i].lower())
    if len(processed) == 1 and processed[0] == "exit":
        exit(0)
    elif (
            len(processed) == 3
            and processed[0] == "start"
            and processed[1] in diff
            and processed[2] in diff
    ):
        return processed[1:]
    else:
        print("input 'start' with two player types or 'exit'")
        return setup_commands(*input("start or exit: ").split())


def dfclt(x):
    """
    Determine Player of type/difficulty given.
    :param x: input difficulty
    :return: Player requested
    """
    d = {"user": User, "easy": Easy, "medium": Medium, "hard": Hard}
    return d.get(x)()


def check_win(board, t):
    """
    Check if player T won the game.
    :param board: game's board
    :param t: turn (X or O)
    :return: whether T won or not
    """
    for i in BOARD_RANGE:
        across = all([board.get(i, j) == t for j in BOARD_RANGE])
        down = all([board.get(j, i) == t for j in BOARD_RANGE])
        if across or down:
            return True
    diag_p = all([board.get(i, i) == t for i in BOARD_RANGE])
    diag_n = all([board.get(i, 4-i) == t for i in BOARD_RANGE])
    return diag_n or diag_p


def game_state(board):
    """
    Determine game state (X wins, O wins, Tie, or Continue playing).
    :param board: game's board
    :return: winner or None if game not over
    """
    if check_win(board, 'X'):
        return "X"
    elif check_win(board, 'O'):
        return "O"
    elif len([i for row in board.get_board() for i in row if i == "_"]) == 0:
        return "draw"


def main():
    while True:
        x, o = setup_commands(*input("start or exit: ").split())
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
        if winner == "draw":
            print(winner)
        else:
            print(f"{winner} wins")


if __name__ == "__main__":
    main()
