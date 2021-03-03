print1 = print


def print(*a):
    for i in a:
        print1(i.upper(), end=' ')




print("Нельзя ли потише?")