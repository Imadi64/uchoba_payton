chislo1 = float(input())
chislo2 = float(input())
znak = input()
if znak == "+":
    print(chislo1 + chislo2)
elif znak == "-":
    print(chislo1 - chislo2)
elif znak == "*":
    print(chislo1 * chislo2)
elif znak == "/":
    if chislo2 != 0:
        print(chislo1 / chislo2)
    else:
        print(888888)
else:
    print(888888)
