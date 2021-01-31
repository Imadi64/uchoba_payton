for i in range(0, 16):
    b = int(input())
    if i % b == 0:
        print("ДА")
    else:
        print("НЕТ")
b = int(input())
if b == 1:
    print("ДА")
elif b == 2:
    print("ДА")
elif b == 4:
    print("ДА")
elif b == 8:
    print("ДА")
elif b == 16:
    print("ДА")
else:
    print("НЕТ")
