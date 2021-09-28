chislo = int(input())
zvezdi = "*"
a = 0
for i in range(chislo):
    a = chislo - i - 1
    print(" " * a + zvezdi + "*" * i + "*" * i)
