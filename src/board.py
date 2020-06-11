class Board:
    def __init__(self, cells):
        self.board = []
        cells = cells.strip()
        assert len(cells) == 9
        i = -1
        for j, c in enumerate(cells):
            if j % 3 == 0:
                self.board.append([])
                i += 1
            self.board[i].append(c)

    def print_board(self):
        print("---------")
        for row in self.board:
            print('| ' + " ".join(row).replace("_", " ") + ' |')
        print("---------")

    def get_board(self):
        return self.board

    def get(self, x, y):
        return self.board[1-y][x-1]

    def set(self, x, y, t):
        if self.get(x, y) == '_':
            self.board[1-y][x-1] = t
            return True
        else:
            return False
