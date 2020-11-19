god = int(input())
if god % 400 == 0:
    print("Високосный")
elif god % 4 == 0:
    if god % 100 == 0:
        print("Не високосный")
    else:
        print("Високосный")
else:
    print("Не високосный")