matrix = [[0, 0, 0, 0],
          [0, 0, 2, 0],
          [0, 1, 0, 0],
          [3, 0, 0, 4]]

def solve_sudoku(matrix):
    for i in range(len(matrix)):
        if matrix[0][0] == 0:
            if matrix[1][0] == 0:
                if matrix[2][0] == 0:
                    if matrix[3][0] == 0:



