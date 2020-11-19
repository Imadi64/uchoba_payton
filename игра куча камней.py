x = 0
n = int(input())
while n > 1:
    n -= x
    if n > 6:
        if n % 2 == 0:
            n -= 3
            print(3, n)
            x = int(input())
            while not 0 < x < 4:
                print("Некорректный ход:", x)
                x = int(input())
        else:
            n -= 2
            print(2, n)
            x = int(input())
            while not 0 < x < 4:
                print("Некорректный ход:", x)
                x = int(input())
    elif n == 6:
        n -= 1
        print(1, n)
        x = int(input())
        while not 0 < x < 4:
            print("Некорректный ход:", x)
            x = int(input())
    elif n == 5:
        n -= 1
        print(1, n)
        x = int(input())
        while not 0 < x < 4:
            print("Некорректный ход:", x)
            x = int(input())
    elif n == 4:
        n -= 3
        print(3, n)
        print("ИИ выиграл!")
    elif n == 3:
        n -= 2
        print(2, n)
        print("ИИ выиграл!")
    elif n == 2:
        n -= 1
        print(1, n)
        print("ИИ выиграл!")
    elif n == 1:
        print("Вы выиграли!")
