def setup_board():
    cells = input("Enter cells: ").strip()
    assert len(cells) == 9
    board = []
    i = 0
    for j in range(3):
        board.append([])
        while i == 0 or i % 3 != 0:
            board[j].append(cells[i])
            i += 1
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


def move(board):
    loc = input("Enter the coordinates: ").split()
    x, y = -1, -1
    try:
        x = int(loc[0]) - 1
        y = int(loc[1]) - 1
    except ValueError:
        print("You should enter numbers!")
        move(board)
    except IndexError:
        print("Please enter valid coordinates.")
        move(board)
    if x not in range(3) or y not in range(3):
        print("Coordinates should be from 1 to 3!")
        move(board)
    elif board[2 - y][x] != "_":
        print("This cell is occupied! Choose another one!")
        move(board)
    else:
        board[2 - y][x] = turn(board)


def find_neighbors(x, y):
    neighbors = []
    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if x in range(3) and y in range(3) and (i, j) != (x, y):
                neighbors.append((i, j))
    return neighbors


def visit(board, x, y, visited, counter):
    if board[x][y] != turn:
        return False
    if counter == 3:
        return True
    for neighbor in find_neighbors(x, y):
        if not visited[neighbor[0]][neighbor[1]]:
            v = visit(board, neighbor[0], neighbor[1], visited, counter + 1)
            if v:
                return True
    return False


def check_win(board):
    visited = []
    for i in range(3):
        visited.append([False, False, False])
    for x in range(3):
        for y in range(3):
            if visit(board, x, y, visited, 1):
                return True
    return False


def game_state(board):
    if check_win(board):
        print("X wins")
    elif check_win(board):
        print("O wins")
    else:
        e_counter = len([i for row in board for i in row if i == "_"])
        if e_counter > 0:
            print("Game not finished")
        else:
            print("Draw")


def main():
    board = setup_board()
    print_board(board)
    move(board)
    print_board(board)
    game_state(board)


if __name__ == "__main__":
    main()
