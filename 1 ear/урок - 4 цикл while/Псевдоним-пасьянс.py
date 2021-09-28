a = int(input())
while a != 0:
    b = int(input())
    if b <= a and b > 0 and b <= 3:
        a = a - b
        print(a)
    else:
        print(a)