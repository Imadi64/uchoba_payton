chislo = int(input())
a = 0
for i in range(1, chislo):
    if chislo % i == 0:
        print(i, end=" ")
        a += 1
print(chislo)

if a >= 2:
    print("НЕТ")
else:
    print("ПРОСТОЕ")
