WHITE = 1
BLACK = 2


def transformation(char, color):
    if char == 'Q':
        return Queen(color)
    if char == 'R':
        return Rook(color)
    if char == 'B':
        return Bishop(color)
    if char == 'N':
        return Knight(color)


def opponent(color):
    if color == WHITE:
        return BLACK
    else:
        return WHITE


def correct_coords(row, col):
    """Функция проверяет, что координаты (row, col) лежат
    внутри доски"""
    return 0 <= row < 8 and 0 <= col < 8


class Pieces:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color


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
        """Возвращает строку из двух символов. Если в клетке (row, col)
        находится фигура, символы цвета и фигуры. Если клетка пуста,
        то два пробела."""
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
        '''Переместить фигуру из точки (row, col) в точку (row1, col1).
        Если перемещение возможно, метод выполнит его и вернёт True.
        Если нет --- вернёт False'''

        if not correct_coords(row, col) or not correct_coords(row1, col1):
            return False
        if row == row1 and col == col1:
            return False  # нельзя пойти в ту же клетку
        piece = self.field[row][col]
        if piece is None:
            return False
        if piece.get_color() != self.color:
            return False
        if self.field[row1][col1] is None:
            if not piece.can_move(self, row, col, row1, col1):
                return False
        elif self.field[row1][col1].get_color() == opponent(piece.get_color()):
            if not piece.can_attack(self, row, col, row1, col1):
                return False
        else:
            return False
        if isinstance(self.field[row][col], Rook) or isinstance(
                self.field[row][col], King):
            self.field[row][col].moved(True)
        self.field[row][col] = None  # Снять фигуру.
        self.field[row1][col1] = piece  # Поставить на новое место.
        self.color = opponent(self.color)
        return True

    def move_and_promote_pawn(self, row, col, row1, col1, char):
        piece = self.field[row][col]
        color = piece.get_color()
        if not (isinstance(piece, Pawn)):
            return False
        if self.move_piece(row, col, row1, col1) and (row1 == 7 or row1 == 0):
            self.field[row1][col1] = transformation(char,
                                                    color)  # Поставить на новое место.
            return True
        return False

    def castling0(self):
        if self.current_player_color() == WHITE:
            if not isinstance(self.field[0][0], Rook) or not isinstance(
                    self.field[0][4], King):
                return False
            if self.field[0][0].moved or self.field[0][4].moved:
                return False
            else:
                self.field[0][0] = None
                self.field[0][3] = Rook(self.color)
                self.field[0][4] = None
                self.field[0][2] = King(self.color)
                self.color = opponent(self.color)
                return True

        else:
            if not isinstance(self.field[7][0], Rook) or not isinstance(
                    self.field[7][4], King) \
                    or self.field[7][0].moved or self.field[7][4].moved:
                return False
            else:
                self.field[7][0] = None
                self.field[7][3] = Rook(self.color)
                self.field[7][4] = None
                self.field[7][2] = King(self.color)
                self.color = opponent(self.color)
                return True

    def castling7(self):
        if self.current_player_color() == WHITE:
            if not isinstance(self.field[0][7], Rook) or not isinstance(
                    self.field[0][4], King) \
                    or self.field[0][7].moved or self.field[0][4].moved:
                return False
            else:
                self.field[0][7] = None
                self.field[0][5] = Rook(self.color)
                self.field[0][4] = None
                self.field[0][6] = King(self.color)
                self.color = opponent(self.color)
                return True

        else:
            if not isinstance(self.field[7][7], Rook) or not isinstance(
                    self.field[7][4], King) \
                    or self.field[7][7].moved or self.field[7][4].moved:
                return False
            else:
                self.field[7][7] = None
                self.field[7][5] = Rook(self.color)
                self.field[7][4] = None
                self.field[7][6] = King(self.color)
                self.color = opponent(self.color)
                return True


class Rook(Pieces):
    def __init__(self, color):
        super().__init__(color)
        self.move = False

    def char(self):
        return 'R'

    def moved(self, move):
        self.move = move
        return self.move

    def can_move(self, board, row, col, row1, col1):
        # Невозможно сделать ход в клетку,
        # которая не лежит в том же ряду или столбце клеток.
        if row != row1 and col != col1:
            return False

        step = 1 if (row1 >= row) else -1
        for r in range(row + step, row1, step):
            # Если на пути по вертикали есть фигура
            if not (board.get_piece(r, col) is None):
                return False

        step = 1 if (col1 >= col) else -1
        for c in range(col + step, col1, step):
            # Если на пути по горизонтали есть фигура
            if not (board.get_piece(row, c) is None):
                return False
        return True

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)


class Pawn(Pieces):
    def __init__(self, color):
        super().__init__(color)

    def char(self):
        return 'P'

    def can_move(self, board, row, col, row1, col1):
        # Пешка может ходить только по вертикали
        # "взятие на проходе" не реализовано
        if col != col1:
            return False

        # Пешка может сделать из начального положения ход на 2 клетки
        # вперёд, поэтому поместим индекс начального ряда в start_row.
        if self.color == WHITE:
            direction = 1
            start_row = 1
        else:
            direction = -1
            start_row = 6

        # ход на 1 клетку
        if row + direction == row1:
            return True

        # ход на 2 клетки из начального положения
        if (row == start_row
                and row + 2 * direction == row1
                and board.field[row + direction][col] is None):
            return True
        return False

    def can_attack(self, board, row, col, row1, col1):
        direction = 1 if (self.color == WHITE) else -1
        return (row + direction == row1
                and (col + 1 == col1 or col - 1 == col1))


class Bishop(Pieces):
    def __init__(self, color):
        super().__init__(color)

    def can_move(self, board, row, col, row1, col1):
        if abs(row1 - row) == abs(col1 - col):
            return True
        return False

    def char(self):
        return 'B'

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)


class Knight(Pieces):
    def __init__(self, color):
        super().__init__(color)

    def can_move(self, board, row, col, row1, col1):
        if abs(col - col1) * abs(row - row1) == 2:
            return True
        return False

    def char(self):
        return 'N'

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)


class Queen(Pieces):
    def __init__(self, color):
        super().__init__(color)

    def can_move(self, board, row, col, row1, col1):
        piece = board.get_piece(row1, col1)
        if not (piece is None) and piece.get_color() == self.color:
            return False

        if row == row1 or col == col1:

            step = 1 if (row1 >= row) else -1
            for r in range(row + step, row1, step):
                if not (board.get_piece(r, col) is None):
                    return False

            step = 1 if (col1 >= col) else -1
            for c in range(col + step, col1, step):
                if not (board.get_piece(row, c) is None):
                    return False

            return True

        if row - col == row1 - col1:

            step = 1 if (row1 >= row) else -1
            for r in range(row + step, row1, step):
                c = col - row + r
                if not (board.get_piece(r, c) is None):
                    return False

            return True

        if row + col == row1 + col1:
            step = 1 if (row1 >= row) else -1
            for r in range(row + step, row1, step):
                c = row + col - r
                if not (board.get_piece(r, c) is None):
                    return False
            return True

        return False

    def char(self):
        return 'Q'

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)


class King(Pieces):
    def __init__(self, color):
        super().__init__(color)
        self.move = False

    def can_move(self, board, row, col, row1, col1):
        piece = board.get_piece(row1, col1)
        if not (piece is None) and piece.get_color() == self.color:
            return False
        if abs(row - row1) <= 1 and abs(col - col1) <= 1:
            return True
        return False

    def char(self):
        return 'K'

    def moved(self, move):
        self.move = move
        return self.move

    def can_attack(self, board, row, col, row1, col1):
        return self.can_move(board, row, col, row1, col1)


print("1")
board = Board()
board.field = [([None] * 8) for i in range(8)]
board.field[0][0] = Rook(WHITE)
board.field[0][4] = King(WHITE)
board.field[0][7] = Rook(WHITE)

board.field[7][0] = Rook(BLACK)
board.field[7][4] = King(BLACK)
board.field[7][7] = Rook(BLACK)

print('before:')
for row in range(7, -1, -1):
    for col in range(8):
        char = board.cell(row, col)[1]
        print(char.replace(' ', '-'), end='')
    print()
print()

print("Рокировка")
print(board.castling0())
print(board.castling7())

for row in range(7, -1, -1):
    for col in range(8):
        char = board.cell(row, col)[1]
        print(char.replace(' ', '-'), end='')
    print()
