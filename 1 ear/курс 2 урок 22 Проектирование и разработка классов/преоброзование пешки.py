WHITE = 1
BLACK = 2


def opponent(color):
    if color == WHITE:
        return BLACK
    else:
        return WHITE


def correct_coords(row, col):
    return 0 <= row < 8 and 0 <= col < 8


class Board:
    def __init__(self):
        self.color = WHITE
        self.field = []
        for row in range(8):
            self.field.append([None] * 8)
        self.field[0] = [
            Rook(WHITE), Knight(WHITE), Bishop(WHITE), Queen(WHITE),
            King(WHITE), Bishop(WHITE), Knight(WHITE), Rook(WHITE)
        ]
        self.field[1] = [
            Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE),
            Pawn(WHITE), Pawn(WHITE), Pawn(WHITE), Pawn(WHITE)
        ]
        self.field[6] = [
            Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK),
            Pawn(BLACK), Pawn(BLACK), Pawn(BLACK), Pawn(BLACK)
        ]
        self.field[7] = [
            Rook(BLACK), Knight(BLACK), Bishop(BLACK), Queen(BLACK),
            King(BLACK), Bishop(BLACK), Knight(BLACK), Rook(BLACK)
        ]

    def current_player_color(self):
        return self.color

    def cell(self, row, col):
        piece = self.field[row][col]
        if piece is None:
            return '  '
        color = piece.get_color()
        c = 'w' if color == WHITE else 'b'
        return c + piece.char()

    def get_piece(self, row, col):
        if correct_coords(row, col):
            return self.field[row][col]
        else:
            return None

    def move_piece(self, row, col, row1, col1):
        if not correct_coords(row, col) or not correct_coords(row1, col1):
            return False
        if row == row1 and col == col1:
            return False
        piece = self.field[row][col]
        if piece is None:
            return False
        if piece.get_color() != self.color:
            return False
        if not piece.can_move(self, row, col, row1, col1):
            return False
        self.field[row][col] = None
        self.field[row1][col1] = piece
        piece.set_position(row1, col1)
        self.color = opponent(self.color)
        return True

    def is_under_attack(self, row, col, color):
        for i in range(8):
            for j in range(8):
                if self.field[i][j]:
                    if self.field[i][j].get_color() == color and\
                            self.field[i][j].can_move(row, col):
                        return True
        return False

    def move_and_promote_pawn(self, row, col, row1, col1, char):
        pwn = Pawn
        if not isinstance(self.field[row][col], pwn):
            return False
        if self.field[row1][col1] is not None:
            if not self.field[row][col].can_attack(self, row, col, row1, col1):
                return False
        else:
            if not self.field[row][col].can_move(self, row, col, row1, col1):
                return False
        p = self.field[row][col]
        self.field[row][col] = None
        if char == 'Q':
            self.field[row1][col1] = Queen(p.get_color())
        elif char == 'R':
            self.field[row1][col1] = Rook(p.get_color())
        elif char == 'B':
            self.field[row1][col1] = Bishop(p.get_color())
        elif char == 'N':
            self.field[row1][col1] = Knight(p.get_color())
        self.color = opponent(self.color)
        return True


class Piece:
    def __init__(self, color):
        self.color = color

    def can_move(self, board, row, col, row1, col1):
        if not correct_coords(row, col) or not correct_coords(row1, col1):
            return False
        if row == row1 and col == col1:
            return False
        if board.cell(row1, col1)[1] != ' ':
            if board.get_piece(row1, col1).get_color() == self.color:
                return False
        return True

    def set_position(self, row, col):
        self.row, self.col = row, col

    def get_color(self):
        return self.color

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)


class Pawn(Piece):
    def can_move(self, board, row, col, row1, col1):
        if not super().can_move(board, row, col, row1, col1):
            return False
        if col != col1:
            return False

        if self.color == WHITE:
            direction = 1
            start_row = 1
        else:
            direction = -1
            start_row = 6

        if row + direction == row1:
            return True

        if (row == start_row
                and row + 2 * direction == row1
                and board.field[row + direction][col] is None):
            return True
        return False

    def char(self):
        return 'P'

    def can_attack(self, board, row, col, row1, col1):
        if board.cell(row1, col1)[1] == ' ':
            return False
        if board.get_piece(row1, col1).get_color() == self.color:
            return False
        direction = 1 if (self.color == WHITE) else -1
        return (row + direction == row1
                and (col + 1 == col1 or col - 1 == col1))


class Rook(Piece):
    def can_move(self, board, row, col, row1, col1):
        if not super().can_move(board, row, col, row1, col1):
            return False

        if row != row1 and col != col1:
            return False
        step = 1 if (row1 >= row) else -1
        for r in range(row + step, row1, step):
            if not (board.get_piece(r, col) is None):
                return False
        step = 1 if (col1 >= col) else -1
        for c in range(col + step, col1, step):
            if not (board.get_piece(row, c) is None):
                return False
        return True

    def char(self):
        return 'R'


class Knight:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def char(self):
        return 'N'

    def get_color(self):
        return self.color

    def can_move(self, row, col):
        if not (0 <= row < 8 and 0 <= col < 8):
            return False
        if abs(self.col - col) * abs(
                self.row - row) == 2 and self.row != row and self.col != col:
            return True
        return False


class Bishop:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def char(self):
        return 'B'

    def get_color(self):
        return self.color

    def can_move(self, row, col):
        if not (0 <= row < 8 and 0 <= col < 8):
            return False
        if abs(row - self.row) == abs(col - self.col):
            return True
        return False


class Queen:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color

    def set_position(self, row, col):
        self.row = row
        self.col = col

    def char(self):
        return 'Q'

    def get_color(self):
        return self.color

    def can_move(self, row, col):
        if not (0 <= row < 8 and 0 <= col < 8):
            return False
        if abs(row - self.row) == abs(col - self.col):
            return True
        if self.row != row and self.col != col:
            return False
        return True


class King(Piece):
    def can_move(self, board, row, col, row1, col1):
        if not super().can_move(board, row, col, row1, col1):
            return False
        if abs(row - row1) > 1 or abs(col - col1) > 1:
            return False
        return True

    def char(self):
        return 'K'
