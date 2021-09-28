a = int(input())
s = 0
f = ''
slow = dict()
while s != a:
    u = input()
    for i in range(len(u)):
        if u[i] != ' ':
            f += u[i]
        else:
            break
    u = u.split()
    del u[0]
    slow[f] = u
    f = ''
    s += 1
b = int(input())
for _ in range(b):
    new = input()
    if new not in slow:
        print('Нет в словаре')
    else:
        print(*slow[new])
