import random


def setup_commands(*args):
    diff = ["user", "easy"]
    if len(args) == 1 and args[0] == "exit":
        exit(0)
    elif (
            len(args) == 3
            and args[0] == "start"
            and args[1] in diff
            and args[2] in diff
    ):
        return args[1:]
    else:
        print("Bad parameters!")
        return setup_commands(*input("Input command: ").split())


def setup_board(cells):
    cells = cells.strip()
    assert len(cells) == 9
    board = []
    i = -1
    for j, c in enumerate(cells):
        if j % 3 == 0:
            board.append([])
            i += 1
        board[i].append(c)
    return board


def print_board(board):
    print("---------")
    for row in board:
        print('| ' + " ".join(row).replace("_", " ") + ' |')
    print("---------")


def turn(board):
    num_x, num_o = 0, 0
    for row in board:
        for i in row:
            if i == 'X':
                num_x += 1
            elif i == 'O':
                num_o += 1
    if num_x == num_o:
        return 'X'
    else:
        return 'O'


def move(board, player):
    try:
        x, y = player(board)
        if x not in range(3) or y not in range(3):
            print("Coordinates should be from 1 to 3!")
            move(board, player)
        elif board[2-y][x] != "_":
            print("This cell is occupied! Choose another one!")
            move(board, player)
        else:
            board[2-y][x] = turn(board)
    except ValueError:
        print("You should enter numbers!")
        move(board, input("Enter the coordinates: ").split())
    except IndexError:
        print("Please enter valid coordinates.")
        move(board, input("Enter the coordinates: ").split())


def user(board):
    x, y = input("Enter the coordinates: ").split()
    return int(x) - 1, int(y) - 1


def easy(board):
    i, j = random.randrange(3), random.randrange(3)
    if board[2-j][i] == "_":
        print('Making move level "easy"')
        return [i, j]
    else:
        return easy(board)


def dfclt(x):
    d = {"user": user, "easy": easy}
    return d.get(x)


def check_win(board, t):
    for i in range(3):
        across = all([board[i][j] == t for j in range(3)])
        down = all([board[j][i] == t for j in range(3)])
        if across or down:
            return True
    diag_n = all([board[i][i] == t for i in range(3)])
    diag_p = all([board[i][2 - i] == t for i in range(3)])
    return diag_n or diag_p


def game_state(board):
    if check_win(board, 'X'):
        return "X wins"
    elif check_win(board, 'O'):
        return "O wins"
    elif len([i for row in board for i in row if i == "_"]) == 0:
        return "Draw"


def main():
    while True:
        x, o = setup_commands(*input("Input command: ").split())
        x, o = dfclt(x), dfclt(o)
        board = setup_board("_________")
        print_board(board)
        winner = None
        while not winner:
            move(board, x)
            print_board(board)
            winner = game_state(board)
            if winner:
                break
            else:
                move(board, o)
                print_board(board)
        print(winner)


if __name__ == "__main__":
    main()
