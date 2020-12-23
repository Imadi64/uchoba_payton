x = True
while x:
    num = int(input())
    deistvie = input()
    if deistvie == '!':
        if num >= 0:
            numm = 1
            for i in range(1, num + 1):
                numm *= i
            print(numm)
    elif deistvie != 'x':
        numm = int(input())
        if deistvie == '+':
            print(num + numm)
        elif deistvie == '-':
            print(num - numm)
        elif deistvie == '*':
            print(num * numm)
        elif deistvie == '/':
            if numm > 0:
                print(num // numm)
        elif deistvie == '%':
            if numm > 0:
                print(num % numm)
    else:
        print(num)
        x = False
