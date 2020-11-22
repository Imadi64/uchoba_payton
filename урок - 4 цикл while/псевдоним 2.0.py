a = int(input())
while a > 0:
    if a % 2 == 0:
        b = 2
        a -= b
        print(b, a)
    elif a % 2 != 0:
        b = 3
        a -= b
        print(b, a)
    elif a % 2 != 0 and a < 3:
        b = 1
        a -= b
        print(b, a)
    if a == 0:
        print('ИИ выиграл')
    xi = int(input())
    while xi > 3 or xi < 1 is True:
        if xi > 3 or xi < 1:
            print('Некорректный ход', xi)
            del xi
            xi = int(input())
        else:
            a -= xi
            print(xi, a)
            if a == 0:
                print('Вы выиграли!')