x = 0
n = int(input())
while n > 0:
    n -= x
    if n > 3:
        if n % 4 == 1:
            n -= 1
            print(1, n)
            x = int(input())
            while not 0 < x < 4:
                print("Некорректный ход:", x)
                x = int(input())
            print(x, n - x)
        elif n % 4 == 2:
            n -= 2
            print(2, n)
            x = int(input())
            while not 0 < x < 4:
                print("Некорректный ход:", x)
                x = int(input())
            print(x, n - x)
        elif n % 4 == 3:
            n -= 3
            print(3, n)
            x = int(input())
            while not 0 < x < 4:
                print("Некорректный ход:", x)
                x = int(input())
            print(x, n - x)
        else:
            n -= 1
            print(1, n)
            x = int(input())
            while not 0 < x < 4:
                print("Некорректный ход:", x)
                x = int(input())
            print(x, n - x)

    elif n == 3:
        n -= 3
        print(3, n)
        print("ИИ выиграл!")
    elif n == 2:
        n -= 2
        print(2, n)
        print("ИИ выиграл!")
    elif n == 1:
        n -= 1
        print(1, n)
        print("ИИ выиграл!")
    elif n == 0:
        print("Вы выиграли!")