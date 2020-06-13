class Board:
    """Representation of game board."""

    def __init__(self, cells):
        """
        Constructor for board objects.
        :param cells: input starting game position
        """
        self.board = []
        cells = cells.strip()
        assert len(cells) == 9
        i = -1
        for j, c in enumerate(cells):
            if j % 3 == 0:
                self.board.append([])
                i += 1
            self.board[i].append(c)

    def copy_board(self):
        """
        create a copy of self.
        :return: a new board with the same state as this
        """
        arr = [i for row in self.get_board() for i in row]
        return Board("".join(arr))

    def print_board(self):
        """
        Prints out current board state.
        """
        print("---------")
        for row in self.board:
            print('| ' + " ".join(row).replace("_", " ") + ' |')
        print("---------")

    def get_board(self):
        """
        Getter method for board.
        :return: Board's internal representation
        """
        return self.board

    def get(self, x, y):
        """
        Getter method for specific location.
        :param x: horizontal position
        :param y: vertical position
        :return: piece at x, y, or '_' if none
        """
        return self.board[3-y][x-1]

    def set(self, x, y, t):
        """
        Setter method for board.
        :param x: horizontal position
        :param y: vertical position
        :param t: player
        :return: whether the piece was successfully set
        """
        if self.get(x, y) == '_':
            self.board[3-y][x-1] = t
            return True
        else:
            return False
