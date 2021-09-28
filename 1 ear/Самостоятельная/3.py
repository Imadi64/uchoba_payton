chislo = int(input())
spisok = []
for i in range(chislo):
    nabor1 = input()
    nabor2 = input()
    mno1 = set(nabor1)
    mno2 = set(nabor2)
    a = mno1 ^ mno2
    print(" ".join(a))