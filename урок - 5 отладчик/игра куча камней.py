a = 0
n = input()
while not n.isdigit():
    print("Некорректный ход:", n)
    n = input()
n = int(n)
if n == 1:
    print(1, 0)
    print("Вы выиграли!")
while n > 1:
    n -= a
    if n % 4 == 0:
        n -= 3
        print(3, n)
    elif n % 4 == 3:
        n -= 2
        print(2, n)
    elif (n % 4 == 2) or (n % 4 == 1):
        n -= 1
        print(1, n)
    if n > 1:
        a = input()
        while (a != "1") and (a != "2") and (a != "3"):
            print("Некорректный ход:", a)
            a = input()
        a = int(a)
        print(a, n - a)
    if n == 1:
        print("ИИ выиграл!")
    if n == 0:
        print("Вы выиграли!")


# from random import randint
# x = 0
# n = int(input())
# while n > 0:
#     n -= x
#     if n > 5:
#         if (n - 5) % 4 == 1:
#             n -= 1
#             print(1, n)
#             x = int(input())
#             while not 0 < x < 4:
#                 print("Некорректный ход:", x)
#                 x = int(input())
#             print(x, n - x)
#         elif (n - 5) % 4 == 2:
#             n -= 2
#             print(2, n)
#             x = int(input())
#             while not 0 < x < 4:
#                 print("Некорректный ход:", x)
#                 x = int(input())
#             print(x, n - x)
#         elif (n - 5) % 4 == 3:
#             n -= 3
#             print(3, n)
#             x = int(input())
#             while not 0 < x < 4:
#                 print("Некорректный ход:", x)
#                 x = int(input())
#             print(x, n - x)
#         else:
#             a = randint(1, 3)
#             n -= a
#             print(a, n)
#             x = int(input())
#             while not 0 < x < 4:
#                 print("Некорректный ход:", x)
#                 x = int(input())
#             print(x, n - x)
#
#     elif n == 5:
#         n -= 1
#         print(1, n)
#         x = int(input())
#         while not 0 < x < 4:
#             print("Некорректный ход:", x)
#             x = int(input())
#         print(x, n - x)
#     elif n == 4:
#         n -= 3
#         print(3, n)
#         x = int(input())
#         while not 0 < x < 2:
#             print("Некорректный ход:", x)
#             x = int(input())
#         print(x, n - x)
#     elif n == 3:
#         n -= 2
#         print(2, n)
#         x = int(input())
#         while not 0 < x < 2:
#             print("Некорректный ход:", x)
#             x = int(input())
#         print(x, n - x)
#     elif n == 2:
#         n -= 1
#         print(1, n)
#         x = int(input())
#         while not x == 1:
#             print("Некорректный ход:", x)
#             x = int(input())
#         print(x, n - x)
#     elif n == 1:
#         n -= 1
#         print(1, n)
#         print("Вы выиграли!")
#     elif n == 0:
#         print("ИИ выиграл!")