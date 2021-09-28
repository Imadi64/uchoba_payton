n = int(input())
f1, f2, f3 = 1, 1, 1
if n <= 3:
    for i in range(n):
        print(f3, end=" ")
else:
    print(1, 1, end=" ")
    for i in range(n - 2):
        print(f3, end=" ")
        f1, f2, f3 = f2, f3, f1 + f2 + f3
