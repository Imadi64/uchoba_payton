import numpy


class Table(object):
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.tabl = numpy.zeros((self.rows, self.cols), dtype=int)
        pass

    def set_value(self, row, col, value):
        self.tabl[row, col] = value

    def get_value(self, row, col):
        if row > self.rows - 1 or col > self.cols - 1 or row < 0 or col < 0:
            return None
        else:
            return self.tabl[row, col]

    def n_rows(self):
        return self.rows

    def n_cols(self):
        return self.cols

    def add_row(self, row):
        b = numpy.zeros(self.cols, dtype=int)
        niz = self.tabl[row:, :]
        verh = numpy.vstack((self.tabl[:row, :], b))
        self.tabl = numpy.vstack((verh, niz))
        self.rows += 1

    def add_col(self, col):
        a = numpy.zeros((self.rows, 2), dtype=int)
        b = a[:, :1]
        right = self.tabl[:, col:]
        # ss = self.tabl[:, :col]
        left = numpy.hstack((self.tabl[:, :col], b))
        self.tabl = numpy.hstack((left, right))
        self.cols += 1

    def delete_col(self, col):
        right = self.tabl[:, col + 1:]
        left = self.tabl[:, :col]
        self.tabl = numpy.hstack((left, right))
        self.cols -= 1

    def delete_row(self, row):
        verh = self.tabl[:row, :]
        niz = self.tabl[row + 1:, :]
        self.tabl = numpy.vstack((verh, niz))
        self.rows -= 1
