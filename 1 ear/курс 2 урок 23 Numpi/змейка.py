import numpy


def snake(rows, cols):
    a = numpy.fromiter(map(int, range(1, rows * cols + 1)),
                       dtype='int8').reshape(rows, cols)
    for i in range(len(a)):
        if i % 2 == 0:
            continue
        else:
            i1 = sorted(a[i], reverse=True)
            a[i] = i1
    return a


print(snake(10, 20))
