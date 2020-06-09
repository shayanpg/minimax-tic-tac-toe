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


def move(board, loc):
    x, y = -1, -1
    try:
        x = int(loc[0]) - 1
        y = int(loc[1]) - 1
    except ValueError:
        print("You should enter numbers!")
        move(board, loc)
    except IndexError:
        print("Please enter valid coordinates.")
        move(board, loc)
    if x not in range(3) or y not in range(3):
        print("Coordinates should be from 1 to 3!")
        move(board, loc)
    elif board[2 - y][x] != "_":
        print("This cell is occupied! Choose another one!")
        move(board, loc)
    else:
        board[2 - y][x] = turn(board)


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
    else:
        e_counter = len([i for row in board for i in row if i == "_"])
        if e_counter > 0:
            return "Game not finished"
        else:
            return "Draw"


def main():
    board = setup_board(input("Enter cells: "))
    print_board(board)
    move(board, input("Enter the coordinates: ").split())
    print_board(board)
    print(game_state(board))


if __name__ == "__main__":
    main()
