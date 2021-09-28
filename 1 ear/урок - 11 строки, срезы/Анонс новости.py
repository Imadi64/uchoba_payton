a = int(input()) - 3
b = int(input())
for i in range(b):
    novost = input()
    if len(novost) > a + 3:
        print(novost[0:a], "...", sep="")
    else:
        print(novost)
