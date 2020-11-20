chislo = input()
a = int(chislo[0])
b = int(chislo[1])
c = int(chislo[2])
x = a + b
y = b + c
sp = sorted([x, y], reverse = True)
print(str(sp[0]) + str(sp[1]))