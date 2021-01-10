n = int(input())
iq1 = 0
for i in range(1, n + 1):
    iq = int(input())
    iq1 += iq
    cof = iq1 / i
    if cof == iq:
        print(0)
    elif cof > iq:
        print('<')
    else:
        print('>')
