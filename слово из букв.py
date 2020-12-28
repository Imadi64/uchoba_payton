lydi = set()
pausa = set()
a = int(input())
b = int(input())
c = int(input())
cout = 0
for i in range(a + b + c):
    name = input()
    if name in lydi:
        cout += 1
        pausa.add(name)
    lydi.add(name)
if (a == b == c) and len(lydi) == a:
    print('NO')
else:
    if len(pausa) + cout > 0:
        if ((len(pausa) + cout) % 2 != 0):
            print((len(pausa) + cout) % 2)
        else:
            print((len(pausa) + cout) // 2)
    else:
        print('NO')
