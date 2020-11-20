chislo = float(input())
if chislo <= 0.000001:
    if chislo >= -0.000001:
        chislo = 0.000001
print(1 / chislo)
