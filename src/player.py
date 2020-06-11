import random


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


class Player:
    def move(self, board):
        return self.randmove(board)

    def randmove(self, board):
        i, j = random.randrange(1, 4), random.randrange(1, 4)
        if board.get(i, j) == "_":
            return [i, j]
        else:
            return self.randmove(board)

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
        return [int(x) - 1, int(y) - 1]


class Easy(Player):
    def move(self, board):
        print('Making move level "easy"')
        return super().move(board)


class Medium(Player):
    def move(self, board):
        pass


class Hard(Player):
    pass
